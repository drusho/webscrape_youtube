# import libraries
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
options.add_argument("headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)


# Chrome driver location (for M1 macbook air)
DRIVER_PATH = "/opt/homebrew/bin/chromedriver"

# activate driver
driver = webdriver.Chrome(executable_path=DRIVER_PATH)


# Scroll to bottom of page
def scroll_page():
    for x in range(7):
        html = driver.find_element_by_tag_name("html")
        html.send_keys(Keys.END)
        time.sleep(2)


def scrap_videos():
    scroll_page()

    chan_xpath = '//*[@id="channel-name"]'
    subs_xpath = '//*[@id="subscriber-count"]'
    videos_class = "style-scope ytd-grid-video-renderer"
    views_xpath = './/*[@id="metadata-line"]/span[1]'
    post_date_xpath = './/*[@id="metadata-line"]/span[2]'

    title_xpath = './/*[@id="video-title"]'

    # Scrap Channel Name
    try:
        channel_name = driver.find_element_by_xpath(chan_xpath).text
    except (Exception,):
        pass

    # Scrap Number of Subscribers
    try:
        subscribers = driver.find_element_by_xpath(subs_xpath).text
    except (Exception,):
        pass

    # Reassign variable to recalculate all videos
    videos = driver.find_elements_by_class_name(videos_class)

    # Loop through all videos
    for video in videos:

        # grab title if available
        try:
            title = video.find_element_by_xpath(title_xpath).text
        except (Exception,):
            pass

        # grab url if available
        try:
            url = video.find_element_by_xpath(title_xpath).get_attribute("href")
        except (Exception,):
            pass

        # grab views if available
        try:
            views = video.find_element_by_xpath(views_xpath).text
        except (Exception,):
            pass

        # grab post date if available
        try:
            post_date = video.find_element_by_xpath(post_date_xpath).text
        except (Exception,):
            pass

        video_items = {
            "channel_name": channel_name,
            "subscribers": subscribers,
            "title": title,
            "views": views,
            "post_date": post_date,
            "url": url,
        }

        vid_list.append(video_items)

    return vid_list


# scrap About section
def scrap_about():

    chan_name_xp = '//*[@id="channel-name"]'
    chan_join = './/*[@id="right-column"]/yt-formatted-string[2]/span[2]'
    chan_views = './/*[@id="right-column"]/yt-formatted-string[3]'
    chan_desc = './/*[@id="description"]'

    # Scrap Channel Name
    try:
        channel_name = driver.find_element_by_xpath(chan_name_xp).text
    except (Exception,):
        pass

    # Scrap Channel Join Date (about)
    try:
        channel_join = driver.find_element_by_xpath(chan_join).text
    except (Exception,):
        pass

    # Scrap Channel Views (about)
    try:
        channel_views = driver.find_element_by_xpath(chan_views).text
    except (Exception,):
        pass

    # Scrap Channel Description (about)
    try:
        channel_description = driver.find_element_by_xpath(chan_desc).text
    except (Exception,):
        pass

    about_items = {
        "channel_name": channel_name,
        "channel_join_date": channel_join,
        "channel_views": channel_views,
        "channel_description": channel_description,
    }

    vid_list.append(about_items)
    return vid_list


# top youtubers based off 'https://blog.bit.ai'
top_youtubers = [
    "ijustine",
    "AndroidAuthority",
    "Mrwhosetheboss",
    "TechnoBuffalo",
    "TLD",
    "austinevans",
    "unboxtherapy",
    "LinusTechTips",
    "UrAvgConsumer",
    "mkbhd",
]

# empty list to hold video details
vid_list = []

# url of most videos sorted by most popular
for youtuber in top_youtubers:
    print(f"processing {youtuber}")
    url = f"https://www.youtube.com/{youtuber}/videos?view=0&sort=p&flow=grid"
    driver.get(url)
    scroll_page()
    vid_list = scrap_videos()
    about_url = f"https://www.youtube.com/{youtuber}/about"
    about = driver.get(about_url)
    driver.implicitly_wait(10)
    about_items = scrap_about()

# Close Chrome browser
driver.quit()

# create pandas df for video info
df_channel = pd.DataFrame(vid_list)

# export df to csv
df_channel.to_csv("yt_channel_scrap.csv")

print(df_channel.shape)

print(df_channel.head(10))
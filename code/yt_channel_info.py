# import libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


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
    # scroll_page()

    # Scrap Channel Name
    try:
        channel_name = driver.find_element_by_xpath('//*[@id="channel-name"]').text
    except:
        channel_name = ""

    # Scrap Number of Subscribers
    try:
        subscribers = driver.find_element_by_xpath('//*[@id="subscriber-count"]').text
    except:
        subscribers = ""

    # Reassign variable to recalculate all videos
    videos = driver.find_elements_by_class_name("style-scope ytd-grid-video-renderer")

    # Loop through all videos
    for video in videos:

        # grab title if available
        try:
            title = video.find_element_by_xpath('.//*[@id="video-title"]').text
        except:
            title = ""

        # grab url if available
        try:
            url = video.find_element_by_xpath('.//*[@id="video-title"]').get_attribute(
                "href"
            )
        except:
            url = ""

        # grab views if available
        try:
            views = video.find_element_by_xpath(
                './/*[@id="metadata-line"]/span[1]'
            ).text
        except:
            views = ""

        # grab post date if available
        try:
            post_date = video.find_element_by_xpath(
                './/*[@id="metadata-line"]/span[2]'
            ).text
        except:
            post_date = ""

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

    # Scrap Channel Name
    try:
        channel_name = driver.find_element_by_xpath('//*[@id="channel-name"]').text
    except:
        channel_name = ""

    # Scrap Channel Join Date (about)
    try:
        channel_join = driver.find_element_by_xpath(
            './/*[@id="right-column"]/yt-formatted-string[2]/span[2]'
        ).text
    except:
        channel_join = ""

    # Scrap Channel Views (about)
    try:
        channel_views = driver.find_element_by_xpath(
            './/*[@id="right-column"]/yt-formatted-string[3]'
        ).text
    except:
        channel_views = ""

    # Scrap Channel Description (about)
    try:
        channel_description = driver.find_element_by_xpath(
            './/*[@id="description"]'
        ).text
    except:
        channel_description = ""

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
df_vids = pd.DataFrame(vid_list)

# export df to csv
df_vids.to_csv("yt_channel_scrap.csv")

print(df_vids.shape)

print(df_vids.head(10))
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from requests import options
from selenium import webdriver


start_time = datetime.now()


# instantiate a chrome options object so you can set the size and headless preference
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")

# Chrome driver location (for M1 macbook air)
DRIVER_PATH = "/opt/homebrew/bin/chromedriver"

# activate driver
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# video duration
def duration():
    duration_x = "//span[@class='ytp-time-duration']"
    duration = driver.find_elements_by_xpath(duration_x)[0].text
    return duration

    # convert duration to only seconds
    # duration = time.strptime(video_time, "%M:%S")
    # d_convert = datetime.timedelta(minutes=x.tm_min, seconds=x.tm_sec).total_seconds()


# partial description
def par_description():
    vid_desc = "//div[@class='watch-main-col']/meta[@itemprop='description']"
    elems = driver.find_elements_by_xpath(vid_desc)
    for elem in elems:
        return elem.get_attribute("content")


# Full Description
def full_description():
    vid_desc = "//span[@class='style-scope yt-formatted-string']"
    elems = driver.find_elements_by_xpath(vid_desc)
    for elem in elems:
        return elem.get_attribute("content")


# publish_date
def publish():
    pub_date = "//div[@class='watch-main-col']/meta[@itemprop='datePublished']"
    elems = driver.find_elements_by_xpath(pub_date)
    for elem in elems:
        return elem.get_attribute("content")


# upload_date
def upload():
    upload_date = "//div[@class='watch-main-col']/meta[@itemprop='uploadDate']"
    elems = driver.find_elements_by_xpath(upload_date)
    for elem in elems:
        return elem.get_attribute("content")


# genre
def genre():
    genre = "//div[@class='watch-main-col']/meta[@itemprop='genre']"
    elems = driver.find_elements_by_xpath(genre)
    for elem in elems:
        return elem.get_attribute("content")


# video_width
def width():
    v_width = "//div[@class='watch-main-col']/meta[@itemprop='width']"
    elems = driver.find_elements_by_xpath(v_width)
    for elem in elems:
        return elem.get_attribute("content")


# video_height
def height():
    v_height = "//div[@class='watch-main-col']/meta[@itemprop='height']"
    elems = driver.find_elements_by_xpath(v_height)
    for elem in elems:
        return elem.get_attribute("content")


# Interaction Count
def interactions():
    interactions = "//div[@class='watch-main-col']/meta[@itemprop='interactionCount']"
    elems = driver.find_elements_by_xpath(interactions)
    for elem in elems:
        return elem.get_attribute("content")


# Video_title
def video_title():
    video_title = "//div[@class='watch-main-col']/meta[@itemprop='name']"
    elems = driver.find_elements_by_xpath(video_title)
    for elem in elems:
        return elem.get_attribute("content")


# Channel_name
def channel_name():
    channel_name = (
        "//div[@class='watch-main-col']/span[@itemprop='author']/link[@itemprop='name']"
    )
    elems = driver.find_elements_by_xpath(channel_name)
    for elem in elems:
        return elem.get_attribute("content")


# Number Likes
def likes():
    likes_xpath = "(//div[@id='top-level-buttons-computed']//*[contains(@aria-label,' likes')])[last()]"
    return driver.find_element_by_xpath(likes_xpath).text


# Total Comments
def comments():
    # Move Page to display comments
    # set scroll pause time
    SCROLL_PAUSE_TIME = 0.5

    # scroll to page bottom
    driver.execute_script("window.scrollTo(0, 1080)")

    # Wait for page load
    time.sleep(SCROLL_PAUSE_TIME)

    # scroll to page bottom
    driver.execute_script("window.scrollTo(300, 1080)")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    com = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="count"]/yt-formatted-string')
        )
    )
    return com.text


# import csv of youtube channels data
df_channels = pd.read_csv(
    "/Users/lovemachine/Downloads/- temporary/webscrape_youtube/data/data_raw/yt_channel_scrap.csv",
)

# new df of channel names and urls
df_videos = df_channels[["channel_name", "url"]].dropna()

# isolate video urls to a list
# url_list = df_videos.url.to_list()

url_list = [
    "https://www.youtube.com/watch?v=U0WkfAkSmC4",
    "https://www.youtube.com/watch?v=ugd8c6zDDQA",
    "https://www.youtube.com/watch?v=VJI88QIW7H4",
    "https://www.youtube.com/watch?v=PRVr1heimY8",
]

vid_list = []
url_fails_ls = []

count = 0

# # launch driver(s)
for url in url_list:
    driver.get(url)
    count += 1
    time.sleep(3)
    subscribe_button = '//*[@id="subscribe-button"]'
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, subscribe_button))
    )

    try:
        comments_num = comments()
        likes_num = likes()
        chan_name = channel_name()
        v_duration = duration()
        p_description = par_description()
        publish_date = publish()
        upload_date = upload()
        v_genre = genre()
        v_width = width()
        v_height = height()
        title = video_title()
        interaction_count = interactions()

    except:
        print(f"EXCEPTION RAISED for {url}")
        url_fails_ls.append(url)
        pass

    video_items = {
        "url": url,  # primary key
        "Channel Name": chan_name,
        "Title": title,
        "Duration": v_duration,
        "Partial Description": p_description,
        "Publish Date": publish_date,
        "Upload_date": upload_date,
        "Genre": v_genre,
        "Width": v_width,
        "Height": v_height,
        "Likes": likes_num,
        "Comments": comments_num,
        "Interaction Count": interaction_count,
    }

    vid_list.append(video_items)

    # print(f"url {count} of {len(url_list)} complete")
    # print every 10th url
    if count % 10 == 0:
        print(f"URL {count} of {len(url_list)} processed.")

driver.quit()

# # create dfs for video and failed urls
df_videos = pd.DataFrame(vid_list)

url_fails_dict = {"url": url_fails_ls}
df_url_fails = pd.DataFrame(url_fails_dict)

end_time = datetime.now()

print("Driver Quit")
print("Code Duration: {}".format(end_time - start_time))
print(f"Videos Processed: {len(vid_list)}")
print(f"Failures: {len(url_fails_ls)}")
print(df_videos.shape)
print(df_videos.head())


# export df to csv
df_url_fails.to_csv(
    "/Users/lovemachine/Downloads/- temporary/webscrape_youtube/data/data_raw/url_fails.csv"
)

df_videos.to_csv(
    "/Users/lovemachine/Downloads/- temporary/webscrape_youtube/data/data_raw/yt_videos_scrap.csv"
)


# ## Resources

# """
# Comments Scrapping:
# https://stackoverflow.com/questions/61410776/what-should-be-the-css-selector-to-find-count-of-comments-in-a-youtube-video-usi

# """

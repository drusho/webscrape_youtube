import pandas as pd
from requests import options
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

from uritemplate import partial

# instantiate a chrome options object so you can set the size and headless preference
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")

# Chrome driver location (for M1 macbook air)
DRIVER_PATH = "/opt/homebrew/bin/chromedriver"

# activate driver
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# launch driver
url = f"https://www.youtube.com/watch?v=UDATm1CwIR8"
driver.get(url)
time.sleep(4)


# video duration
def duration():
    duration = "//span[@class='ytp-time-duration']"
    video_time = driver.find_elements_by_xpath(duration)[0].text
    x = time.strptime(video_time, "%M:%S")
    return datetime.timedelta(minutes=x.tm_min, seconds=x.tm_sec).total_seconds()


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
# url_ad = url_address()
interaction_count = interactions()


print(
    f"""
    Channel Name: {chan_name},
    Title: {title},
    Duration: {v_duration},
    Partial Description: {p_description},
    Publish Date {publish_date},
    Upload_date: {upload_date},
    Genre: {v_genre},
    Width: {v_width},
    Height: {v_height},
    Likes: {likes_num},
    Interaction Count: {interaction_count}"""
)

driver.quit()

# import csv of youtube channels data
# df_channels = pd.read_csv(
#     "/Users/lovemachine/Downloads/- temporary/webscrape_youtube/data/data_raw/yt_channel_scrap.csv",
# )

# # new df of channel names and urls
# df_videos = df_channels[["channel_name", "url"]].dropna()

# # isolate video urls to a list
# url_list = df_videos.url.to_list()

# # loop through url list
# for url in url_list:
#     pass
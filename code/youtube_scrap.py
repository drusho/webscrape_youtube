#import libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# Chrome driver location (for M1 macbook air)
DRIVER_PATH = '/opt/homebrew/bin/chromedriver'

# activate driver
driver = webdriver.Chrome(executable_path = DRIVER_PATH)

# top youtubers based off 'https://blog.bit.ai'
top_youtubers = ['ijustine',
                 'AndroidAuthority',
                 'Mrwhosetheboss',
                 'TechnoBuffalo',
                 'TLD',
                 'duncan33303',
                 'unboxtherapy',
                 'LinusTechTips',
                 'UrAvgConsumer',
                 'mkbhd']

# empty list to hold video details
vid_list = []

# url of most videos sorted by most popular
for youtuber in top_youtubers:
    url = f'https://www.youtube.com/{youtuber}/videos?view=0&sort=p&flow=grid'

    driver.get(url)

    driver.implicitly_wait(10)
    
    # individual video info container (title, views, date, ect)
    videos = driver.find_elements_by_class_name("style-scope ytd-grid-video-renderer")

    #scroll to bottom of infinite scroll page
    for video in videos:
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        driver.implicitly_wait(10)

    # Channel Name
    try:
        channel = driver.find_element_by_xpath('//*[@id="channel-name"]').text
    except:
        channel = 'none'

    # Number of Subribers
    try:
        subscribers = driver.find_element_by_xpath('//*[@id="subscriber-count"]').text
    except:
        subscribers = 'none'

    # reassign variable to recalculate all videos
    videos = driver.find_elements_by_class_name("style-scope ytd-grid-video-renderer")

    # loop through all videos
    for video in videos:

        # grab title if available
        try:
            title = video.find_element_by_xpath('.//*[@id="video-title"]').text
        except:
            title = ''

        # grab views if available
        try:
            views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
        except:
            views = ''

        # grab post date if available
        try:
            post_date = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
        except:
            post_date = ''

        video_items = {'channel':channel,
                       'subscribers':subscribers,
                       'title':title, 'views':views,
                       'post_date':post_date}

        vid_list.append(video_items)

# # close Chrome browser
driver.quit()

# create pandas df for video info
df_vids = pd.DataFrame(vid_list)

# export df to csv
df_vids.to_csv('yt_videos.csv')

print(df_vids.shape)
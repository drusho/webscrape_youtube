#import libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# Chrome driver location (for M1 macbook air)
DRIVER_PATH = '/opt/homebrew/bin/chromedriver'

# activate driver
driver = webdriver.Chrome(executable_path = DRIVER_PATH)

# list of top tech youtubers
url = 'https://www.ranker.com/list/best-tech-channels-youtube/youtuber'
driver.get(url)

driver.implicitly_wait(10)

#profile class
p_class = "gridItem_main__1ilxA gridItem_hasMedia__38WR2 gridItem_hasRank__3kRup gridItem_bigGrid__1Camu"

profiles = driver.find_element_by_class_name(p_class)

title = '//*[@id="__next"]/article/div[3]/div[1]/ul/li[1]/div[2]/div/h2/a'

for p in profiles:

    # grab title if available
    try:
        title = p.find_element_by_xpath(title).text
    except:
        title = ''

    print(title)
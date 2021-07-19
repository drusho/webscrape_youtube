# File Descriptions



### __yt_channel_info.py__

Web Scrapping was performed using Selenium.  _Video_ and _About_ sections were scrapped for  info on both the Youtube channel and videos on each channel.

This included:
* Channel_name
* Number of Subscribers
* Video Titles
* Views for Each Video
* Video Post Date (Vague Description)
* Url for Each Video
* Channel Join Date
* Total Channel Views
* Channel Description


### __yt_video_info.py__

This file used urls scrapped in __yt_channel_info.py__ to scrap more specific details of each video this included:

* Exact date video was posted
* Hashtags associated with video
* Video length in minutes/seconds
* Number of comments per video

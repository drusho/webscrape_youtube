# Files


## yt_channel_scrap.csv
Data that was acquired from Youtube Channels' main profile.  Video and About sections were scrapped.
* Channel Name
* Number of subcribers per channel
* Most popular videos (Average of 200 per Channel is normal)
* Estimated Publish date (non specific ex. "1 month ago")
* Video urls
* Video titles
* Channel Views
* Channel Join Date
* Channel Description



## yt_video_scrap_big_data.csv
Data was acquired by visiting each url for 2000 videos that were found in __yt_channel_scrap.csv__.  Contains specific video details that couldn't be found on main Youtube Channel pages, such as:

* video length
* video size (width/height)
* number of engagements per video
* Number of Video Likes
* Number of Comments
* Upload and Publish Date (Usually its the same date)
* Genre (Most are Tech)
## url_fails.csv
urls that were not scrapped.  This list was auto populated as a failsafe to recover any missing data if needed.

[<img src="https://img.shields.io/badge/Email-%23EA4335.svg?&sflat&logo=gmail&logoColor=white" height="20" width="60" />](mailto:rraxxpl0jagb@opayq.com) &emsp;[<img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?&sflat&logo=Twitter&logoColor=white" alt="Twitter profile link button" height="20" width="70" />](https://twitter.com/drusho) &emsp; [<img src="https://img.shields.io/badge/Linkedin-%230A66C2.svg?&sflat&logo=linkedin&logoColor=white" alt="Linkedin profile link button" height="20" width="70" />](https://linkedin.com/in/davidrusho) &emsp; [<img src="https://img.shields.io/badge/Tableau-%23ff4d4d.svg?&sflat&logo=tableau&logoColor=white" alt="Tableau profile link button" height="20" width="70" >](https://public.tableau.com/app/profile/drusho) &emsp; [<img src="https://img.shields.io/badge/Github Blog-%23181717.svg?&style=flat&logo=github&logoColor=white" alt="Github profile link button" height="20" width="90" alt="Github Blog Button"/>](https://drusho.github.io/blog) 

# __Web Scrapping Popular Youtube Tech Channels with Selenium__
#### Data Mining, Data Wrangling, and Exploratory Data Analysis

<img src="https://raw.githubusercontent.com/drusho/webscrape_youtube/main/assets/header_youtube_web.png">

<br>

## About the Data

Web scraping was performed on the _Top 10 Tech Channels_ on Youtube using _[Selenium](https://selenium-python.readthedocs.io/)_ (an automated browser (driver) controlled using python, which is often used in web scraping and web testing).  Web scrapped Youtube channels were  were determined using a __[Top 10 Tech Youtubers](https://blog.bit.ai/top-tech-youtubers/)__ list from [blog.bit.ai](https://blog.bit.ai/). 

All data was saved to multiple CSV files to aid in further analyze on a Google Colab notebook.  Please see my [<img src="https://img.shields.io/badge/Github_Blog-%23ffa64d.svg?&style=flat&logo=&logoColor=" />](https://drusho.github.io/blog/selenium/web%20scrapping/pandas/youtube/python/2021/07/20/webscrapping-youtube-blog.html) for more more details.

<br>

## Sample of Data Collected

The average number of videos per channel was around 200.  In total, the data from 2000 videos was scrapped.  

##### Word Cloud of Word Frequency in Video Titles 

<img src="https://raw.githubusercontent.com/drusho/webscrape_youtube/main/reports/figures/word_frequency (wordcloud).png" width=300 height=200>
<br>
<br>

<img src="https://raw.githubusercontent.com/drusho/webscrape_youtube/main/reports/figures/word_frequency_of_video_title_(bar_plot).gif" width=400 height=220>

<br>
<br>

<img src="https://raw.githubusercontent.com/drusho/webscrape_youtube/main/reports/figures/top_video_likes_over_time_(scatter_plot).gif" width=500 height=220>
<br>
<br>





## Take Aways

  <img src="https://raw.githubusercontent.com/drusho/webscrape_youtube/main/reports/figures/correlation (dataframe).png" width=500 height=100>

1. Video Comment numbers have very little correlation to any data that was obtained in this project.
   

  

2. The following seem to be seems to be highly correlated.
   * Channel Views and Subscribers
   * Interactions and Video Views

3. Video titles fall into 5 topic groups.

    #### Kmeans and PCA used to create clusters for video titles
    
    <img src="https://raw.githubusercontent.com/drusho/webscrape_youtube/main/reports/figures/scatter.gif" width=500 height=220>

   * Iphone (kmeans 0)
   * Samsung (kmeans 1)
   * Reviews (kmeans 2)
   * Unboxing (kmeans 3)
   * How-to (kmeans 4)

4. 70% of the the most viewed videos are about phones.

   <img src="https://raw.githubusercontent.com/drusho/webscrape_youtube/main/reports/figures/top_10_youtube_videos_by_views (dataframe).png" width=500 height=220>


5. Join Date (Date a Youtube Channel was created) does not seem to have any relationship to number of subscribers or overall cha

   <img src="https://raw.githubusercontent.com/drusho/webscrape_youtube/main/reports/figures/channels_ordered_by_join_date_(dataframe).png" width=500 height=300>


<br>
<br>

## Project Links

[<img src="https://img.shields.io/badge/google%20colab-%23FFCC22.svg?&style=flat-&logo=google%20colab&logoColor=black" />  "Data Analysis of Youtube Tech Channels"](https://colab.research.google.com/drive/1UxpBBsypGqUj7816zyvGNhJcPfaxBP_c?usp=sharing)

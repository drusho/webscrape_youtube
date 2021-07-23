[<img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?&sflat&logo=Twitter&logoColor=white" alt="Twitter profile link button" height="20" width="70" />](https://twitter.com/drusho) &emsp; [<img src="https://img.shields.io/badge/Linkedin-%230A66C2.svg?&sflat&logo=linkedin&logoColor=white" alt="Linkedin profile link button" height="20" width="70" />](https://linkedin.com/in/davidrusho) &emsp; [<img src="https://img.shields.io/badge/Tableau-%23ff4d4d.svg?&sflat&logo=tableau&logoColor=white" alt="Tableau profile link button" height="20" width="70" >](https://public.tableau.com/app/profile/drusho) &emsp; [<img src="https://img.shields.io/badge/Github Blog-%23181717.svg?&style=flat&logo=github&logoColor=white" alt="Github profile link button" height="20" width="90" alt="Github Blog Button"/>](https://drusho.github.io/blog)

# __Using Selenium to Webscrape Youtube Tech Channels__

<img src="https://raw.githubusercontent.com/drusho/webscrape_youtube/main/assets/header_youtube_web.png">

<br>

## About the Data

Web scraping was performed on the _Top 10 Tech Channels_ on Youtube using _[Selenium](https://selenium-python.readthedocs.io/)_ (an automated browser (driver) controlled using python, which is often used in web scraping and web testing).  Web scrapped Youtube channels were  were determined using a __[Top 10 Tech Youtubers](https://blog.bit.ai/top-tech-youtubers/)__ list from [blog.bit.ai](https://blog.bit.ai/).  Scraping included:
* General data for each channel 
	* ex.join date, name, no. of subscribers
* Data from most popular videos per channel
	* ex. video titles, views,  	
* Data specific to each video.
	* ex. post date, no. of upvotes, no. comments. 
	

The average number of videos per channel was around 200.  In total, the data from 2000 videos was scrapped.  All data was saved to multiple CSV files to aid in further analyze on a Google Colab notebook.  Please see my [<img src="https://img.shields.io/badge/Github_Blog-%23ffa64d.svg?&style=flat&logo=&logoColor=" />](https://drusho.github.io/blog/selenium/web%20scrapping/pandas/youtube/python/2021/07/20/webscrapping-youtube-blog.html) for more more details.

<br>

## Project Links

[<img src="https://img.shields.io/badge/google%20colab-%23FFCC22.svg?&style=flat-&logo=google%20colab&logoColor=black" />  "Data Analysis of Youtube Tech Channels"](https://colab.research.google.com/drive/1UxpBBsypGqUj7816zyvGNhJcPfaxBP_c?usp=sharing)

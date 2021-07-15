# File Descriptions


## Firework Injury Data

<br>

> df_injury_clean.csv

<br>

Cleaned dataframe created from [NEISS csv files from 2016 to 2020](https://github.com/drusho/fireworks_data_exploration/tree/main/data/data_raw).  Data was merged and then combined with addtional data from the NEISS Coding Manaul to fill in coding data with descriptions to increase readability. (See sample below)

|FIELD1|Treatment_Date|Age|Sex|Alcohol|Drug|Narrative|Incident Locale|Body_Part|Diagnosis|Disposition|
|------|--------------|--------------------------------|------|-------|----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|-----------------|-------------------------------------------|-------------------------------------------------------|
|0|1/1/16|39|Male  |  |   |39YOM WAS LIGHTING BOTTLE...|Home|Eyeball|Contusions, Abrasions|Treated/Untreated and Released...|


<br>


>df_injury_clean2.csv

Same data as above except Age column has been adjusted to reflex real ages.  New column was created 'Age_Fix' to show actual ages.  'Age' column combines both coding for age groups and numeric ages of people.  'Age_Fix' columns only shows numeric ages of individuals.

<br>


>df_state_sales_clean.csv

State abbrevations have been merged with the data to assist in graphing data onto maps using Plotly.  Abbreviations were scraped from this [site](https://abbreviations.yourdictionary.com/articles/state-abbrev.html).


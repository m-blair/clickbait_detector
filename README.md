# Clickbait Detector
***
This project uses machine learning techniques to determine an article as 'clickbait' or not, based on its title. This has implications for use in spam detection, and for filtering in web scraping. 

The datasets used in training the model were obtained via Kaggle:

[Mixed Dataset](https://www.kaggle.com/datasets/amananandrai/clickbait-dataset?select=clickbait_data.csv) <br>
[News Headlines](https://www.kaggle.com/datasets/therohk/million-headlines) <br>
[5-Minute Crafts Video Titles](https://www.kaggle.com/datasets/shivamb/5minute-crafts-video-views-dataset)
<br>
# Making predictions
The user is asked to input a string (title of an article), and the model returns a value in the range (0,1), 
0 being NOT-CLICKBAIT, and 1 being CLICKBAIT. Any value >= 0.5 is interpreted as CLICKBAIT, 
where lower or higher values display the "level of certainty" of the model in it's prediction.



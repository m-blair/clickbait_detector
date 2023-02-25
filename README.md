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
where 0 denotes the class NOT-CLICKBAIT, and 1 denotes CLICKBAIT. Any value >= 0.5 is interpreted as CLICKBAIT, 
where lower or higher values can be interpretted as the model's "level of certainty" in it's prediction. 
<br>
***
**EXAMPLE INPUT**
```
15 shocking life hacks that will leave you speechless
```
<br>

**EXAMPLE OUTPUTS**
```
"15 shocking life hacks that will leave you speechless": CLICKBAIT!

[0.99999994]
```
```
"how to earn $5000 a month doing absolutely nothing": CLICKBAIT!

[0.9785793]
```
```
"President Biden visits Kiev amidst Ohio train derailment outrage": Not clickbait.

[8.869257e-06]
```
```
"How to fix Python ModuleNotFound Error": Not clickbait.

[0.01191904]
```


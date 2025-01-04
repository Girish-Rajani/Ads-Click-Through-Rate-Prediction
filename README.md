# Ads Click Through Rate Prediction

 ## Overview

The Click Through Rate (CTR) is the ratio of clicks to impressions and is an important KPI when determining the success of an ad. This Click Through Rate Prediction project analyzes the CTR to better determine the types of people most likely to click on an ad. A machine learning model (Random Forest Classifier) is also built to predict whether a user will click on an ad based on the various metrics collected such as daily time spent on the site, age, income, daily internet usage, etc., and their relationships.

 ## Exploratory Data Analysis (EDA) Performed:

 ### CTR Based on Time Spent on Site

 ![ctr_based_on_time_spent_on_site](https://github.com/user-attachments/assets/7b75a2c8-fe99-44ab-9fcc-b8b673cbaa6a)

From the above graph, we can see that the users who spend more time on the website click more on ads.

### CTR Based on Daily Internet Usage

![ctr_based_on_daily_internet_usage](https://github.com/user-attachments/assets/c9731673-fccb-48b3-a3d4-06b2ad9cf6ea)

From the above graph, we can see that users with high internet usage click less on ads than users with low internet usage.

### CTR Based on Age

![ctr_based_on_age](https://github.com/user-attachments/assets/0c7cc51a-8cb8-4367-8893-a6a78fff7729)

From the above graph, we can see that users around 40 years click more on ads compared to users around 27-36 years old.

### CTR Based on Income

![ctr_based_on_income](https://github.com/user-attachments/assets/3a3ddb92-add8-47f5-8bf2-8933d0ad272f)

There’s not much difference, but people from high-income areas click less on ads.

 ## Click Through Rate Prediction Model

 * Overall CTR was computed by dividing the number of clicks by impressions which resulted in **49.17%**
 * Daily Time Spent on Site, Age, Area Income, Daily Internet Usage and Gender were used as input features to predict Click Through Rate (CTR)
 * Split data into train and test data (80:20)
 * Used Random Forest Classifier to fit the model
 * Achieved 96% accuracy on test data

 ## Conclusion

 This project builds on the foundational work provided in The Clever Programmer's Click-Through Rate Prediction Case Study using Python by expanding the analysis to provide deeper insights into the relationship between various consumer metrics and CTR. A classification machine learning was then built to allow the prediction of CTR, achieving an accuracy of 96%.

 ## References

 1. [Click-Through Rate](https://www.masterclass.com/articles/what-is-click-through-rate)
 2. [Project Reference](https://thecleverprogrammer.com/2023/01/16/ads-click-through-rate-prediction-using-python/)
 3. [Dataset](https://www.kaggle.com/datasets/gauravduttakiit/clickthrough-rate-prediction)

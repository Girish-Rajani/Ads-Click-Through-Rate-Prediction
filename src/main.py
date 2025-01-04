#Import required libraries
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import numpy as np
pio.templates.default = "plotly_white"

#Read the dataset
data = pd.read_csv("../data/ad_10000records.csv")
print(data.head())

#Exploratory Data Analysis

#Transform Clicked-on-Ad from 0's and 1's to yes and no
data["Clicked on Ad"] = data["Clicked on Ad"].map({0: "No", 
                               1: "Yes"})

#Analyze CTR based on Time Spent on Site
fig = px.box(data, 
             x="Daily Time Spent on Site",  
             color="Clicked on Ad", 
             title="Click Through Rate based on Time Spent on Site", 
             color_discrete_map={'Yes':'blue',
                                 'No':'red'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Analyze CTR based on Daily Internet Usage
fig = px.box(data, 
             x="Daily Internet Usage",  
             color="Clicked on Ad", 
             title="Click Through Rate based on Daily Internet Usage", 
             color_discrete_map={'Yes':'blue',
                                 'No':'red'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Analyze CTR based on the age of users
fig = px.box(data, 
             x="Age",  
             color="Clicked on Ad", 
             title="Click Through Rate based on Age", 
             color_discrete_map={'Yes':'blue',
                                 'No':'red'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#fig.write_image("../output/ctr_based_on_age.png")

#Analyze CTR based on Income
fig = px.box(data, 
             x="Area Income",  
             color="Clicked on Ad", 
             title="Click Through Rate based on Income", 
             color_discrete_map={'Yes':'blue',
                                 'No':'red'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

#Compute overall Click-Through Rate of Ads

data["Clicked on Ad"].value_counts()

click_through_rate = 4917 / 10000 * 100
print('Overall CTR is ',click_through_rate,'%')

#Click Through Rate Prediction Model


data["Gender"] = data["Gender"].map({"Male": 1, 
                               "Female": 0})
#Use first 7 columns except for Ad Topic Line and City as input features
x=data.iloc[:,0:7]
x=x.drop(['Ad Topic Line','City'],axis=1)

#Use Clicked on Ad as target value
y=data.iloc[:,9]

#Split data into train and test
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,
                                           test_size=0.2,
                                           random_state=4)
#Training the model using the random forecast classification algorithm
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(x, y)

from sklearn.metrics import accuracy_score
y_pred = model.predict(xtest)
print('The Random Forest model received a test accuracy score of: ',accuracy_score(ytest,y_pred))

#Using the model to make CTR predictions based on input from user
print("Ads Click Through Rate Prediction : ")
a = float(input("Daily Time Spent on Site: "))
b = float(input("Age: "))
c = float(input("Area Income: "))
d = float(input("Daily Internet Usage: "))
e = input("Gender (Male = 1, Female = 0) : ")
features = np.array([[a, b, c, d, e]])
print("Will the user click on ad = ", model.predict(features))


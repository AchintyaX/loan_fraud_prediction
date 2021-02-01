# Load Fraud Prediction 

## Problem Statement 

The Bank Indessa has not done well in the last 3 quarters. Their NPAs (Non Performing Assets)
have reached all time high. It is starting to lose the confidence of its investors. As a result, it’s stock
has fallen by 20% in the previous quarter alone.
After careful analysis, it was found that the majority of NPA was contributed by loan defaulters. With
the messy data collected over all the years, this bank has decided to use machine learning to figure
out a way to find these defaulters and devise a plan to reduce them.
This bank uses a pool of investors to sanction their loans. For example: If any customer has applied
for a loan of $20000, along with the bank, the investors perform due diligence on the requested loan
application. Keep this in mind while understanding data.
In this challenge, you will help this bank by predicting the probability that a member will default.

## Evaluation Metric 

Submissions will be evaluated based on AUC-ROC score.

## Approach 

To tackle any Machine Learning of this type, there are a series of steps that are needed to be followed. After understanding the problem and the dataset we need to take the following procedure before jumping to using ML :

1. Data Cleaning - In this step all the null values are taken care of, by studying the features and understanding what would be the best replacement for null values. followed by converting all the features to numeric format. 

2. Feature Selection - Not all the features that are available to us are useful, some have 0 correlation with our output variable and hence are nothing but noise for the machine learning model. We need to find out the features that are impacting the output variable and only use them in the building a machine learning model. 

3. Feature Engineering - Developing cutsom features from existing features by critical thinking and domain knowledge exploration which provide a higher level understanding of the data. Feature Engineering is a time taking step and it helps in improving the performance of machine learning models drastically 


After this we build the machine learning model, by using various machine learning algorimths and comparing the performance of them to choose the best model. 
In this case we are sticking to classical machine learning techniques because they are known to perform better with Tabular Data in comparision to the hyped Deep Learning. 


## Files 
1. Data_Exploration.ipnb - Contains the code and the thought process behind it for Data Cleaning and Feature Selection 
2. Feature_Engineering.ipynb - Contains the code and the details about the custom features which were engineered 
3. test_data_processing.py - Contains Script for data cleaning of test data 
4. df_test_fe.py - Contains script for feature selection and engineering applied on test data. 
5. Model_development.ipynb - Note for experimentation with various machine learning models 
6. ML_Artivatic_dataset/submission1.csv - submission of predictions 

## Tools used 

1. Pandas 
2. Numpy
3. Matplotlib
4. xgboost
5. scikit-learn 


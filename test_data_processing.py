import pandas as pd 
import numpy as np


df_test = pd.read_csv('ML_Artivatic_dataset/test_indessa.csv')

def median_replacement(feature):
    median = feature.median(skipna=True)
    feature.fillna(median, inplace=True)
    print(feature.isna().any())
    return feature 
median_replaceable = ['annual_inc', 'mths_since_last_delinq','mths_since_last_record','open_acc','pub_rec','revol_util','total_acc','collections_12_mths_ex_med','mths_since_last_major_derog','acc_now_delinq','tot_coll_amt','tot_cur_bal','total_rev_hi_lim']

def mode_replacement(feature):
    mode = feature.mode(dropna=True)
    feature.fillna(mode[0], inplace=True)
    print(feature.isna().any())
    return feature
mode_replaceable = ['emp_length', 'delinq_2yrs', 'inq_last_6mths']

# taking care of null values
for i in median_replaceable:
    df_test[i] = median_replacement(df_test[i])

for i in mode_replaceable:
    df_test[i] = mode_replacement(df_test[i])

df_test['verification_status_joint'].fillna('Not Verified', inplace=True)

drop_cols = ['batch_enrolled', 'desc', 'title', 'emp_title']
df_test.drop(drop_cols, 1, inplace=True)

df_test.term = [int(i[:-7]) for i in df_test.term]


for i in range(len(df_test.last_week_pay)):
    if df_test.last_week_pay[i] == 'NAth week':
        df_test.last_week_pay[i] = '0th week'
df_test.last_week_pay = [int(i[:-7]) for i in df_test.last_week_pay]


df_test.to_csv('ML_Artivatic_dataset/df_test_clean.csv', index = False)
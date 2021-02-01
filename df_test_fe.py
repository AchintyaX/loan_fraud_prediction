import pandas as pd 
import numpy as np

test = pd.read_csv('ML_Artivatic_dataset/df_test_clean.csv')

test['loan_to_income'] = test['annual_inc']/test['funded_amnt_inv']

test['bad_state'] = test['acc_now_delinq'] + (test['total_rec_late_fee']/test['funded_amnt_inv']) + (test['recoveries']/test['funded_amnt_inv']) + (test['collection_recovery_fee']/test['funded_amnt_inv']) + (test['collections_12_mths_ex_med']/test['funded_amnt_inv'])


# For the sake of this model, I have used just a boolean flag if things had gone bad, with this case I didn't see
# a benifit of including above computations
test.loc[test['bad_state'] > 0, 'bad_state'] = 1

test['avl_lines'] = test['total_acc'] - test['open_acc']

test['int_paid'] = test['total_rec_int'] + test['total_rec_late_fee']

test['emi_paid_progress_perc'] = ((test['last_week_pay']/(test['term']/12*52+1))*100)

test['total_repayment_progress'] = ((test['last_week_pay']/(test['term']/12*52+1))*100) + ((test['recoveries']/test['funded_amnt_inv']) * 100)


# so the new features generated are -
features_new = ['loan_to_income', 'bad_state', 'avl_lines', 'int_paid', 'emi_paid_progress_perc','total_repayment_progress' ]

# and the features we had found useful using feature selection 
features_selected = ['revol_bal',
 'total_rev_hi_lim',
 'collection_recovery_fee',
 'delinq_2yrs',
 'revol_util',
 'pub_rec',
 'recoveries',
 'open_acc',
 'inq_last_6mths',
 'loan_amnt',
 'funded_amnt',
 'funded_amnt_inv',
 'term',
 'dti',
 'last_week_pay',
 'grade',
 'purpose',
 'home_ownership',
 'verification_status',
 'initial_list_status']

tot_features = ['member_id'] + features_selected + features_new

df = test[tot_features]
df.to_csv('ML_Artivatic_dataset/final_test.csv', index=False )
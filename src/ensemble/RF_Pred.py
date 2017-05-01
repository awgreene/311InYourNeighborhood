'''
Created on Apr 26, 2017

@author: abhijit.tomar
'''
import pandas as pd
import os
def get_col_pred(col_name):
    pred_df = pd.read_csv('resources/predictions/col_pred.csv')
    test_values = pred_df[col_name+'_orig'].values
    col_pred = pred_df[col_name+'_pred'].values
    case_id = pred_df['CASE_ENQUIRY_ID'].values
    acc=0
    jarr=[]
    for p, o, c in zip(col_pred, test_values, case_id):
        if p==o:
            acc=acc+1
        jarr.append({"CASE_ENQUIRY_ID":str(c),"Prediction":p,"Original":o})
    acc=acc/len(col_pred)
    return jarr,acc
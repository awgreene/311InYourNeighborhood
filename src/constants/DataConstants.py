'''
Created on Apr 25, 2017

@author: abhijit.tomar
'''
data_url="https://data.boston.gov/datastore/odata3.0/2968e2c0-d479-49ba-a884-4ef523ada3c0?$format=json"
train_columns=["CASE_TITLE","SUBJECT","REASON","TYPE","CASE_ENQUIRY_ID"]
pred_column="Department"
id_col='CASE_ENQUIRY_ID'
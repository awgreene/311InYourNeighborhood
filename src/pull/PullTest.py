'''
Created on Apr 25, 2017

@author: abhijit.tomar
'''
import requests,json
from pandas.io.json import json_normalize
if __name__ == '__main__':
    data_url="https://data.boston.gov/datastore/odata3.0/2968e2c0-d479-49ba-a884-4ef523ada3c0?$format=json"
    data_request = requests.get(data_url)
    data_array = json.loads(data_request.text)["value"]
    in_data_frame = json_normalize(data_array)
    print (in_data_frame)
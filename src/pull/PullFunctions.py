'''
Created on Apr 25, 2017

@author: abhijit.tomar
'''
import requests,json
from pandas.io.json import json_normalize
def pull_from_url(data_url):
    data_request = requests.get(data_url)
    data_array = json.loads(data_request.text)["value"]
    in_data_frame = json_normalize(data_array)
    return in_data_frame.shape
import requests
import json
import re
import csv
def validate_api():
    try:
        data = requests.get("https://official-joke-api.appspot.com/jokes/ten")
        new_data = data.json()
        # data_env = json.loads(new_data)
        convert_json = json.dumps(new_data)
        convert_dict = json.loads(convert_json)
        # print(type(convert_dict))
        print(convert_dict)

        col = ['type', 'setup', 'puncline', 'id']
        d = {}
        for each_dict in convert_dict:
            for key, value in each_dict.items():
                d[key] = value
                print(d)
        
    except Exception as e:
        print(e)

validate_api()
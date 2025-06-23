import requests
import json
from pprint import pprint
from fastapi import FastAPI
from fastapi.responses import JSONResponse

try:
    response = requests.get(url='https://official-joke-api.appspot.com/jokes/ten')
    #print(response._content.decode('utf-8'))
    #pprint(json.loads(response._content.decode('utf-8')))
    data_list = json.loads(response._content.decode('utf-8'))

    for i in range(len(data_list)):
        for j in range(len(data_list)-1):
            if data_list[j]['id'] > data_list[j+1]['id']:
                data_list[j]['id'], data_list[j+1]['id'] = data_list[j+1]['id'], data_list[j]['id']

    pprint(data_list)

    converted_data = str(data_list)

    file = 'data_dump.txt'

    with open('data_dump.txt','w') as f:
        f.write(converted_data)


except Exception as e:

    print(f'Encountered error {e}')

#print(json(response))

app = FastAPI()

@app.get('/')
def get_request():
    return JSONResponse(content={'data':converted_data},status_code=200)

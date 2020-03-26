# Accessing the GitHub jobs API

import requests
import json

get_another_page = True
page_num = -1
while get_another_page:
    page_num += 1
    endpoint = 'https://jobs.github.com/positions.json?description=python&location=pennsylvania&page=' + str(page_num)
    response = requests.get(endpoint)

    # Check the response code for whether the request was successful:
    status_code = response.status_code
    if status_code == 200:
        for obj in response.json():
            for key in obj:
                print(key, ': ', obj[key])
            print('--------------------------------------------------------------')
        print('----------------------- END of PAGE ------------------------')
        get_another = input('Get another page of results? y/n: ')
        if get_another == 'n':
            get_another_page = False
    else:
        print(f'HTTP request was unsuccessful. Status code: {status_code}')
        get_another_page = False

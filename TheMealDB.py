# Accessing the API of "The Meal DB"

import requests
import json

search_for = ''
while len(search_for) == 0:
    search_for = input('Enter dish to search for: ').title()

endpoint = 'https://www.themealdb.com/api/json/v1/1/search.php?s=' + search_for
response = requests.get(endpoint)

# Check the response code for whether the request was successful:
status_code = response.status_code
if status_code == 200:
    recipe_list = response.json()['meals']
    if recipe_list == None:
        print('Sorry, no results')
    else:
        for obj in recipe_list:
            for key in obj:
                if obj[key] != None and len(obj[key].strip()) > 0:
                    print(key, ': ', obj[key])
            print('--------------------------------------------------------------')
        print('----------------------- END of RESULTS ------------------------')
else:
    print(f'HTTP request was unsuccessful. Status code: {status_code}')

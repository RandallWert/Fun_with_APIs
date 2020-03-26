# Access Merriam-Webster's Collegiate Thesaurus API

import requests

look_me_up = ''
while look_me_up == '':
    look_me_up = input('Word to look up: ')

my_API_key = 'get your own API key from Merriam-Webster'
endpoint = 'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/' + look_me_up + '?key=' + my_API_key

response = requests.get(endpoint)

status_code = response.status_code
if status_code == 200:
    response_list = response.json()
    entry_num = 0
    for thes_entry_obj in response_list:
        entry_num += 1
        print(look_me_up, ': entry no. ', entry_num)
        try:
            print('Part of speech: ', thes_entry_obj['fl'])
        except:
            print('Word not found!')
            break
        else:
            print('Definition: ', thes_entry_obj['shortdef'][0])

            syn_list = thes_entry_obj['meta']['syns'][0]
            if len(syn_list) > 0:
                print('Synonyms: ')
                for syn in syn_list:
                    print(' ' * 4, syn)

            if 'rel_list' in thes_entry_obj['def'][0]['sseq'][0][0][1]:
                related_list = thes_entry_obj['def'][0]['sseq'][0][0][1]['rel_list'][0]
                if len(related_list) > 0:
                    print('Other related words: ')
                    for rw in related_list:
                        print(' ' * 4, rw['wd'])

            print('----------------------------------------')
else:
    print('Failed: ', status_code)

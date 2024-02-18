import pprint

import requests

headers = {

}
url = 'https://api.github.com/search/repostotories?q=tetris+language:assembly&sort=start&order=desc'
#token = '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'
headers = {
    'Autorization': f'tokenP{token}'
}
result = requests.get(url,headers = headers)
session = requests.session()
session.auth = ('TeNo210',token)
result = session.get(url)
#result = requests.get(url,auth=('TeNo210',token))
#url = 'https://api.github.com/search/repostotories?q=tetris+language:assembly&sort=start&order=desc'
result = session.get(url)
pprint.pprint(result.json())

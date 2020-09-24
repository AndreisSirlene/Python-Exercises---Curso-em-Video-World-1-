##Test the internet connection in Python ##

import urllib.request
try:
    web = urllib.request.urlopen("http://pudim.com.br/")
except Exception as erro:  # need to turn off wifi
    print('The website Pudim is not available!')
else: #With wifi on
    print('The server is available')
    print(web.read()) # this print allow to get all the html code of the website

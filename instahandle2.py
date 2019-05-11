#!/usr/local/bin/python3
import requests
import json
import re

base_url = 'https://www.instagram.com/'
login_url = base_url + 'accounts/login/ajax'
user_url = base_url + 'ontomeme'
username = input("Enter Username: ")
password = input("Enter Password: ")
uAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
login_data = {'username': username, 'password': password}

session = requests.Session()
session.headers = {'user-agent': uAgent}
session.headers.update({'Referer': base_url})

req = session.get(base_url)
csrf_token = re.search('(?<=\"csrf_token\":\")\w+', req.text).group(0) 
session.headers.update({'X-CSRFToken': csrf_token})

login = session.post(login_url, login_data, allow_redirects=True)
csrf_token = re.search('(?<=\"csrf_token\":\")\w+', req.text).group(0) 
session.headers.update({'X-CSRFToken': csrf_token})

cookies = login.cookies

login.encoding= login.apparent_encoding
req.encoding= req.apparent_encoding
login_text = json.dumps(login.text)
req2 = session.get(user_url)

print(login.cookies)
print(login.content)
print(req.text)
# print(req2.content)

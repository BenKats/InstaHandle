#!/usr/local/bin/python3
import requests
import json

base_url = 'https://www.instagram.com/'
login_url = base_url + 'accounts/login/ajax'
username = input("Enter Username: ")
password = input("Enter Password: ")
usr_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'

session = requests.Session()
session.headers = {'user-agent': usr_agent}
session.headers.update({'Referer': base_url})

req = session.get(base_url)
session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})
login_data = {'username': username, 'password': password}
login = session.post(login_url, data=login_data, allow_redirects=True)
session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
cookies = login.cookies
login_text = json.loads(login.text)

print(login_text)
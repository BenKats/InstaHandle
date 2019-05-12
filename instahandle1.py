#!/usr/local/bin/python3
import mechanize
from bs4 import BeautifulSoup
import requests
import json

def main():
    url = 'https://www.instagram.com/accounts/login/?force_classic_login'
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    post_params = {'username': username, 'password': password}
    browser = mechanize.Browser()
    browser.set_handle_robots(False)   
    browser.set_handle_refresh(False)  
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    response = browser.open(url)
    # # print(response.read())

    for f in br.forms():
        print("Form name:",f.name)
        print(str(f))
    br.form = list(br.forms())[0]
    print(br)

    # br.submit()
    # response = requests.post(url, data=post_params)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)

    # ses = requests.session()
    # url2 = "https://www.instagram.com/accounts/login/ajax/"
    # req = ses.post(url2, json.dumps(post_params))
    # print(req.content)

if __name__ == '__main__':
    main()
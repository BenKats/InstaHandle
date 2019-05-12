#!/usr/local/bin/python3
import mechanize
from bs4 import BeautifulSoup
import json

def main():
    base_url = 'https://www.instagram.com/'
    url = base_url + 'accounts/login/?force_classic_login'
    logout_url = base_url + 'accounts/logout'
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    post_params = {'username': username, 'password': password}

    br = mechanize.Browser()
    br.set_handle_robots(False)   # ignore robots
    br.set_handle_refresh(False)  # can sometimes hang without this
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')]


    response = br.open(url)
    # # print(response.read())

    # for f in br.forms():
    #     print("Form name:",f.name)
    #     print(str(f))

    br.form = list(br.forms())[0]
    # for control in br.form.controls:
    #     print(control)
    #     print("type=%s, name=%s value=%s" % (control.type, control.name, br[control.name]))

    br.form['username'] = username
    br.form['password'] = password
    br.submit()

    print('##################################################')
    # print(response.read())
    print('##################################################')
    resp2 = br.open(base_url + 'a' )
    print(resp2.read())

    soup = BeautifulSoup(br.response().read(), 'html.parser' )
    handle_status = soup.find('title').text.strip()
    print('\n' + handle_status)
    
    br.open(logout_url)

if __name__ == '__main__':
    main()
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
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


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
    print(response.read())
    print('##################################################')
    resp2 = br.open(base_url + username )
    print(resp2.read())
    br.open(logout_url)

if __name__ == '__main__':
    main()
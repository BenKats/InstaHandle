#!/usr/local/bin/python3
import mechanize
from bs4 import BeautifulSoup

def parse(br):
    print('#######################################################')
    print('Check to see if on challenge page or on an account ' + br.geturl())
    print('#######################################################')

    soup = BeautifulSoup(br.response().read(), 'html.parser' )
    handle_status = soup.find('title').text.strip()
    print('\n' + handle_status)
    if handle_status == 'Content Unavailable • Instagram':
        print('Reserved Username')
    elif handle_status == 'Page Not Found • Instagram':
        print('Available Username')
        print('Check to see if on challenge page or on an account ' + br.geturl())
    else:
        print('Active Username')
    

def testHandle(br, base_url):
    with open('handles.txt') as handles:
        for word in handles.readlines():
            handle = word.strip('\n')
            if len(handle) > 30:
                print('Exceeds character limit: ' + handle)
                continue
            try:
                resp2 = br.open(base_url + handle)
                # print(resp2.read())
                print('Satus of ' + handle + 'page ' + str(resp2.code))
            except mechanize.HTTPError:
                print('Failure to load: ' + br.geturl())
                print('HTTP Error: Probably 404, account doesnt exist or bot check')
            parse(br)
   
def login(br, url):
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    br.set_handle_robots(False)   
    br.set_handle_refresh(False)  
    br.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')]

    response = br.open(url)
    # print(response.read())

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

    print('Login Status: ' + str(response.code))
    print('#######################################################')

def main():
    base_url = 'https://www.instagram.com/'
    url = base_url + 'accounts/login/?force_classic_login'
    logout_url = base_url + 'accounts/logout'
    br = mechanize.Browser()
    
    login(br, url)
    testHandle(br, base_url)
    br.open(logout_url)
    br.close()

if __name__ == '__main__':
    main()
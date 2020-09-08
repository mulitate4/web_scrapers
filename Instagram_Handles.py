import webbrowser
from random import randint
from time import sleep, strftime

import pandas as pd
from selenium import webdriver


def open_pages(user):
    webbrowser.open_new_tab("instagram.com/" + user)
    sleep(1)

chromedriver_path = 'C:\\chromedriver.exe'

webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(1)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)

# enter details
username = webdriver.find_element_by_name('username')
username.send_keys('dan_guy_comics')
password = webdriver.find_element_by_name('password')
password.send_keys('navsmipiyary2@!71605')

# click login
login_button = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
login_button.click()
sleep(8)

# close notification
notnow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
notnow.click()


# edit this always
hashtag_list = ['comics', 'funnycomic']


for hashtag in hashtag_list:
    instagram_handles = []
    instagram_bios = []

    webdriver.get('https://www.instagram.com/explore/tags/' + hashtag)
    sleep(5)

    first_pic = webdriver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    first_pic.click()
    sleep(randint(1, 3))

    # get data about users
    for x in range(1, 5):
        username = webdriver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
        print(username)


        if username not in instagram_handles:
            print("username added!")
            instagram_handles.append(username)
            sleep(randint(5, 6))
        else:
            print("username already added!")
            sleep(randint(5, 6))

        webdriver.find_element_by_link_text('Next').click()
        sleep(3)

    # put data in csv format
    print(instagram_handles)
    insta_handlesdf = pd.DataFrame({'Handles': instagram_handles,})
    insta_handlesdf.to_csv(format(strftime("%Y%m%d-%H%M%S")) + hashtag + '_instagramhandles.csv')

    for handles in instagram_handles:
        open_pages(handles)
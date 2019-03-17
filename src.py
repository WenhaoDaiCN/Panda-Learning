#!/usr/bin/env python
# encoding: utf-8
# 如果觉得不错，可以推荐给你的朋友！http://tool.lu/pyc
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options
from threading import Thread
import requests
import json
import os
import re
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def info():
    print('\xe7\x86\x8a\xe7\x8c\xab\xe5\xad\xa6\xe4\xb9\xa0\xe4\xb8\x8b\xe8\xbd\xbd\xe5\x9c\xb0\xe5\x9d\x80\xe4\xb8\xba https://github.com/Alivon/Panda-Learning')
    print('\xe8\xaf\xa5\xe9\x93\xbe\xe6\x8e\xa5\xe6\x9c\x89\xe8\xaf\xa6\xe7\xbb\x86\xe4\xbd\xbf\xe7\x94\xa8\xe8\xaf\xb4\xe6\x98\x8e\xef\xbc\x8c\xe8\xbd\xac\xe5\x8f\x91\xe8\xaf\xb7\xe5\x8f\x91\xe6\xad\xa4\xe9\x93\xbe\xe6\x8e\xa5\xe7\xbb\x99\xe7\x9c\x9f\xe6\xad\xa3\xe9\x9c\x80\xe8\xa6\x81\xe4\xbd\xbf\xe7\x94\xa8\xe7\x9a\x84\xe4\xba\xba\xef\xbc\x8c\xe8\x80\x8c\xe4\xb8\x8d\xe6\x98\xaf\xe4\xbd\xbf\xe6\xad\xa4\xe6\xac\xbe\xe7\xa8\x8b\xe5\xba\x8f\xe6\xb6\x88\xe5\xa4\xb1\xe7\x9a\x84\xe4\xba\xba')


def user():
    name = input('\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d: ')
    return name


def login():
    print(datetime.now(), '\xe7\xa8\x8b\xe5\xba\x8f\xe5\xbc\x80\xe5\x90\xaf')
    driver.get('https://pc.xuexi.cn/points/login.html')
    
    try:
        remover = WebDriverWait(driver, 30, 0.2).until((lambda driver: driver.find_element_by_class_name('redflagbox')))
    except exceptions.TimeoutException:
        None
        None
        None

    driver.execute_script('arguments[0].remove()', remover)
    
    try:
        remover = WebDriverWait(driver, 30, 0.2).until((lambda driver: driver.find_element_by_class_name('header')))
    except exceptions.TimeoutException:
        None
        None
        None

    driver.execute_script('arguments[0].remove()', remover)
    
    try:
        remover = WebDriverWait(driver, 30, 0.2).until((lambda driver: driver.find_element_by_class_name('footer')))
    except exceptions.TimeoutException:
        None
        None
        None

    driver.execute_script('arguments[0].remove()', remover)
    js = 'var link = document.createElement("a");link.href="https://login.dingtalk.com/login/index.htm?goto=https%3A%2F%2Foapi.dingtalk.com%2Fconnect%2Foauth2%2Fsns_authorize%3Fappid%3Ddingoankubyrfkttorhpou%26response_type%3Dcode%26scope%3Dsnsapi_login%26redirect_uri%3Dhttps%3A%2F%2Fpc-api.xuexi.cn%2Fopen%2Fapi%2Fsns%2Fcallback";document.getElementById("app").appendChild(link);link.innerHTML="\xe9\x92\x89\xe9\x92\x89\xe8\xb4\xa6\xe5\x8f\xb7\xe7\x99\xbb\xe9\x99\x86";link.style.cssText = "display:block;margin:10px auto;font-size: 16px;background-color: #008be6;color: white;text-align: center;text-decoration: none;width:214px;height:26px;border-radius:8px;;"'
    driver.execute_script(js)
    driver.execute_script('window.scrollTo(document.body.scrollWidth/2 - 200 , 0)')
    print(datetime.now(), '\xe6\xad\xa4\xe5\x88\xbb\xe8\xaf\xb7\xe6\x89\xab\xe6\x8f\x8f\xe4\xba\x8c\xe7\xbb\xb4\xe7\xa0\x81...')
    WebDriverWait(driver, 270).until(EC.title_is('\xe6\x88\x91\xe7\x9a\x84\xe5\xad\xa6\xe4\xb9\xa0'))
    cookies = driver.get_cookies()
# WARNING: Decompyle incomplete


def readpoint(driver):
    WebDriverWait(driver, 30).until((lambda driver: driver.find_element_by_class_name('my-points-card-text')))
    points = driver.find_elements_by_class_name('my-points-card-text')
    readnum = int(points[1].text.split('/')[1][:-1]) - int(points[1].text.split('/')[0][:-1])
    videonum = int(points[2].text.split('/')[1][:-1]) - int(points[2].text.split('/')[0][:-1])
    readtime = (int(points[3].text.split('/')[1][:-1]) - int(points[3].text.split('/')[0][:-1])) * 4
    videotime = (int(points[4].text.split('/')[1][:-1]) - int(points[4].text.split('/')[0][:-1])) * 5
    print('\xe9\x98\x85\xe8\xaf\xbb\xe6\x96\x87\xe7\xab\xa0\xe5\xbe\x97\xe5\x88\x86{}\xef\xbc\x8c\xe9\x9c\x80\xe8\xa6\x81\xe5\x86\x8d\xe5\xad\xa6\xe4\xb9\xa0{}\xe7\xaf\x87\xe6\x96\x87\xe7\xab\xa0'.format(points[1].text, readnum))
    print('\xe8\xa7\x82\xe7\x9c\x8b\xe8\xa7\x86\xe9\xa2\x91\xe5\xbe\x97\xe5\x88\x86{}\xef\xbc\x8c\xe9\x9c\x80\xe8\xa6\x81\xe5\x86\x8d\xe5\xad\xa6\xe4\xb9\xa0{}\xe4\xb8\xaa\xe8\xa7\x86\xe9\xa2\x91'.format(points[2].text, videonum))
    print('\xe6\x96\x87\xe7\xab\xa0\xe5\xad\xa6\xe4\xb9\xa0\xe6\x97\xb6\xe9\x95\xbf\xe5\xbe\x97\xe5\x88\x86{}\xef\xbc\x8c\xe9\x9c\x80\xe8\xa6\x81\xe5\x86\x8d\xe5\xad\xa6\xe4\xb9\xa0{}\xe5\x88\x86\xe9\x92\x9f\xe6\x96\x87\xe7\xab\xa0'.format(points[3].text, readtime))
    print('\xe8\xa7\x86\xe9\xa2\x91\xe5\xad\xa6\xe4\xb9\xa0\xe5\xb8\x82\xe5\x9c\xba\xe5\xbe\x97\xe5\x88\x86{}\xef\xbc\x8c\xe9\x9c\x80\xe8\xa6\x81\xe5\x86\x8d\xe5\xad\xa6\xe4\xb9\xa0{}\xe5\x88\x86\xe9\x92\x9f\xe8\xa7\x86\xe9\xa2\x91'.format(points[4].text, videotime))
    return (readnum, videonum, readtime, videotime)


def check():
    driver.get('https://pc.xuexi.cn/points/my-study.html')
    print('\xe6\xad\xa3\xe5\x9c\xa8\xe6\xa0\xa1\xe9\xaa\x8c\xe7\x94\xa8\xe6\x88\xb7\xef\xbc\x8c\xe7\x8e\xb0\xe5\x9c\xa8\xe8\xaf\xb7\xe5\x8b\xbf\xe6\x89\xab\xe6\x8f\x8f\xe4\xba\x8c\xe7\xbb\xb4\xe7\xa0\x81\xe7\xad\x89\xe5\xbe\x85\xe7\xa8\x8b\xe5\xba\x8f\xe6\x8f\x90\xe7\xa4\xba\xef\xbc\x81\xef\xbc\x81\xef\xbc\x81')
    driver.delete_all_cookies()
# WARNING: Decompyle incomplete


def get_list():
    if os.path.exists('./user/{}/log.txt'.format(user_name)):
        print('\xe5\x8e\x86\xe5\x8f\xb2\xe5\xad\xa6\xe4\xb9\xa0\xe8\xae\xb0\xe5\xbd\x95\xe8\xaf\xbb\xe5\x8f\x96\xe6\x88\x90\xe5\x8a\x9f')
        print('\xe5\x90\x8e\xe5\x8f\xb0\xe5\xad\xa6\xe4\xb9\xa0\xe5\x8d\xb3\xe5\xb0\x86\xe5\xbc\x80\xe5\xa7\x8b...')
# WARNING: Decompyle incomplete


def learn_article(cookies, readnum, readtime, log, article):
    driver.quit()
    options = Options()
    options.binary_location = './chrome/chrome.exe'
    options.add_argument('blink-settings=imagesEnabled=false')
    options.add_argument('--mute-audio')
    options.add_argument('--window-size=400,500')
    options.add_argument('--headless')
    options.add_argument('--log-level=3')
    options.add_argument('--disable-logging ')
    driver_article = webdriver.Chrome('./chromedriver.exe', options, **None)
    driver_article.get('https://pc.xuexi.cn/points/my-study.html')
    driver_article.delete_all_cookies()
    for None in cookies:
        cookie = None
    
    links = []
    pattern = 'list\\"\\:(.+),\\"count\\"\\:'
    list = re.search(pattern, article)
    for i in range(log, log + readnum):
        links.append(eval(list.group(1))[i]['static_page_url'])
    
    for i in range(readnum):
        driver_article.get(links[i])
        for j in range(240):
            driver_article.execute_script('window.scrollTo(0, document.body.scrollHeight/240*{})'.format(j))
            print('\r\xe6\xad\xa3\xe5\x9c\xa8\xe5\xa4\x9a\xe7\xba\xbf\xe7\xa8\x8b\xe5\xad\xa6\xe4\xb9\xa0\xe4\xb8\xad\xef\xbc\x8c\xe6\x96\x87\xe7\xab\xa0\xe5\x89\xa9\xe4\xbd\x99{}\xe7\xa7\x92'.format(readtime - j), '', **None)
            time.sleep(1)
        
        driver_article.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        readtime -= 240
    
    driver_article.get(eval(list.group(1))[0]['static_page_url'])
    for i in range(readtime):
        time.sleep(1)
        print('\r\xe6\xad\xa3\xe5\x9c\xa8\xe5\xa4\x9a\xe7\xba\xbf\xe7\xa8\x8b\xe5\xad\xa6\xe4\xb9\xa0\xe4\xb8\xad\xef\xbc\x8c\xe6\x96\x87\xe7\xab\xa0\xe5\x89\xa9\xe4\xbd\x99{}\xe7\xa7\x92'.format(readtime - i), '', **None)
        driver_article.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    
    print('\xe6\x96\x87\xe7\xab\xa0\xe5\xad\xa6\xe4\xb9\xa0\xe5\xae\x8c\xe6\x88\x90')
    return driver_article


def learn_video(cookies, videonum, videotime, log, video):
    options = Options()
    options.binary_location = './chrome/chrome.exe'
    options.add_argument('blink-settings=imagesEnabled=false')
    options.add_argument('--mute-audio')
    options.add_argument('--window-size=400,500')
    options.add_argument('--headless')
    options.add_argument('--log-level=3')
    options.add_argument('--disable-logging ')
    driver_video = webdriver.Chrome('./chromedriver.exe', options, **None)
    driver_video.get('https://pc.xuexi.cn/points/my-study.html')
    driver_video.delete_all_cookies()
    for None in cookies:
        cookie = None
    
    pattern = 'https://www.xuexi.cn/[^,"]*html'
    link = re.findall(pattern, video, re.I)
    link.reverse()
    print('=' * 30)
    links = []
    for i in range(log, log + videonum):
        links.append(link[i])
    
    for i in range(videonum):
        driver_video.get(links[i])
        for j in range(300):
            driver_video.execute_script('window.scrollTo(0, document.body.scrollHeight/240*{})'.format(j))
            print('\r\xe6\xad\xa3\xe5\x9c\xa8\xe5\xa4\x9a\xe7\xba\xbf\xe7\xa8\x8b\xe5\xad\xa6\xe4\xb9\xa0\xe4\xb8\xad\xef\xbc\x8c\xe8\xa7\x86\xe9\xa2\x91\xe5\x89\xa9\xe4\xbd\x99{}\xe7\xa7\x92'.format(videotime - j), '', **None)
            time.sleep(1)
        
        driver_video.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        videotime -= 300
    
    driver_video.get(link[log])
    for i in range(videotime):
        time.sleep(1)
        print('\r\xe6\xad\xa3\xe5\x9c\xa8\xe5\xa4\x9a\xe7\xba\xbf\xe7\xa8\x8b\xe5\xad\xa6\xe4\xb9\xa0\xe4\xb8\xad\xef\xbc\x8c\xe8\xa7\x86\xe9\xa2\x91\xe5\x89\xa9\xe4\xbd\x99{}\xe7\xa7\x92'.format(videotime - i), '', **None)
        driver_video.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    
    print('\xe8\xa7\x86\xe9\xa2\x91\xe5\xad\xa6\xe4\xb9\xa0\xe5\xae\x8c\xe6\x88\x90')
    driver_video.quit()


def learn_main(cookies, readnum, videonum, readtime, videotime):
    (log, article, video) = get_list()
    logwrite = log + 6
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    info()
    user_name = user()
    options = Options()
    options.binary_location = './chrome/chrome.exe'
    options.add_argument('blink-settings=imagesEnabled=false')
    options.add_argument('--mute-audio')
    options.add_argument('--window-size=400,500')
    options.add_argument('--window-position=800,0')
    options.add_argument('--log-level=3')
    options.add_argument('--disable-logging ')
    driver = webdriver.Chrome('./chromedriver.exe', options, **None)
    if os.path.exists('./user/{}'.format(user_name)):
        if os.path.exists('./user/{}/cookies.txt'.format(user_name)):
            check()
        else:
            login()
    else:
        os.makedirs('./user/{}'.format(user_name))
        login()
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options
from threading import Thread
import requests
import json
import os
import re
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def info():
    print('\xe7\x86\x8a\xe7\x8c\xab\xe5\xad\xa6\xe4\xb9\xa0\xe4\xb8\x8b\xe8\xbd\xbd\xe5\x9c\xb0\xe5\x9d\x80\xe4\xb8\xba https://github.com/Alivon/Panda-Learning')
    print('\xe8\xaf\xa5\xe9\x93\xbe\xe6\x8e\xa5\xe6\x9c\x89\xe8\xaf\xa6\xe7\xbb\x86\xe4\xbd\xbf\xe7\x94\xa8\xe8\xaf\xb4\xe6\x98\x8e\xef\xbc\x8c\xe8\xbd\xac\xe5\x8f\x91\xe8\xaf\xb7\xe5\x8f\x91\xe6\xad\xa4\xe9\x93\xbe\xe6\x8e\xa5\xe7\xbb\x99\xe7\x9c\x9f\xe6\xad\xa3\xe9\x9c\x80\xe8\xa6\x81\xe4\xbd\xbf\xe7\x94\xa8\xe7\x9a\x84\xe4\xba\xba\xef\xbc\x8c\xe8\x80\x8c\xe4\xb8\x8d\xe6\x98\xaf\xe4\xbd\xbf\xe6\xad\xa4\xe6\xac\xbe\xe7\xa8\x8b\xe5\xba\x8f\xe6\xb6\x88\xe5\xa4\xb1\xe7\x9a\x84\xe4\xba\xba')


def user():
    name = input('\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d: ')
    return name


def login():
    print(datetime.now(), '\xe7\xa8\x8b\xe5\xba\x8f\xe5\xbc\x80\xe5\x90\xaf')
    driver.get('https://pc.xuexi.cn/points/login.html')
    
    try:
        remover = WebDriverWait(driver, 30, 0.2).until((lambda driver: driver.find_element_by_class_name('redflagbox')))
    except exceptions.TimeoutException:
        None
        None
        None

    driver.execute_script('arguments[0].remove()', remover)
    
    try:
        remover = WebDriverWait(driver, 30, 0.2).until((lambda driver: driver.find_element_by_class_name('header')))
    except exceptions.TimeoutException:
        None
        None
        None

    driver.execute_script('arguments[0].remove()', remover)
    
    try:
        remover = WebDriverWait(driver, 30, 0.2).until((lambda driver: driver.find_element_by_class_name('footer')))
    except exceptions.TimeoutException:
        None
        None
        None

    driver.execute_script('arguments[0].remove()', remover)
    js = 'var link = document.createElement("a");link.href="https://login.dingtalk.com/login/index.htm?goto=https%3A%2F%2Foapi.dingtalk.com%2Fconnect%2Foauth2%2Fsns_authorize%3Fappid%3Ddingoankubyrfkttorhpou%26response_type%3Dcode%26scope%3Dsnsapi_login%26redirect_uri%3Dhttps%3A%2F%2Fpc-api.xuexi.cn%2Fopen%2Fapi%2Fsns%2Fcallback";document.getElementById("app").appendChild(link);link.innerHTML="\xe9\x92\x89\xe9\x92\x89\xe8\xb4\xa6\xe5\x8f\xb7\xe7\x99\xbb\xe9\x99\x86";link.style.cssText = "display:block;margin:10px auto;font-size: 16px;background-color: #008be6;color: white;text-align: center;text-decoration: none;width:214px;height:26px;border-radius:8px;;"'
    driver.execute_script(js)
    driver.execute_script('window.scrollTo(document.body.scrollWidth/2 - 200 , 0)')
    print(datetime.now(), '\xe6\xad\xa4\xe5\x88\xbb\xe8\xaf\xb7\xe6\x89\xab\xe6\x8f\x8f\xe4\xba\x8c\xe7\xbb\xb4\xe7\xa0\x81...')
    WebDriverWait(driver, 270).until(EC.title_is('\xe6\x88\x91\xe7\x9a\x84\xe5\xad\xa6\xe4\xb9\xa0'))
    cookies = driver.get_cookies()
# WARNING: Decompyle incomplete


def readpoint(driver):
    WebDriverWait(driver, 30).until((lambda driver: driver.find_element_by_class_name('my-points-card-text')))
    points = driver.find_elements_by_class_name('my-points-card-text')
    readnum = int(points[1].text.split('/')[1][:-1]) - int(points[1].text.split('/')[0][:-1])
    videonum = int(points[2].text.split('/')[1][:-1]) - int(points[2].text.split('/')[0][:-1])
    readtime = (int(points[3].text.split('/')[1][:-1]) - int(points[3].text.split('/')[0][:-1])) * 4
    videotime = (int(points[4].text.split('/')[1][:-1]) - int(points[4].text.split('/')[0][:-1])) * 5
    print('\xe9\x98\x85\xe8\xaf\xbb\xe6\x96\x87\xe7\xab\xa0\xe5\xbe\x97\xe5\x88\x86{}\xef\xbc\x8c\xe9\x9c\x80\xe8\xa6\x81\xe5\x86\x8d\xe5\xad\xa6\xe4\xb9\xa0{}\xe7\xaf\x87\xe6\x96\x87\xe7\xab\xa0'.format(points[1].text, readnum))
    print('\xe8\xa7\x82\xe7\x9c\x8b\xe8\xa7\x86\xe9\xa2\x91\xe5\xbe\x97\xe5\x88\x86{}\xef\xbc\x8c\xe9\x9c\x80\xe8\xa6\x81\xe5\x86\x8d\xe5\xad\xa6\xe4\xb9\xa0{}\xe4\xb8\xaa\xe8\xa7\x86\xe9\xa2\x91'.format(points[2].text, videonum))
    print('\xe6\x96\x87\xe7\xab\xa0\xe5\xad\xa6\xe4\xb9\xa0\xe6\x97\xb6\xe9\x95\xbf\xe5\xbe\x97\xe5\x88\x86{}\xef\xbc\x8c\xe9\x9c\x80\xe8\xa6\x81\xe5\x86\x8d\xe5\xad\xa6\xe4\xb9\xa0{}\xe5\x88\x86\xe9\x92\x9f\xe6\x96\x87\xe7\xab\xa0'.format(points[3].text, readtime))
    print('\xe8\xa7\x86\xe9\xa2\x91\xe5\xad\xa6\xe4\xb9\xa0\xe5\xb8\x82\xe5\x9c\xba\xe5\xbe\x97\xe5\x88\x86{}\xef\xbc\x8c\xe9\x9c\x80\xe8\xa6\x81\xe5\x86\x8d\xe5\xad\xa6\xe4\xb9\xa0{}\xe5\x88\x86\xe9\x92\x9f\xe8\xa7\x86\xe9\xa2\x91'.format(points[4].text, videotime))
    return (readnum, videonum, readtime, videotime)


def check():
    driver.get('https://pc.xuexi.cn/points/my-study.html')
    print('\xe6\xad\xa3\xe5\x9c\xa8\xe6\xa0\xa1\xe9\xaa\x8c\xe7\x94\xa8\xe6\x88\xb7\xef\xbc\x8c\xe7\x8e\xb0\xe5\x9c\xa8\xe8\xaf\xb7\xe5\x8b\xbf\xe6\x89\xab\xe6\x8f\x8f\xe4\xba\x8c\xe7\xbb\xb4\xe7\xa0\x81\xe7\xad\x89\xe5\xbe\x85\xe7\xa8\x8b\xe5\xba\x8f\xe6\x8f\x90\xe7\xa4\xba\xef\xbc\x81\xef\xbc\x81\xef\xbc\x81')
    driver.delete_all_cookies()
# WARNING: Decompyle incomplete


def get_list():
    if os.path.exists('./user/{}/log.txt'.format(user_name)):
        print('\xe5\x8e\x86\xe5\x8f\xb2\xe5\xad\xa6\xe4\xb9\xa0\xe8\xae\xb0\xe5\xbd\x95\xe8\xaf\xbb\xe5\x8f\x96\xe6\x88\x90\xe5\x8a\x9f')
        print('\xe5\x90\x8e\xe5\x8f\xb0\xe5\xad\xa6\xe4\xb9\xa0\xe5\x8d\xb3\xe5\xb0\x86\xe5\xbc\x80\xe5\xa7\x8b...')
# WARNING: Decompyle incomplete


def learn_article(cookies, readnum, readtime, log, article):
    driver.quit()
    options = Options()
    options.binary_location = './chrome/chrome.exe'
    options.add_argument('blink-settings=imagesEnabled=false')
    options.add_argument('--mute-audio')
    options.add_argument('--window-size=400,500')
    options.add_argument('--headless')
    options.add_argument('--log-level=3')
    options.add_argument('--disable-logging ')
    driver_article = webdriver.Chrome('./chromedriver.exe', options, **None)
    driver_article.get('https://pc.xuexi.cn/points/my-study.html')
    driver_article.delete_all_cookies()
    for None in cookies:
        cookie = None
    
    links = []
    pattern = 'list\\"\\:(.+),\\"count\\"\\:'
    list = re.search(pattern, article)
    for i in range(log, log + readnum):
        links.append(eval(list.group(1))[i]['static_page_url'])
    
    for i in range(readnum):
        driver_article.get(links[i])
        for j in range(240):
            driver_article.execute_script('window.scrollTo(0, document.body.scrollHeight/240*{})'.format(j))
            print('\r\xe6\xad\xa3\xe5\x9c\xa8\xe5\xa4\x9a\xe7\xba\xbf\xe7\xa8\x8b\xe5\xad\xa6\xe4\xb9\xa0\xe4\xb8\xad\xef\xbc\x8c\xe6\x96\x87\xe7\xab\xa0\xe5\x89\xa9\xe4\xbd\x99{}\xe7\xa7\x92'.format(readtime - j), '', **None)
            time.sleep(1)
        
        driver_article.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        readtime -= 240
    
    driver_article.get(eval(list.group(1))[0]['static_page_url'])
    for i in range(readtime):
        time.sleep(1)
        print('\r\xe6\xad\xa3\xe5\x9c\xa8\xe5\xa4\x9a\xe7\xba\xbf\xe7\xa8\x8b\xe5\xad\xa6\xe4\xb9\xa0\xe4\xb8\xad\xef\xbc\x8c\xe6\x96\x87\xe7\xab\xa0\xe5\x89\xa9\xe4\xbd\x99{}\xe7\xa7\x92'.format(readtime - i), '', **None)
        driver_article.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    
    print('\xe6\x96\x87\xe7\xab\xa0\xe5\xad\xa6\xe4\xb9\xa0\xe5\xae\x8c\xe6\x88\x90')
    return driver_article


def learn_video(cookies, videonum, videotime, log, video):
    options = Options()
    options.binary_location = './chrome/chrome.exe'
    options.add_argument('blink-settings=imagesEnabled=false')
    options.add_argument('--mute-audio')
    options.add_argument('--window-size=400,500')
    options.add_argument('--headless')
    options.add_argument('--log-level=3')
    options.add_argument('--disable-logging ')
    driver_video = webdriver.Chrome('./chromedriver.exe', options, **None)
    driver_video.get('https://pc.xuexi.cn/points/my-study.html')
    driver_video.delete_all_cookies()
    for None in cookies:
        cookie = None
    
    pattern = 'https://www.xuexi.cn/[^,"]*html'
    link = re.findall(pattern, video, re.I)
    link.reverse()
    print('=' * 30)
    links = []
    for i in range(log, log + videonum):
        links.append(link[i])
    
    for i in range(videonum):
        driver_video.get(links[i])
        for j in range(300):
            driver_video.execute_script('window.scrollTo(0, document.body.scrollHeight/240*{})'.format(j))
            print('\r\xe6\xad\xa3\xe5\x9c\xa8\xe5\xa4\x9a\xe7\xba\xbf\xe7\xa8\x8b\xe5\xad\xa6\xe4\xb9\xa0\xe4\xb8\xad\xef\xbc\x8c\xe8\xa7\x86\xe9\xa2\x91\xe5\x89\xa9\xe4\xbd\x99{}\xe7\xa7\x92'.format(videotime - j), '', **None)
            time.sleep(1)
        
        driver_video.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        videotime -= 300
    
    driver_video.get(link[log])
    for i in range(videotime):
        time.sleep(1)
        print('\r\xe6\xad\xa3\xe5\x9c\xa8\xe5\xa4\x9a\xe7\xba\xbf\xe7\xa8\x8b\xe5\xad\xa6\xe4\xb9\xa0\xe4\xb8\xad\xef\xbc\x8c\xe8\xa7\x86\xe9\xa2\x91\xe5\x89\xa9\xe4\xbd\x99{}\xe7\xa7\x92'.format(videotime - i), '', **None)
        driver_video.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    
    print('\xe8\xa7\x86\xe9\xa2\x91\xe5\xad\xa6\xe4\xb9\xa0\xe5\xae\x8c\xe6\x88\x90')
    driver_video.quit()


def learn_main(cookies, readnum, videonum, readtime, videotime):
    (log, article, video) = get_list()
    logwrite = log + 6
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    info()
    user_name = user()
    options = Options()
    options.binary_location = './chrome/chrome.exe'
    options.add_argument('blink-settings=imagesEnabled=false')
    options.add_argument('--mute-audio')
    options.add_argument('--window-size=400,500')
    options.add_argument('--window-position=800,0')
    options.add_argument('--log-level=3')
    options.add_argument('--disable-logging ')
    driver = webdriver.Chrome('./chromedriver.exe', options, **None)
    if os.path.exists('./user/{}'.format(user_name)):
        if os.path.exists('./user/{}/cookies.txt'.format(user_name)):
            check()
        else:
            login()
    else:
        os.makedirs('./user/{}'.format(user_name))
        login()

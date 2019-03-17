# coding=utf-8
import time
from datetime import datetime
from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options
from threading import Thread
import requests
import json
import os
import re

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 警告等级


def info():
    print("熊猫学习下载地址为 https://github.com/Alivon/Panda-Learning")
    print("该链接有详细使用说明，转发请发此链接给真正需要使用的人，而不是使此款程序消失的人")


def user():
    name = input("请输入用户名: ")
    return name


def login():
    print(datetime.now(), "程序开启")
    driver.get("https://pc.xuexi.cn/points/login.html")
    try:
        remover = WebDriverWait(driver, 30, 0.2).until(lambda driver: driver.find_element_by_class_name("redflagbox"))
    except exceptions.TimeoutException:
        pass
    else:
        driver.execute_script('arguments[0].remove()', remover)
    try:
        remover = WebDriverWait(driver, 30, 0.2).until(lambda driver: driver.find_element_by_class_name("header"))
    except exceptions.TimeoutException:
        pass
    else:
        driver.execute_script('arguments[0].remove()', remover)
    try:
        remover = WebDriverWait(driver, 30, 0.2).until(lambda driver: driver.find_element_by_class_name("footer"))
    except exceptions.TimeoutException:
        pass
    else:
        driver.execute_script('arguments[0].remove()', remover)
        js = 'var link = document.createElement("a");' \
             'link.href="https://login.dingtalk.com/login/index.htm?goto=https%3A%2F%2Foapi.dingtalk.com%2Fconnect%2Foauth2%2Fsns_authorize%3Fappid%3Ddingoankubyrfkttorhpou%26response_type%3Dcode%26scope%3Dsnsapi_login%26redirect_uri%3Dhttps%3A%2F%2Fpc-api.xuexi.cn%2Fopen%2Fapi%2Fsns%2Fcallback";' \
             'document.getElementById("app").appendChild(link);' \
             'link.innerHTML="钉钉账号登陆";' \
             'link.style.cssText = "display:block;margin:10px auto;font-size: 16px;background-color: #008be6;color: white;text-align: center;text-decoration: none;width:214px;height:26px;border-radius:8px;;"'
        driver.execute_script(js)

        driver.execute_script('window.scrollTo(document.body.scrollWidth/2 - 200 , 0)')
    print(datetime.now(), "此刻请扫描二维码...")

    WebDriverWait(driver, 270).until(EC.title_is(u"我的学习"))
    cookies = driver.get_cookies()
    with open("./user/{}/cookies.txt".format(user_name), "w") as fp:
        json.dump(cookies, fp)

    check()


def readpoint(driver):
    WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_class_name("my-points-card-text"))
    points = driver.find_elements_by_class_name("my-points-card-text")
    readnum = int(points[1].text.split("/")[1][:-1]) - int(points[1].text.split("/")[0][:-1])
    videonum = int(points[2].text.split("/")[1][:-1]) - int(points[2].text.split("/")[0][:-1])
    readtime = (int(points[3].text.split("/")[1][:-1]) - int(points[3].text.split("/")[0][:-1])) * 4
    videotime = (int(points[4].text.split("/")[1][:-1]) - int(points[4].text.split("/")[0][:-1])) * 5
    print("阅读文章得分{}，需要再学习{}篇文章".format(points[1].text, readnum))
    print("观看视频得分{}，需要再学习{}个视频".format(points[2].text, videonum))
    print("文章学习时长得分{}，需要再学习{}分钟文章".format(points[3].text, readtime))
    print("视频学习市场得分{}，需要再学习{}分钟视频".format(points[4].text, videotime))
    return readnum, videonum, readtime, videotime


def check():
    driver.get("https://pc.xuexi.cn/points/my-study.html")  # 读取上下文
    print("正在校验用户，现在请勿扫描二维码等待程序提示！！！")
    driver.delete_all_cookies()  # 删除未登陆cookie
    with open("./user/{}/cookies.txt".format(user_name), "r") as file:
        cookies = json.load(file)

    for cookie in cookies:  # 添加cookies
        driver.add_cookie({k: cookie[k] for k in {'name', 'value', 'domain', 'path', 'expiry'}})

    driver.get("https://pc.xuexi.cn/points/my-points.html")
    WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_class_name("footer"))

    if EC.title_is("我的积分"):
        try:
            print("正在校验用户，现在请勿扫描二维码等待程序提示！！！")
            print("正在校验用户[{}]学习数据记录，若上次使用本程序超过6小时没有登陆，请等待10秒后程序提手扫描再扫描二维码".format(user_name))
            WebDriverWait(driver, 10).until(
                lambda driver: driver.find_element_by_class_name("my-points-card-subtitle-once-value"))
            print("登陆成功，即将开始自动学习")
            readnum, videonum, readtime, videotime = readpoint(driver)
            learn_main(cookies, readnum, videonum, readtime, videotime)
        except exceptions.TimeoutException:
            print("服务器登陆状态失效，请重新登陆")
            login()
    else:
        print("服务器登陆状态失效，请重新登陆")
        login()


def get_list():
    if os.path.exists("./user/{}/log.txt".format(user_name)):
        print("历史学习记录读取成功")
        print("后台学习即将开始...")
    else:
        with open("./user/{}/log.txt".format(user_name), "w", encoding="utf8")as fp:
            fp.write("0")
        get_list()
    with open("./user/{}/log.txt".format(user_name), "r", encoding="utf8") as fp:
        log = int(fp.read())
    article = requests.get(
        "https://www.xuexi.cn/c06bf4acc7eef6ef0a560328938b5771/data9a3668c13f6e303932b5e0e100fc248b.js").content.decode(
        "utf8")
    video = requests.get(
        "https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/datadb086044562a57b441c24f2af1c8e101.js").content.decode(
        "utf8")
    return log, article, video


def learn_article(cookies, readnum, readtime, log, article):
    driver.quit()
    options = Options()
    options.binary_location = "./chrome/chrome.exe"
    options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    options.add_argument('--mute-audio')  # 关闭声音
    options.add_argument('--window-size=400,500')
    options.add_argument('--headless')
    driver_article = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)  # 实例化chrome

    driver_article.get("https://pc.xuexi.cn/points/my-study.html")  # 读取上下文
    driver_article.delete_all_cookies()  # 删除未登陆cookie
    for cookie in cookies:  # 添加cookies
        driver_article.add_cookie({k: cookie[k] for k in {'name', 'value', 'domain', 'path', 'expiry'}})

    links = []
    pattern = r"list\"\:(.+),\"count\"\:"
    list = re.search(pattern, article)
    for i in range(log, log + readnum):
        links.append(eval(list.group(1))[i]["static_page_url"])
    for i in range(readnum):
        driver_article.get(links[i])
        for j in range(4 * 60):
            driver_article.execute_script(
                'window.scrollTo(0, document.body.scrollHeight/240*{})'.format(j))
            print("\r正在多线程学习中，文章剩余{}秒".format(readtime - j), end="")
            time.sleep(1)
        driver_article.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        readtime -= 4 * 60
    driver_article.get(eval(list.group(1))[0]["static_page_url"])
    for i in range(readtime):
        time.sleep(1)
        print("\r正在多线程学习中，文章剩余{}秒".format(readtime - i), end="")
        driver_article.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    print("文章学习完成")
    return driver_article


def learn_video(cookies, videonum, videotime, log, video):
    options = Options()
    options.binary_location = "./chrome/chrome.exe"
    options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    options.add_argument('--mute-audio')  # 关闭声音
    options.add_argument('--window-size=400,500')
    options.add_argument('--headless')
    driver_video = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)  # 实例化chrome
    driver_video.get("https://pc.xuexi.cn/points/my-study.html")  # 读取上下文
    driver_video.delete_all_cookies()  # 删除未登陆cookie
    for cookie in cookies:  # 添加cookies
        driver_video.add_cookie({k: cookie[k] for k in {'name', 'value', 'domain', 'path', 'expiry'}})
    pattern = r'https://www.xuexi.cn/[^,"]*html'
    link = re.findall(pattern, video, re.I)
    link.reverse()
    print("=" * 30)
    links = []
    for i in range(log, log + videonum):
        links.append(link[i])
    for i in range(videonum):
        driver_video.get(links[i])
        for j in range(5 * 60):
            driver_video.execute_script(
                'window.scrollTo(0, document.body.scrollHeight/240*{})'.format(j))
            print("\r正在多线程学习中，视频剩余{}秒".format(videotime - j), end="")
            time.sleep(1)
        driver_video.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        videotime -= 5 * 60
    driver_video.get(link[log])
    for i in range(videotime):
        time.sleep(1)
        print("\r正在多线程学习中，视频剩余{}秒".format(videotime - i), end="")
        driver_video.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    print("视频学习完成")
    driver_video.quit()


def learn_main(cookies, readnum, videonum, readtime, videotime):
    log, article, video = get_list()
    logwrite = log + 6
    with open("./user/{}/log.txt".format(user_name), "w", encoding="utf8")as fp:
        json.dump(logwrite, fp)
    hour_now = datetime.now().hour
    print(datetime.now())
    if hour_now in [6, 7, 8, 12, 13, 20, 21, 22]:
        print("现在为活跃时间，学习效率加倍")
        readnum //= 2
        videonum //= 2
        readtime //= 2
        videotime //= 2
    else:
        print("非活跃时间")
    t2 = Thread(target=learn_video, args=(cookies, videonum, videotime * 60, log, video))
    t2.start()
    driver_article = learn_article(cookies, readnum, readtime * 60, log, article)
    t2.join()
    print("学习完毕")

    driver_article.get("https://pc.xuexi.cn/points/my-points.html")
    print("学习完毕，学习情况如下，30分钟后程序自动关闭")
    readpoint(driver_article)
    driver_article.quit()
    time.sleep(60 * 30)


if __name__ == '__main__':
    info()
    user_name = user()
    # desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
    # desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
    options = Options()
    options.binary_location = "./chrome/chrome.exe"
    options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    options.add_argument('--mute-audio')  # 关闭声音
    options.add_argument('--window-size=400,500')
    options.add_argument('--window-position=800,0')
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)  # 实例化chrome
    if os.path.exists("./user/{}".format(user_name)):
        pass
        if os.path.exists("./user/{}/cookies.txt".format(user_name)):
            check()
        else:
            login()
    else:
        os.makedirs("./user/{}".format(user_name))
        login()

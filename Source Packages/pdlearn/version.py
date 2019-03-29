import requests


def up_info():
    print("正在联网获取跟新信息...")
    __Version = "v2.1 preview"
    __INFO = "熊猫学习唯一下载地址为 https://github.com/Alivon/Panda-Learning"
    try:
        updata_log = requests.get(
        "https://raw.githubusercontent.com/Alivon/Panda-Learning/master/Update%20log").content.decode(
        "utf8")
        updata_log = updata_log.split("\n")
        print(__INFO)
        print("程序版本为：{}，\n最新版本为：{}".format(__Version, updata_log[1].split("=")[1]), end=" ")
        print("主要更新说明：{}".format(updata_log[2]))
        print("更新显示不会打断之前操作，请继续...")
    except:
        print("网络错误")


if __name__ == '__main__':
    up_info()

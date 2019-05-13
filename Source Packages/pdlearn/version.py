import requests


def up_info():
    print("\n正在联网获取更新信息...")
    __Version = "v2.5"
    __INFO = "熊猫学习唯一下载地址为 https://github.com/Alivon/Panda-Learning"
    try:
        updata_log = requests.get(
        "https://raw.githubusercontent.com/Alivon/Panda-Learning/master/Update%20log").content.decode(
        "utf8")
        updata_log = updata_log.split("\n")
        print(__INFO)
        print("程序版本为：{}，\n最新版本为：{}".format(__Version, updata_log[1].split("=")[1]))
        print("="*120)
        if __Version != updata_log[1].split("=")[1]:
            print("当前不是最新版本，建议更新")
            print("=" * 120)
            print("更新提要：")
            for i in updata_log[2:]:
                print(i)
        print("=" * 120)
        print("更新显示不会打断之前输入等操作，请继续......（若已输入用户标记直接enter）")
    except:
        print("版本信息网络错误")


if __name__ == '__main__':
    up_info()

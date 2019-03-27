from datetime import datetime


def is_active():
    isac = False
    hour_now = datetime.now().hour
    if hour_now in [6, 7, 12, 13, 20, 21]:
        isac = True
        print("当前为活跃时间，双倍暴击")
    return isac

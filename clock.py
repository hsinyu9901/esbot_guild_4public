import urllib
import urllib.request
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

# 星期一到星期日的時候，每隔 20 分鐘就呼喊一次


@sched.scheduled_job('cron', day_of_week='mon-sun', minute='*/20')
def scheduled_job():
    url = "https://escooter-esbot.herokuapp.com/"
    conn = urllib.request.urlopen(url)

    for key, value in conn.getheaders():
        print(key, value)


sched.start()

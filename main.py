import pandas as pd
import datetime
import os
import requests

def send_notification(event, note):
    # 这里以 Server酱 (微信提醒) 为例，你也可以换成邮件或 Telegram
    sct_key = os.getenv('SCT_KEY')
    if sct_key:
        title = f"⏰ 提醒：{event}"
        desp = f"内容：{note}\n时间：{datetime.date.today()}"
        url = f"https://sctapi.ftqq.com/{sct_key}.send?title={title}&desp={desp}"
        requests.get(url)
        print(f"已发送提醒: {event}")

# 获取今天日期 (格式: MM-DD)
today = datetime.datetime.now().strftime('%m-%d')

# 读取提醒列表
df = pd.read_csv('reminders.csv')

# 检查是否有今天的任务
for index, row in df.iterrows():
    if row['date'] == today:
        send_notification(row['event'], row['note'])
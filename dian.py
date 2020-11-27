# coding=utf-8
# author:@Roywaller

import http.client
import pandas as pd
import requests
import time
import datetime
import pytz

tz = pytz.timezone('Asia/Shanghai') #东八区
t = datetime.datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')

conn = http.client.HTTPConnection("beijingxuanlifang.qdxyjt.com")

payload = "__EVENTVALIDATION=hZPBwmXtHS2S8lZAmrrXKCmh13w9wYS4xUR3OBIO6uwvx6%2F95lnoau0W2YK49cnfopuoDfBCIItH4Cbo6evqJqxNZMmzxkbcsvKZfnqg1pf0Drr7aTAw5A9RAH5oZ%2FevQc6lFWnSxeS98QKkd315hKzAgfG82yJt6DQGkmUhBdRv59uuWZqEDE2xAYxSe8MFx5rmOFaPVFJOE0DzCvSxC1FPQ6bxDgFDFVYD8MZYJ6A%3D&__VIEWSTATE=hx5eHPrpntbteJVuRyNsCWl2H5Yl20MK%2BNhMbWcxe6y1SVBkNbTEIgcH7PCWnsBJBJWeXGHmGlkeyRwoK8DZpHQRToj9KhszPLHXmBkjH2Jy4J2HHbX%2BrCGChlF6uF6eycab%2FF5k0xJwDX2BXHdp0CLMOQiGi%2F1FZtDPJUN5AJALTIvmFU0wI5oX6U4DiCGAjcgKG6%2BK%2FPj%2F6lXFIeEQWEy7ttLZJE%2FFkXb6iOGHBCdtNxcGiRJMsuzQLV1Zu7cOPe4vO7y3C0e7VK5ruyfa8oVsNg%2BWyhbwydXS7kGupx9dRodGl3Us75E%2FkP3XJiDYzirsmD52s3b6UgrwphDIlYroCh9Awe1LJvZi3HJg7vhAWYgTU84511g1nHh0GUL2mRsykjffWrPGB03rhHvdtsQnumML3eROV7wf6ACYm4g45meUyiYumTOv9%2F69om429NmC4Dq7kPngbs3AawNUl20uW5qdZQXfkCNDGObr6RnTj8PSKHQciQNX2Zgqet5S3JYZHeHYBRXVhV0vepJBNB%2BgFGU52Yg70nz9dybI%2B6NE1fdjmLVB1%2BHPmBxwuJkEqPfnzffqfpBaZuErYpJeGg5JRK9GDn2a1UE%2BOUzPEvMaJmT46q%2FTIhCyhYt29UZHucFIoXf9XUWHSFQYfO3CTD0BUx%2BWzHT%2BfMSZR26dG8YqKDHRG1V1Ci9nLsRXfs2k9mBjYvmRHpnlhkBLg4qTWI187Y0M70CFQvE4AgaXIhBijCziWQ%2F7ltSapv2K26056Do1%2Bo2o7GQuNqyeMtwpC62wJvKhywubqOAnTWVmvWHeX8%2BWowXUIs3o246Ekq2rFB2ezaLb4N7xYuFGD5GjHvki6KSJSCCNN%2F0YiYh2xUGUO5DR7r5fo%2BHKWpEvs1nPzCoDC7g3HFyLS%2B%2FfhGxzq4WjH5EV7Wy8kfL%2FvXV2NM%2FJQgxoVRlSCM5%2BE7iYPbJk&__VIEWSTATEGENERATOR=CA0B0334&chaxun=%E6%9F%A5%E8%AF%A2&lou=1%E5%8F%B7%E6%A5%BC&yonghu=0005020027"

headers = {
    'upgrade-insecure-requests': "1",

    'dnt': "1",

    'content-type': "application/x-www-form-urlencoded",

    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",

    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

    'client-ip': "127.0.0.1",

    'true-client-ip': "127.0.0.1",

    'x-client-ip': "127.0.0.1",

    'x-forwarded-for': "127.0.0.1",

    'x-real-ip': "127.0.0.1",

    'x-remote-ip': "127.0.0.1",

    'x-remote-addr': "127.0.0.1",

    'cache-control': "no-cache"
    }

conn.request("POST", "/Default.aspx", payload, headers)

res = conn.getresponse()

data = res.read()

tables = pd.read_html(data.decode("utf-8"))

df = tables[1]

out=df[2][0],':',df[3][0],'\n\n',df[0][0],':',df[1][0],'\n\n',df[0][1],':',df[1][1],'\n\n',df[2][1],':',df[3][1],'\n\n',df[0][4],':',df[1][4]

out1=''.join(out)

RoomNum=''.join(df[3][0])

SysNum=''.join(df[1][0])

TotNum=''.join(df[1][1])

LeftNum=''.join(df[3][1])

LastDate=''.join(df[1][4])

result_list = [[RoomNum,SysNum,TotNum,LeftNum,LastDate,t]]

columns = ["房间号", "系统编号", "表字", "购电剩余", "上次通讯时间","记录时间"]

dt = pd.DataFrame(result_list, columns=columns)

dt.to_csv("Records.csv",header=None, index=0, encoding='utf_8_sig', mode='a')

#api = "https://sc.ftqq.com/SCU3867T339ca212371e4f0e4d1273832086e69b582bfec6dd91b.send"

#title = u"电量通知"

#content = ""+out1+""

#data = {
#   "text":title,
#   "desp":content
#}

#req = requests.post(api,data = data)

with open("README.md","a") as f:
        f.write(str(result_list) + '  ')

# coding=utf-8
# author:@Roywaller

import http.client
import pandas as pd
import requests
import time
import datetime
import pytz

tz = pytz.timezone('Asia/Shanghai')  # 东八区
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

# out=df[2][0],':',df[3][0],'\n\n',df[0][0],':',df[1][0],'\n\n',df[0][1],':',df[1][1],'\n\n',df[2][1],':',df[3][1],'\n\n',df[0][4],':',df[1][4],'\n\n',"https://roywaller.github.io/XLFElectricity-Inquiry/Records.html"

# out1=''.join(out)

RoomNum = ''.join(df[3][0])

SysNum = ''.join(df[1][0])

TotNum = ''.join(df[1][1])

LeftNum = ''.join(df[3][1])

LastDate = ''.join(df[1][4])

LastUsed = pd.read_csv("Records.csv").iloc[-1]["表字"]

Used = str(round(float(TotNum) - float(LastUsed), 3))
print(Used)
print(type(Used))

result_list = [[RoomNum, SysNum, TotNum, Used, LeftNum, LastDate, t]]

columns = ["房间号", "系统编号", "表字", "当前已用", "购电剩余", "上次通讯时间", "记录时间"]

dt = pd.DataFrame(result_list, columns=columns)

lastimeres = pd.read_csv("Records.csv").iloc[-1]["上次通讯时间"]
#content = "房间号:" + RoomNum + "\n\n系统编号:" + SysNum + "\n\n表字:" + TotNum + "\n\n当前已用:" + str(
#    Used) + "\n\n购电剩余:" + LeftNum + "\n\n上次通讯时间:" + LastDate + "\n\n https://roywaller.github.io/XLFElectricity-Inquiry/Records.html"

if LastDate != lastimeres:
    dt.to_csv("Records.csv", header=None, index=0, encoding='utf_8_sig', mode='a')
    csv = pd.read_csv("Records.csv")

    used = csv["当前已用"].values.tolist()
    lastime = csv["上次通讯时间"].values.tolist()

    GEN_HTML = "Records.html"  # 命名生成的html

    str_1 = lastime
    str_2 = used

    f = open(GEN_HTML, 'w')
    message = """
	<!DOCTYPE html>

    <html style="height: 100%%">

    <head>

    <meta charset="utf-8">

    </head>

    <body style="height: 100%%; margin: 0">

    <div id="container" style="height: 100%%"></div>



    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>

    <!-- Uncomment this line if you want to dataTool extension

    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts@5/dist/extension/dataTool.min.js"></script>

    -->

    <!-- Uncomment this line if you want to use gl extension

    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts-gl@2.0.0-rc.1/dist/echarts-gl.min.js"></script>

    -->

    <!-- Uncomment this line if you want to echarts-stat extension

    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts-stat@latest/dist/ecStat.min.js"></script>

    -->

    <!-- Uncomment this line if you want to use map

    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts@5/map/js/china.js"></script>

    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts@5/map/js/world.js"></script>

    -->

    <!-- Uncomment these two lines if you want to use bmap extension

    <script type="text/javascript" src="https://api.map.baidu.com/api?v=2.0&ak=<Your Key Here>"></script>

    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts@5/dist/extension/bmap.min.js"></script>

    -->



    <script type="text/javascript">

    var dom = document.getElementById("container");

    var myChart = echarts.init(dom);

    var app = {};



    var option;

    option = {

    title: {

    text: '用电分布记录',

    subtext: ''

    },

    tooltip: {

    trigger: 'axis',

    axisPointer: {

    type: 'cross'

    }

    },

    toolbox: {

    show: true,

    feature: {

    dataZoom: {

    yAxisIndex: 'none'

    },

    dataView: {readOnly: false},

    magicType: {type: ['line', 'bar']},

    restore: {},

    saveAsImage: {}

    }

    },

    xAxis: {

    type: 'category',

    boundaryGap: false,

    axisLabel: {

    //rotate:45,

    interval:3,

    formatter:function(val){

        var strs = val.split(''); //字符串数组

        var str = ''

        for(var i = 0, s; s = strs[i++];) { //遍历字符串数组

        str += s;

        if(!(i %% 10)) str += '\\n'; //按需要求余

    }

    return str

    }},

    data: %s

    },

    yAxis: {

    type: 'value',

    axisLabel: {

    formatter: '{value} kW·h'

    },

    axisPointer: {

    snap: true

    }

    },

    series: [

    {

    name: '时段用电量',

    type: 'line',

    smooth: true,

    itemStyle : { normal: {label : {show: true}}},

    data: %s,

    }

    ]

    };



    if (option && typeof option === 'object') {

    myChart.setOption(option);

    }

    window.onresize = myChart.resize;



    </script>

    </body>

    </html>""" % (str_1, str_2)
    f.write(message)
    f.close()
else:
    print("数据未更新")

conn = http.client.HTTPConnection("wmwechat.hownewiot.com")

headers = {
    'dnt': "1",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'client-ip': "127.0.0.1",
    'true-client-ip': "127.0.0.1",
    'x-client-ip': "127.0.0.1",
    'x-forwarded-for': "127.0.0.1",
    'x-real-ip': "127.0.0.1",
    'x-remote-ip': "127.0.0.1",
    'x-remote-addr': "127.0.0.1",
    'cache-control': "no-cache",
    'postman-token': "25c5aab5-5328-1f3a-1bdc-b65395806b8e"
}

conn.request("GET", "/bj002/weixin/comm/waterUseFeeInfo.do?weChatNo=oYBnwvxMuMxlcQEw9Fvyqo0Sgya4", headers=headers)
res = conn.getresponse()
data = res.read()

tables = pd.read_html(data.decode("utf-8"))
df = tables[0]
setime = df['结算时间'][0]
sewatervol = df['结算水量(m³)'][0]
sewaterfee = df['结算水费'][0]
balance = df['剩余金额'][0]
cumread = df['累计读数(m³)'][0]
result_list = [[setime, sewatervol, sewaterfee, balance, cumread]]
columns = ["结算时间", "结算水量(m³)", "结算水费", "剩余金额", "累计读数(m³)"]
dt = pd.DataFrame(result_list, columns=columns)
lastimeres = pd.read_csv("water.csv").iloc[-1]["结算时间"]
if setime != lastimeres:
    print(result_list)
    dt.to_csv("water.csv", header=None, index=0, encoding='utf_8_sig', mode='a')
    csv = pd.read_csv("water.csv")
else:
    print("数据未更新")

content = "用电情况\n\n房间号:" + RoomNum + "\n\n系统编号:" + SysNum + "\n\n累计表字:" + TotNum + "\n\n当前已用:" + TotNum + \
          "\n\n购电剩余:" + LeftNum + "\n\n上次通讯时间:" + LastDate + "\n\n https://roywaller.github.io/XLFElectricity-Inquiry/Records.html" + \
          "\n\n\n\n用水情况\n\n结算时间：" + setime + "\n\n累计读数：" + cumread + "\n\n结算水量：" + sewatervol + "\n\n剩余金额：" + balance

api = "https://sctapi.ftqq.com/SCT62936TXA1lLED0i5z9u5qmYceyWavU.send"
title = u"购电剩余：" + LeftNum + u"购水剩余：" + balance
data = {
    "text": title,
    "desp": content
}
req = requests.post(api, data=data)

### XLFElectricity Inquiry

#炫立方用电量查询

#[查看图表](https://roywaller.github.io/XLFElectricity-Inquiry/Records.html)

   #更新日志

      #2020-11-27 V1.0 测试
      #2020-12-03 V1.1 根据[上次通讯时间]判断数据是否更新，如果数据没有更新则不记录内容

   #TODO

      #判断当天是否当月最后一天，如果是写CSV和HTML并在上月CSV中统计用电总量
      
	  ```python
	  #!/usr/bin/env python3
	  # coding: utf-8
	  
	  import datetime
	  
	  def last_day_of_month(any_day):
	      """
	      获取获得一个月中的最后一天
	      :param any_day: 任意日期
	      :return: string
	      """
	      next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
	      return next_month - datetime.timedelta(days=next_month.day)
	  
	  
	  # 当前日期
	  now = datetime.datetime.now().date()
	  year,month,day = str(now).split("-")  # 切割
	  # 年月日，转换为数字
	  year = int(year)
	  month = int(month)
	  day = int(day)
	  
	  # 获取这个月最后一天
	  last_day = last_day_of_month(datetime.date(year, month, day))
	  
	  # 判断当前日期是否为月末
	  if str(now) == last_day:
	      print('yes')
	  else:
	      print('no')
	  ```

  #免责申明

    该项目仅供学习使用，严禁用于商业用途，由此造成的一切后果，本人概不负责。

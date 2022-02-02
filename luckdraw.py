start_time = "2019-08-05 01:00:00" # 自定义填写开始时间
end_time = "2020-08-05 00:00:00" # 自定义结束时间
n = 144                  # 自定义抽取人数

def lottery (start,end,n):# 定义抽奖函数，在一定时间区间内抽取随机的几个时间点
    import time 
    import random
    import os 
    
    def dateTotimeStamp(date,format_string="%Y-%m-%d %H:%M:%S",digits=10):#定义字符串转时间戳函数
         
         # 时间字符串转时间戳，默认10位，时间串默认格式为"%Y-%m-%d %H:%M:%S"
        import time
        try:
            date_1 = date[:19]
            date_2 = date[20:20+digits-10]
            time_array = time.strptime(date_1,format_string)
            time_stamp = int(time.mktime(time_array))
            if digits == 10:
                return time_stamp
            else:
                time_stamp = int(time_stamp*(10 ** (digits-10)))
                time_stamp = time_stamp+int(date_2)
                return time_stamp
        except Exception as e:
                print(e)
    # 调用字符串转时间戳函数，执行转化过程 添加文件
    start = dateTotimeStamp(start)#- - - - - - - - -填写开始时间-- - - - - - - - - - - - -
    end = dateTotimeStamp(end) #- - - - - - - - - 填写结束时间- - - - - - - - -
    i = n #赋值变量 - - - - - - - - - - - - - -- - - - - - - - - - - - -- -定义需要抽奖的人数 - - - - - - - - - - - -- -  
    while   0 < i : 
        t = random.randint(start, end) # 利用随机函数，在时间区间内随机抽取一个时间戳
        dateArray = datetime.datetime.utcfromtimestamp(t)  #时间戳转换为可读的字符串时间
        otherStyleTime = dateArray.strftime( "%Y-%m-%d %H:%M:%S") #时间戳转换为可读的字符串时间
        print ("抽中随机时间点 |",otherStyleTime)   # 打印这个时间
        i = i -1   #变量调整          
lottery (start_time,end_time,n)  # 调用函数

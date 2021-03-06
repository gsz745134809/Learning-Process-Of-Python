1.得到当前时间

使用time模块，首先得到当前的时间戳
In [42]: time.time()
Out[42]: 1408066927.208922

将时间戳转换为时间元组 struct_time
In [43]: time.localtime(time.time())
Out[43]: time.struct_time(tm_year=2014, tm_mon=8, tm_mday=15, tm_hour=9, tm_min=42, tm_sec=20, tm_wday=4, tm_yday=227, tm_isdst=0)

格式化输出想要的时间
In [44]: time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
Out[44]: '2014-08-15 09:43:04'

接上文，不加参数时，默认就是输出当前的时间
In [48]: time.strftime('%Y-%m-%d %H:%M:%S')
Out[48]: '2014-08-15 09:46:53'

当然也可以透过datetime模块来实现，如下：
In [68]: t = time.time()
In [69]: datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
Out[69]: '2014-08-15 10:04:51'

同时，也可以只使用datetime模块
In [46]: datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
Out[46]: '2014-08-15 09:45:27'
In [47]: datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
Out[47]: '2014-08-15 09:46:10'

2.获取时间差，计算程序的执行时间等：

使用time模块：
In [75]: def t():
   ....:     start = time.time()
   ....:     time.sleep(10)
   ....:     end = time.time()
   ....:     print end - start
   ....:

In [76]: t()
10.0014948845

使用datetime模块：
In [49]: starttime = datetime.datetime.now()
In [50]: endtime = datetime.datetime.now()
In [51]: print (endtime - starttime).seconds
6



3.计算昨天的日期（发散思维，计算其他日期相加、相减等）：

In [52]: d1 = datetime.datetime.now()
In [53]: d2 = d1 - datetime.timedelta(days=1)
In [54]: d1
Out[54]: datetime.datetime(2014, 8, 15, 9, 54, 10, 68665)
In [55]: d2
Out[55]: datetime.datetime(2014, 8, 14, 9, 54, 10, 68665)


4.时间元组 struct_time转化为时间戳

In [56]: datetime.datetime.now()
Out[56]: datetime.datetime(2014, 8, 15, 9, 57, 52, 779893)

In [57]: datetime.datetime.now().timetuple()
Out[57]: time.struct_time(tm_year=2014, tm_mon=8, tm_mday=15, tm_hour=9, tm_min=58, tm_sec=12, tm_wday=4, tm_yday=227, tm_isdst=-1)

In [58]: time.mktime(datetime.datetime.now().timetuple())
Out[58]: 1408067904.0



5.strptime也挺有用的，将时间字符串转换为时间元组struct_time

In [73]: time.strftime('%Y-%m-%d %H:%M:%S')
Out[73]: '2014-08-15 10:27:36'

In [74]: time.strptime('2014-08-15 10:27:36','%Y-%m-%d %H:%M:%S')
Out[74]: time.struct_time(tm_year=2014, tm_mon=8, tm_mday=15, tm_hour=10, tm_min=27, tm_sec=36, tm_wday=4, tm_yday=227, tm_isdst=-1)


##二：time和datetime模块常用方法简介

表示时间的两种方式：

1. 时间戳(相对于1970.1.1 00:00:00以秒计算的偏移量),时间戳是惟一的
2. 时间元组 即(struct_time),共有九个元素，分别表示，同一个时间戳的struct_time会因为时区不同而不同


time 模块常用方法小记

1.time.clock（）

这个需要注意，在不同的系统上含义不同。在UNIX系统上，它返回的是“进程时间”，它是用秒表示的浮点数（时间 戳）。而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。（实际上是以WIN32 上QueryPerformanceCounter()为基础，它比毫秒表示更为精确）

budong@budongdeMacBook-Pro:/tmp$ cat clock.py
#!/usr/bin/env python
import time
if __name__ == '__main__':
    time.sleep(1)
    print "clock1:%s" % time.clock()
    time.sleep(1)
    print "clock2:%s" % time.clock()
    time.sleep(1)
    print "clock3:%s" % time.clock()

运行脚本：
budong@budongdeMacBook-Pro:/tmp$ ./clock.py
clock1:0.059173
clock2:0.059299
clock3:0.059416



2.time.sleep(secs)

线程推迟指定的时间运行
适合放在脚本里，定时sleep一会然后继续干啥

In [138]: while True:
   .....:     time.sleep(3)
   .....:     print time.strftime('%H:%M:%S')
   .....:
17:21:35
17:21:38
17:21:41
17:21:44
……


3.time.localtime([secs])

将一个时间戳转换成一个当前时区的struct_time，如果seconds参数未输入，则以当前时间为转换标准
未提供secs参数时，按当前时间为准
In [141]: time.localtime()
Out[141]: time.struct_time(tm_year=2014, tm_mon=8, tm_mday=14, tm_hour=17, tm_min=23, tm_sec=48, tm_wday=3, tm_yday=226, tm_isdst=0)

提供secs为当前时间戳时
In [142]: time.time()
Out[142]: 1408008232.217969
In [143]: time.localtime(time.time())
Out[143]: time.struct_time(tm_year=2014, tm_mon=8, tm_mday=14, tm_hour=17, tm_min=24, tm_sec=2, tm_wday=3, tm_yday=226, tm_isdst=0)



4.time.strftime(format[, t])

将指定的struct_time(默认为当前时间)，根据指定的格式化字符串输出
t未指定，传入time.localtime()作为默认参数：
In [156]: time.strftime('%Y-%m-%d %H:%M:%S')
Out[156]: '2014-08-14 17:28:16'

指定t为time.localtime(1407945600.0)时：
In [157]: time.localtime(1407945600.0)
Out[157]: time.struct_time(tm_year=2014, tm_mon=8, tm_mday=14, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=226, tm_isdst=0)

In [158]: time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(1407945600.0))
Out[158]: '2014-08-14 00:00:00'



5.time.time（）

返回当前时间的时间戳
In [161]: time.time()
Out[161]: 1408008711.730218

6.time.mktime(t)

将一个struct_time转换为时间戳,如下time.localtime接收一个时间戳返回一个struct_time，而time.mktime接收一个struct_time，返回一个时间戳
In [159]: time.localtime(1407945600.0)
Out[159]: time.struct_time(tm_year=2014, tm_mon=8, tm_mday=14, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=226, tm_isdst=0)
In [160]: time.mktime(time.localtime(1407945600.0))
Out[160]: 1407945600.0

残阳似血的博客：<http://qinxuye.me/article/details-about-time-module-in-python/> 

官方time模块：<http://python.me/library/time.html#module-time>



##datetime 模块常用方法小记

datetime模块常用的主要有下面这四个类：

1. datetime.date: 是指年月日构成的日期(相当于日历)
2. datetime.time: 是指时分秒微秒构成的一天24小时中的具体时间(相当于手表)
3. datetime.datetime: 上面两个合在一起，既包含时间又包含日期
4. datetime.timedelta: 时间间隔对象(timedelta)。一个时间点(datetime)加上一个时间间隔(timedelta)可以得到一个新的时间点(datetime)。比如今天的上午3点加上5个小时得到今天的上午8点。同理，两个时间点相减会得到一个时间间隔。



1.datetime.date 类

1.新建一个date对象，日期为今天，既可以直接调用datetime.date.today()，也可以直接向datetime.date()传值，如下：
In [4]: today = datetime.date.today()
In [5]: today
Out[5]: datetime.date(2014, 8, 15)
In [6]: t = datetime.date(2014,8,15)
In [7]: t
Out[7]: datetime.date(2014, 8, 15)

2.datetime.date.strftime(format) 格式化为需要的时间，如常用的 “年-月-日 小时：分钟：秒” 格式
In [8]: today.strftime('%Y-%m-%d %H:%M:%S')
Out[8]: '2014-08-15 00:00:00'
date对象中小时、分钟、秒默认都是0，纪元年的那个时间

3.datetime.date.timple() 转成struct_time格式，这样传递给time.mktime(t)  后，直接转成时间戳格式
In [9]: today.timetuple()
Out[9]: time.struct_time(tm_year=2014, tm_mon=8, tm_mday=15, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=227, tm_isdst=-1)
In [10]: time.mktime(today.timetuple())
Out[10]: 1408032000.0

4.datetime.date.replace(year, month, day)  返回一个替换后的date对象
In [11]: today.replace(year=2013)
Out[11]: datetime.date(2013, 8, 15)

5.datetime.date.fromtimestamp(timestamp) 将时间戳转化为date对象
In [12]: datetime.date.fromtimestamp(1408058729)
Out[12]: datetime.date(2014, 8, 15)



2.datetime.time 类

1.新建一个time对象
In [15]: t
Out[15]: datetime.time(8, 45, 20)

2.datetime.time.(format)格式化输出
In [16]: t.strftime('%Y-%m-%d %H:%M:%S')
Out[16]: '1900-01-01 08:45:20'
time对应的年、月、日为1900、01、01，纪元年的那个时间

3.datetime.time.replace([hour[, minute[, second[, microsecond[, tzinfo]]]]])  返回一个替换后的time对象
In [17]: t.replace(hour=9)
Out[17]: datetime.time(9, 45, 20)



3.datetime.datetime类

其实和date的那些方法差不多了，大概看以下，简单说说
1.新建一个datetime对象，日期为今天，既可以直接调用datetime.datetime.today()，也可以直接向datetime.datetime()传值，如下：
In [21]: d1 = datetime.datetime.today()
In [22]: d1
Out[22]: datetime.datetime(2014, 8, 15, 8, 12, 34, 790945)
In [23]: d2 = datetime.datetime(2014, 8, 15, 8, 12, 34, 790945)
In [24]: d2
Out[24]: datetime.datetime(2014, 8, 15, 8, 12, 34, 790945)

2.datetime.datetime.now([tz]) 当不指定时区时，和datetime.datetime.today()是一样的结果，如下
In [25]: datetime.datetime.now()
Out[25]: datetime.datetime(2014, 8, 15, 8, 14, 50, 738672)

3..datetime.datetime.strftime(format) 格式化为需要的时间，如常用的 “年-月-日 小时：分钟：秒” 格式
In [27]: d1
Out[27]: datetime.datetime(2014, 8, 15, 8, 12, 34, 790945)
In [28]: d1.strftime('%Y-%m-%d %H:%M:%S')
Out[28]: '2014-08-15 08:12:34'

4.datetime.datetime.timple() 转成struct_time格式，这样传递给time.mktime(t)  后，直接转成时间戳格式
In [29]: d1
Out[29]: datetime.datetime(2014, 8, 15, 8, 12, 34, 790945)
In [30]: d1.timetuple()
Out[30]: time.struct_time(tm_year=2014, tm_mon=8, tm_mday=15, tm_hour=8, tm_min=12, tm_sec=34, tm_wday=4, tm_yday=227, tm_isdst=-1)
In [31]: time.mktime(d1.timetuple())
Out[31]: 1408061554.0

5.datetime.datetime.replace(year, month, day)  返回一个替换后的date对象
In [32]: d1
Out[32]: datetime.datetime(2014, 8, 15, 8, 12, 34, 790945)
In [33]: d1.replace(year=2000)
Out[33]: datetime.datetime(2000, 8, 15, 8, 12, 34, 790945)

6.datetime.datetime.fromtimestamp(timestamp) 将时间戳转化为datetime对象
In [34]: time.time()
Out[34]: 1408061894.081552
In [35]: datetime.datetime.fromtimestamp(1408061894)
Out[35]: datetime.datetime(2014, 8, 15, 8, 18, 14)

4.datetime.timedelta类

没啥好说的，主要做时间的加减法用，如下：
In [78]: today = datetime.datetime.today()
In [79]: yesterday = today - datetime.timedelta(days=1)
In [80]: yesterday
Out[80]: datetime.datetime(2014, 8, 14, 15, 8, 25, 783471)
In [81]: today
Out[81]: datetime.datetime(2014, 8, 15, 15, 8, 25, 783471)
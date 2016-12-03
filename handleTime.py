import time
from datetime import datetime, timedelta

def strTimetoMkTime(str):  #Str = '2014-03-21 00:00:00';
    temp = time.strptime(str+' 00:00:00', "%Y-%m-%d %H:%M:%S");
    return int(time.mktime(temp));

def strToDate(str):
    return  time.strptime(str,'%Y-%m-%d');

def dateBeforDays(stampTime,dayNum):
    dateArray=datetime.utcfromtimestamp(stampTime);
    temp = dateArray - timedelta(days=dayNum)
    return int(time.mktime(temp.timetuple()));

def dateAfterdays(stampTime,dayNum):
    dateArray = datetime.utcfromtimestamp(stampTime);
    temp = dateArray + timedelta(days=dayNum)
    return int(time.mktime(temp.timetuple()));

def getDayByStr(str):
    date=strToDate(str);
    return date.tm_mday;



# print(strTimetoMkTime('2014-03-21 00:00:00'));
# print(strTimetoMkTime('2014-03-21'+' 00:00:00'));

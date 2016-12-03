import evaluate
import handleTime
import pandas as pd
import interstNews
import time


def recommendOneDay(nowDate,kk):
    users = pd.read_table('newsTest.txt', encoding='utf-8');
    users['time'].astype(int);
    divsionTime = handleTime.strTimetoMkTime(nowDate);
    divsionTime=handleTime.dateAfterdays(divsionTime,1);#获取后一天凌晨时间
    users = users[users['time'] < divsionTime];
    users = users['userid'].value_counts();
    interstNews.recommendNewsForUsers(users.index,recommendK=kk,Date=nowDate,Kvalue=260);


start=time.time();
days=['21','22','23','24','25','26','27','28','29','30']
strtime='2014-3-';
i=0;
nowdate=strtime+days[i];
for index in range(5,15):
    print(index);
    recommendOneDay(nowdate,index);
    evaluate.cacualte(days[i],nowdate);#recommendOneDay('2014-3-21');
end=time.time();
print('time =',end-start);
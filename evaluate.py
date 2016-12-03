import pandas as pd
import time

import handleTime


def cacualte(date,nowDate):
    dataRcm=pd.read_table('recommendNews'+date+'.txt',encoding='utf-8');
    datatest=pd.read_table('newsTest.txt',encoding='utf-8');
    time=handleTime.strTimetoMkTime(nowDate);
    timeafter=handleTime.dateAfterdays(time,1);
    datatest['time'].astype(int);
    datatest=datatest[datatest['time']<timeafter];
    datatest=datatest[datatest['time']>=time];
    testCount=pd.Series.count(datatest['newsId']);
    rcmCount=pd.Series.count(dataRcm['newsId']);
    intersection=0
    usersNews=dict();
    for index,row in dataRcm.iterrows():
        if row['userid'] not in usersNews:
             usersNews[row['userid']]=set();
        usersNews[row['userid']].add(row['newsId']);
    for u,v in usersNews.items():
        datatesttemp=datatest[datatest['userid']==u];

        #print(datatesttemp,'woshilinsgi ');
        for t in v:
            for index,row in datatesttemp.iterrows():
                if row['newsId']==t:
                    intersection+=1;

    print('recall',float(intersection)/testCount*100);
    print('precison', float(intersection) / rcmCount*100);


def caculateHotNews(date,hotNews):
    data=pd.read_table('newsTest.txt',encoding='utf-8');
    time=handleTime.strTimetoMkTime(date);
    afterTime=handleTime.dateAfterdays(time,1);
    data['time'].astype(int);
    data=data[data['time']<afterTime];
    data=data[data['time']>=time];
    userlist=data['userid'].value_counts();
    hotnewsCount=pd.Series.count(hotNews)*pd.Series.count(userlist.index);
    userNewsCount=pd.Series.count(data['newsId']);
    intersection=data['newsId'].isin(hotNews);
    intersection=intersection.value_counts()[True];
    print('recall', float(intersection) / userNewsCount * 100);
    print('precison', float(intersection) / hotnewsCount * 100);

def findDays(): #检查过去T天新闻，在当前一天新闻的差异
    datatest = pd.read_table('newsTest.txt', encoding='utf-8');
    time = handleTime.strTimetoMkTime('2014-3-22');
    datatest['time'].astype(int);
    datatest = datatest[datatest['time'] < time];
    datatest=datatest['newsId'].value_counts();
    print(datatest,'test');
    datatrain = pd.read_table('newsTrain.txt', encoding='utf-8');
    time = handleTime.strTimetoMkTime('2014-3-16');
    datatrain['time'].astype(int);
    datatrain = datatrain[datatrain['time'] >= time];
    datatrain=datatrain['newsId'].value_counts();
    #print(pd.Series.count(datatrain.index),'train');
    rsult=datatrain.index.isin(datatest.index);
    print(pd.Series(rsult).value_counts());





#cacualte()
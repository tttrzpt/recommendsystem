import handleTime
import trainDataByUser_User
import pandas as pd
import time


def getSimilarityUsers(u):
    data=trainDataByUser_User.getSimilarity();
    #data=pd.read_csv('similarituUser.txt',encoding='utf-8')
    #print(data)
    #print('stoooooop');
    return data[u];


def filterlooked(similarNews,date):
    if handleTime.getDayByStr(date)>21:
        data=pd.read_table('newsTest.txt',encoding='utf-8');
        data['time'].astype(int);
        nowtime=handleTime.strTimetoMkTime(date);
        befortime=handleTime.dateBeforDays(nowtime,1);
        data=data[data['time']<nowtime];
        data=data[data['time']>=befortime];

    else:
        data=pd.read_table('newsTrain.txt',encoding='utf-8');
        data['time'].astype(int);
        data=data[data['time']>handleTime.strTimetoMkTime('2014-3-20')];
    for u,v in similarNews.items():
        temp=data[data['userid']==u];
        for t in v:
            for index,row in temp.iterrows():
                if row['newsId']==t:
                    similarNews[u].remove(t);
                    if similarNews[u].__len__()==0:
                        del similarNews[u];
    return similarNews;



def getSimilarityToNews(similarityUsers,nowDate='2014-3-21',K=5,days=1):
    #similarityUsers= pd.Series(getSimilarityUsers(user));
    orderUsers= similarityUsers.sort_values(ascending=False);
    kUser=orderUsers[:K];


    dateDay = handleTime.getDayByStr(nowDate);
    nowDate=handleTime.strTimetoMkTime(nowDate);
    newsTest = pd.read_table('newsTest.txt', encoding='utf-8');
    newsTest['time'].astype(int);
    newsFromTest=newsTest[newsTest['time']<nowDate];#选择过去days天内的新闻
    newsFromTest=newsFromTest[newsFromTest['time']>handleTime.dateBeforDays(nowDate,days)];
    newsFromTest['userid'].astype(kUser.index.dtype);
    #print('userid in kuser  ',newsFromTest['userid'].isin(kUser.index));
    newsSimFromTest=newsFromTest[newsFromTest['userid'].isin(kUser.index)];
    #print('xinwengeshu form test ',newsSimFromTest['newsId'].value_counts());
    newsInterst=dict();
    for index,row in newsSimFromTest.iterrows():
        if row['newsId'] not in newsInterst:
            newsInterst[row['newsId']]=0;
        newsInterst[row['newsId']]+=kUser[row['userid']];
    if dateDay<=(20+days):
        newsTrain = pd.read_table('newsTrain.txt', encoding='utf-8');
        newsTrain['time'].astype(int);
        divisionTime=handleTime.dateBeforDays(nowDate,days);
        newsFromTrain=newsTrain[newsTrain['time']>=divisionTime];
        newsSimFromTrain=newsFromTrain[newsFromTrain['userid'].isin(kUser.index) ];

        #print('woshi isin train valuecount',newsFromTrain['userid'].isin(kUser.index).value_counts() );
        #print('xinwengeshu ', newsSimFromTrain['newsId'].value_counts());
        for index, row in newsSimFromTrain.iterrows():
            if row['newsId'] not in newsInterst:
                newsInterst[row['newsId']] = 0;
            newsInterst[row['newsId']] += kUser[row['userid']];

    #print('woshi xinwen ',newsInterst);
    return newsInterst;


def recommendNewsForUsers(users,recommendK=1,Kvalue=1,Date='2014-3-21'):
    data = trainDataByUser_User.getSimilarity();
    #recommendNews=dict();
    #data=filterlooked(data,Date);
    recommendNews=[];
    for u in users:
        # if u not in recommendNews:
        #     recommendNews[u]=set();
        if u not in data.keys():
            continue;
        news=getSimilarityToNews(pd.Series(data[u]),K=Kvalue,nowDate=Date);

        news=pd.Series(news);
        news=news.sort_values(ascending=False);
        news=news[:recommendK];
        for n in news.index:
            #recommendNews[u].add(n);
            recommendNews.append([u,n]);

    recommendNews=pd.DataFrame(recommendNews,columns=['userid','newsId']);
    recommendNews.to_csv('recommendNews'+str(handleTime.getDayByStr(Date))+'.txt',sep='\t',encoding='utf-8',index=False);



# start=time.time()
# #getSimilarityToNews(2379359);
# #getSimilarityUsers(75);
# users=pd.read_table('newsTest.txt',encoding='utf-8');
# users['time'].astype(int);
# divsionTime=handleTime.strTimetoMkTime('2014-03-22 00:00:00');
# users=users[users['time']<divsionTime];
# users=users['userid'].value_counts();
# recommendNewsForUsers(users.index);
#
# end=time.time();
# print(end-start);
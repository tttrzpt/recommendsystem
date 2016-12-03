import evaluate
import handleTime
import pandas as pd
def getHotNews(date,recommendK):
    #data=None;
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
    data = data['newsId'].value_counts();
    data = pd.Series(data.index);
    data = data[:recommendK];
    return data;

#print(getHotNews('2014-3-21',50));
evaluate.caculateHotNews('2014-3-21',getHotNews('2014-3-21',60));
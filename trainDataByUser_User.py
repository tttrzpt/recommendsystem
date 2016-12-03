import pandas as pd
import math


def getSimilarity():


    data=pd.read_table('newsTrain.txt',encoding='utf-8');
    #testdata=pd.read_table('newsTest.txt',encoding='utf-8');
    #print(testdata.groupby('userid'));

    itemUser=dict();
    for index,row in data.iterrows():
        if row['newsId'] not in itemUser:
            itemUser[row['newsId']]=set();
        itemUser[row['newsId']].add(row['userid']);



    intersection =dict();
    num=dict();

    for i ,users in itemUser.items():
        for u in users:
            if u not in num:
                num[u]=0;
                intersection[u]=dict();
            num[u]+=1;
            for v in users:
                if u==v:
                    continue;
                if v not in intersection[u]:
                    intersection[u][v]=0;
                intersection[u][v]+=1;

    similarityUserToUser=dict();
    for u,item in intersection.items():
        similarityUserToUser[u]=dict();
        for v,s in item.items():
            similarityUserToUser[u][v]=s/math.sqrt(num[u]*num[v]);
    #pd.DataFrame(similarityUserToUser).to_csv('similarituUser.txt',encoding='utf-8');

    return similarityUserToUser;
#getSimilarity();
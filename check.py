import pandas as pd

trainData=pd.read_table('newsTrain.txt',encoding='utf-8');
testData=pd.read_table('newsTest.txt',encoding='utf-8');

trainNewsIdCount = trainData['newsId'].value_counts();
testNewsIdCount=testData['newsId'].value_counts();
result=testNewsIdCount.index.isin(trainNewsIdCount.index);
tt=pd.Series(result);
print(tt.value_counts());
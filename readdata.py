
import handleTime
import pandas as pd

#f=os.open('user_click_data.txt',flags=,encoding='utf-8');
#f=BytesIO(open('user_click_data.txt').read().encode('utf-8'));
#np.loadtxt(f,delimiter='\t');,parse_dates=['time'],date_parser=time.localtime(int())
#np.loadtxt(io.StringIO(''.join(line for line in open('user_click_data.txt', encoding='utf-8') if not line.lstrip().startswith('!'))))
#data=pd.read_table('user_click_data.txt',names=['userid','newsId','time','newsTitle','newsContent','newsTime'],parse_dates=['time'],date_parser=gettime,nrows=4);
data=pd.read_table('user_click_data.txt',names=['userid','newsId','time','newsTitle','newsContent','newsTime']);
divisionTimeStr='2014-03-21 00:00:00';
divisionTime=handleTime.strTimetoMkTime(divisionTimeStr);
print(divisionTime);
#print(data[int(data['time'])<divisionTime]);
data['time'].astype('int');
frist20dayData=data[data['time']<divisionTime];
last10dayData=data[data['time']>=divisionTime];
frist20dayData.to_csv('newsTrain.txt',sep='\t',encoding='utf-8',index=False,columns=['userid','newsId','time']);
last10dayData.to_csv('newsTest.txt',sep='\t',encoding='utf-8',index=False,columns=['userid','newsId','time']);
#print(time.localtime(int(testTime)))

#print(data['time'].dtype);
#type (data);
#! ~/miniconda3/env python3

import pandas as pd 
import os 
from scipy import stats
os.chdir('G:\paper_SNP\pNpS')

sum1,sum2=[],[]
s1=[]
for files in os.listdir('.'):
    if files[-3:]=='tab':
        source_data=pd.read_csv(files,sep='\t',header=0,index_col=0)
        #c_1=source_data.iloc[:,0:3]
        #c_2=source_data.iloc[:,4:]
        c_1=source_data.loc[:,['zhq05','zhq510','zhq1015','zhq1520']]
        c_2=source_data.loc[:,['zhq2030','zhq3040','zhq4050','zhq5060','zhq6080','zhq80100']]
        c1_mean=c_1.mean(axis=1)
        c2_mean=c_2.mean(axis=1)
        s1.append(source_data.mean())

        sum1,sum2=0,0
        count1,count2=0,0
        for i in c1_mean:
            if not i==0:
                sum1+=i
                count1+=1
        for i in c2_mean:
            if not i==0:
                sum2+=i
                count2+=1
        try:
            mean1=sum1/(count1)
        except ZeroDivisionError:
            mean1=0
        mean2=sum2/(count2)
        #mean1,mean2=c1_mean.mean(),c2_mean.mean()
        #sum1.append(mean1)
        #sum2.append(mean2)
        print(files,mean1,mean2)
s1=pd.DataFrame(s1)
#s1.to_csv('average_pNpS',sep='\t',header=True)


print(stats.ttest_ind(sum1,sum2))
print(s1.mean())
#!/usr/bin/env python3
'''


'''

print('''脚本是用来导出任意文件夹中相同的列
仅对contigs有效！！！！
如读取SNP 数量等 ''')

import pandas as pd 

import os , re

col_names='SNV_count'
out_dir='F:/SYSU_daily/SNP/result_merge'



out={}
os.chdir('F:/SYSU_daily/SNP/result_merge')
for dir2 in os.listdir('.'):
    if dir2[-6:]=='all.IS':
        print(dir2)
        os.chdir('%s/output'%dir2)
        for files in os.listdir('.'):
            if re.match('.*genome_info.tsv',files):
                source=pd.read_csv(files,sep='\t',header=0,index_col=0)
                s=dir2.split('_')[0]
                out[s]=source[col_names] 
                os.chdir('..')
            else:
                pass
        os.chdir('..')

os.chdir(out_dir)
    
out_df=pd.DataFrame(out)
    
out_df.fillna(0,inplace= True)
out_df.to_csv('%s.tab'%col_names,sep='\t',index=True,header=True)
#!/usr/bin/env python3
import pandas as pd 

'''
2022.5.30重要更新
这个脚本改成了


'''


import os , re
print('''脚本是用来导出任意文件夹中相同的列
仅对gene有效！！！！
如读取SNP 数量等 ''')

col_names='dNdS_substitutions'
out_dir='G:/SYSU_daily/SNP/result_merge/dNdS'

out={}
os.chdir('G:/SYSU_daily/SNP/result_merge')
for dir2 in os.listdir('.'):
    if dir2[-6:]=='all.IS':
        print(dir2)
        os.chdir('%s/output'%dir2)
        for files in os.listdir('.'):
            if re.match('.*gene_info.tsv',files):
                source=pd.read_csv(files,sep='\t',header=0,index_col=1)
                s=dir2.split('_')[0]
                out[s]=source[col_names] 
                os.chdir('..')
            else:
                pass
        os.chdir('..')

gen_stb=open('genomes.stb','r').readlines()
out_index={}
for line in gen_stb:
    line=line.strip().split('\t')
    if line[1] not in out_index:
        out_index[line[1]]=[line[0]]
    else:
        out_index[line[1]].append(line[0])


os.chdir(out_dir)

for i,j in out_index.items():
    out_write={'zhq05':[],'zhq1015':[],'zhq1520':[],'zhq2030':[],'zhq3040':[],'zhq4050':[],'zhq5060':[],'zhq510':[],'zhq6080':[],'zhq80100':[]}
    ind=[]
    for m ,n in out.items():
        tmp=[]
        tmp_d={}
        for x , y in n.items():
            x_j='_'.join(x.split('_')[:-1])
            if x_j in j:
                if not  x in ind:
                    ind.append(x)
                if not x in tmp:
                    tmp.append(x)
                    tmp_d[x]=y
        out_write[m].append(tmp_d)
    for ke,va in out_write.items():
        tmp=[]
        va=va[0]
        for gene,valu in va.items():
            if not gene in tmp:
                tmp.append(gene)
        for test in ind:
            if test not in tmp:
                out_write[ke][0][test]=0
        out_write[ke]=out_write[ke][0]
        
    
    
    out_df=pd.DataFrame(out_write,index=ind)
    
    out_df.fillna(0,inplace= True)
    out_df.to_csv(i+'.%s.tab'%col_names,sep='\t',index=True,header=True)

    

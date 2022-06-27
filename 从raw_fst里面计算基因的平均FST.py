#! /usr/bin/env python3

import pandas as pd 
import re, os 


#先过滤掉非ORF位点
def filtered_not_orf():
    os.chdir('G:/SYSU_daily/SNP/result_merge')
    out=[]
    for dir2 in os.listdir('.'):
        if dir2[-6:]=='all.IS':
            os.chdir('G:/SYSU_daily/SNP/result_merge/%s/output'%dir2)
            for files in os.listdir('.'):
                if re.match('.*SNVs.tsv',files):
                    print(files)
                    source=pd.read_csv(files,sep='\t',header=0)
                    for i in range(len(source['scaffold'])):
                        if source['mutation_type'][i]=='I':
                            pass
                        elif source['gene'][i]=='':
                            pass
                        else:
                            contig_pos=source['scaffold'][i]+'_'+str(source['position'][i])
                            if contig_pos not in out:
                                out.append(contig_pos)
    return (out)

datas=open('G:/paper_SNP/0_20_vs_30_100.weir.fst','r+')
outs=filtered_not_orf()
print(len(outs))
filter_out=open('G:/paper_SNP/filtered_fst','w+')
for line in datas.readlines():
    line=line.strip().split('\t')
    if line[0]+'_'+str(line[1]) in outs:
        filter_out.write('\t'.join(line)+'\n')


'''
def read_freq(gene_dir):
    os.chdir('F:/SYSU_daily/SNP/result_merge')
    #那些所有样点结果所在的文件夹，是主目录
    freq_out={}
    for i in gene_dir.values():
        if i not in freq_out:
            freq_out[i]={5:[],10:[],15:[],20:[],30:[],40:[],50:[],60:[],80:[],100:[]}
    #每个相同的coontigs给一个字典
    out_ind={'zhq05':5,'zhq510':10,'zhq1015':15,'zhq1520':20,'zhq2030':30,\
    'zhq3040':40,'zhq4050':50,'zhq5060':60,'zhq6080':80,'zhq80100':100}
    for dir2 in os.listdir('.'):
        if dir2[-6:]=='all.IS':
            os.chdir('%s/output'%dir2)
            depth=out_ind[dir2.split('_')[0]]
            for files in os.listdir('.'):
                if re.match('.*SNVs.tsv',files):
                    source=pd.read_csv(files,sep='\t',header=0)
'''

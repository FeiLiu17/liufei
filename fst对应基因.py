import os , re
from turtle import position 

def read_fna():
    gene_file=open('G:/SYSU_daily/SNP/all_genomes.fna','r+').readlines()
    out={}
    for i in gene_file:
        if re.match('>',i):
            i=i.strip().lstrip('>').split('#')
            contigs='_'.join(i[0].split('_')[:-1])
            gene=i[0].strip()
            start=i[1].strip()
            end=i[2].strip()
            if contigs not in out:
                out[contigs]={}
                out[contigs][gene]=[start,end]
            else:
                out[contigs][gene]=[start,end]
        else:
            pass
    return(out)

def read_sites_fst(fna_set):
    os.chdir('G:/paper_SNP/FST_raw')
    nubers=open('G:/paper_SNP/gene_number_in_contigs.tab','r+').readlines()
    contigs2number={}
    for line in nubers:
        line=line.strip().split('\t')
        contigs2number[line[0]]=line[1]
    for files in os.listdir('.'):
        if files[-3:]=='tab':
            gene_row=open('fst_gene_row/%s'%files,'w+')
            with open(files,'r+') as lines:
                for line in lines.readlines():
                    line=line.strip().split('\t')
                    contigs='_'.join(line[0].split('_')[:-1])
                    position=line[0].split('_')[-1]
                    if contigs in fna_set:
                        contigs_number=contigs2number[contigs]
                        for x,y in fna_set[contigs].items():
                            if int(position) in range(int(y[0]),int(y[1])):
                                gene_row.write(x+'\t'+position+'\t'+line[1]+'\t'+contigs_number+'\n')

def main():
    fna_set=read_fna()
    read_sites_fst(fna_set)

if __name__=='__main__':
    main()


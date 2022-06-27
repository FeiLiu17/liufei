
#仅用于计算并校正P_value
setwd('E:/paper_SNP/related_data/fig-02-RGs/relative_abundance_info')
library(Hmisc)

relationships=read.csv('RGS_relative_abundance.txt',sep = '\t',header = 1,row.names = 1)
t_r=data.frame(t(relationships))

res <- rcorr(as.matrix(t_r))

#pearson

CorMatrix <- function(cor,p) {
                               ut <- upper.tri(cor) 
                               data.frame(row = rownames(cor)[row(cor)[ut]] ,
                               column = rownames(cor)[col(cor)[ut]], 
                               cor =(cor)[ut], 
                               p = p[ut] )
}
x=CorMatrix (res$r, res$P)
need_data<- x[which(x$column%in%'Depths'),]
need_data[which(p.adjust(need_data$p, method = 'fdr') ),]
need_data$cor2=need_data$cor^2
need_data$p_adj=p.adjust(need_data$p, method = 'fdr')


#使用相关系数绘图
library(ggplot2)
set.seed(10)
xlabs=need_data$row
ylabs=need_data$cor2

xx=data.frame(xlabs,ylabs)

ggplot(xx,aes(xlabs,ylabs))+
  geom_bar(stat='identity',color='#FF3333',fill='#FF3333',width=0.7)+
  theme(axis.text.y = element_text(angle = , hjust = 1))+
  xlab('')+
  ylab('R-squared')+
  #ggtitle('Coverage-Layer')+
  ylim(0,0.93)+
  coord_flip()+
  theme(axis.title.x=element_text(vjust=2, size=15,face = "bold"))+
  theme(axis.text.x = element_text(size = 14,,face = "bold"))+
  theme(axis.text.y = element_text(size = 14,,face = "bold"))+
  theme(axis.title.y=element_text(vjust=2, size=15,face = "bold"))+
  theme(panel.grid=element_blank())


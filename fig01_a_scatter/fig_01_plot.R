library(ggplot2)
library('export')
setwd('E:/paper_SNP/redo/fig01_a_scatter')
#set the work diction 

df=read.csv('Ndb.csv')

windowsFonts(A=windowsFont('Times New Roman'))
# the font
dev.new()
ggplot(df,aes(x=ani*100,y=alignment_coverage*100))+
  geom_point(size=4,alpha=0.3)+
  scale_x_continuous(labels = scales::label_comma(accuracy =1))+
  geom_vline(xintercept = 97,color='red',linetype="dashed",size=2,alpha=1)+
  labs(x =  paste('ANI (%)'), y = paste('Alignment Coverage (%)'))+
  theme_classic()+
  theme(text = element_text(family = 'A',size = 21))+
  theme(aspect.ratio = 1)
dev.off()

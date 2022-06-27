library(vegan)
library(ggplot2)
library(psych)
library(ggrepel)
library(FactoMineR)
library(RColorBrewer)


setwd('F:/paper_SNP/redo/fig01_b_pca')
file_name='related_abundance_rgs_info.txt'
abundance_tab=read.csv(file_name,sep = '\t',row.names = 1,header = 1)
abundance_tab <- data.frame((abundance_tab))
group=read.csv('groups.txt',
               sep = '\t',header = 1, row.names = 1)
ab.pca<-PCA(abundance_tab)
pca_sample <- data.frame(ab.pca$ind$coord[ ,1:2])
pca_sample$samples <- group$groups
pca_sample$Dim.1<-as.numeric(pca_sample$Dim.1)
pca_sample$Dim.2<-as.numeric(pca_sample$Dim.2)
pca_eig1 <- round(ab.pca$eig[1,2], 2)
pca_eig2 <- round(ab.pca$eig[2,2],2 )
#利用圆圈把同组的圈起�?
ggplot(data = pca_sample, aes(x = Dim.1, y = Dim.2,color=samples)) +
  geom_point(aes(color = samples), size = 3)+ 
  theme(panel.grid = element_blank(), panel.background = element_rect(color = 'black', fill = 'transparent'), 
        legend.key = element_rect(fill = 'transparent')) +  
  stat_ellipse(data=pca_sample,
               geom = "polygon",
               aes(fill=samples),
               alpha=0.2,level = 0.9,show.legend = F)+
  labs(x =  paste('PCA1:', pca_eig1, '%'), y = paste('PCA2:', pca_eig2, '%'), color = '',title = '')+  #�? PCA 轴贡献度添加到坐标轴标题�?
  theme(axis.title.x=element_text(vjust=2, size=15,face = "bold"))+
  theme(axis.title.y=element_text(vjust=2, size=15,face = "bold"))+
  theme(legend.key.size = unit(0.28, "inches"),legend.text=element_text(size=12))

  #使用线条（多边形）将同组连接起来
ggplot(data = pca_sample, aes(x = Dim.1, y = Dim.2,color=samples)) +
  geom_point(aes(color = samples), size = 3)+  
  theme(panel.grid = element_blank(), panel.background = element_rect(color = 'black', fill = 'transparent'), 
        legend.key = element_rect(fill = 'transparent')) +  
  geom_polygon(data = pca_sample, alpha = 0.5, aes(fill = factor(samples)),show.legend = F)+
  labs(x =  paste('PCA1:', pca_eig1, '%'), y = paste('PCA2:', pca_eig2, '%'), color = '',title = '')+#�? PCA 轴贡献度添加到坐标轴标题�?
  theme(axis.title.x=element_text(vjust=2, size=15,face = "bold"))+
  theme(axis.title.y=element_text(vjust=2, size=15,face = "bold"))+
  theme(legend.key.size = unit(0.32, "inches"),legend.text=element_text(size=14))



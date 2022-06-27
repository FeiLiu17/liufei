library(ComplexHeatmap)
library(circlize)
setwd('G:/paper_SNP/redo/fig01_c_heatmap/relative_abundance_info')
datas=read.csv('RGS_relative_abundance.txt',sep='\t',header=1,row.names = 1)

#this package wouldn't  normalize the data set, so, we must scale them before plot if necessary.
#as following:
exp_datas<-apply(datas, 1, scale)
rownames(exp_datas)<-colnames(datas)
exp_datas<-t(exp_datas)

#color function
col_fun = colorRamp2(c(0,0.04,0.08),c('#FFCC99','#FF6633','#CC3300'))
#or, there are simple method for color:
#1.  col = rev(rainbow(10))
#2. col=c('#FFCC99','#FF6633','#CC3300')

datas=t(datas)
top_ann=HeatmapAnnotation(BoxPlot=anno_boxplot(datas))

Heatmap(datas,clustering_distance_rows = "pearson",cluster_rows=F,cluster_columns = T,col=c('#FFCC99','#FF6633','#CC3300'),name = 'DNA Relative Abundance',na_col = "black",
        border = F,rect_gp = gpar(col = "white", lwd = 0.5),column_title='', row_title ='',row_names_side = 'left',column_names_rot = 90,
        row_names_max_width=max_text_width(rownames(datas),gp=gpar(fontsize=20)),column_names_gp = gpar(fontsize=12),
        top_annotation = top_ann,column_names_max_height =max_text_width(colnames(datas)) ,row_dend_side = 'right')






#test code 

#ha = HeatmapAnnotation(boxplot = anno_boxplot(datas))

Heatmap(datas,clustering_distance_rows = "pearson",cluster_rows=T,cluster_columns = F,col=c('#FFCC99','#FF6633','#CC3300'),name = 'DNA Relative Abundance',na_col = "black",
        border = F,rect_gp = gpar(col = "white", lwd = 0.5),column_title='', row_title ='',row_names_side = 'right',column_names_rot = 45,
        row_names_max_width=max_text_width(rownames(datas),gp=gpar(fontsize=20)),
        top_annotation = ha)



dat=t(datas)
left_anno=rowAnnotation(boxx=anno_boxplot(t(dat)))
Heatmap(datas,clustering_distance_rows = "pearson",cluster_rows=T,cluster_columns = F,col=c('#FFCC99','#FF6633','#CC3300'),name = 'DNA Relative Abundance',na_col = "black",
        border = F,rect_gp = gpar(col = "white", lwd = 0.5),column_title='', row_title ='',row_names_side = 'right',column_names_rot = 45,
        row_names_max_width=max_text_width(rownames(datas),gp=gpar(fontsize=20)),
        right_annotation = left_anno)

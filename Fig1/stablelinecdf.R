library(ggplot2)
library(ggbeeswarm)
df<-data.frame(NCTGFPStableNucleiquantitation2) 
dfgroups<-c("2xSV40","NCT15","NCT20")
dfgroupssubset<-(subset(df, Cell_Line %in% dfgroups))
dfsample<-dfgroupssubset[sample(nrow(dfgroupssubset), 300, replace = FALSE),]
p<- ggplot(dfsample, aes(x=Cell_Line, y=Nuclei_signal, color=Cell_Line)) +
  geom_beeswarm(cex = 1.7, size=12) +
  scale_color_manual(values=c("#e39010", "#e31063", "#13a558"))+
  theme_classic()+
  ylim(0,50)
p

#CDF plot
ggplot(dfgroupssubset, aes(x=Nuclei_signal, color=Cell_Line)) + stat_ecdf(geom="line", size=6)+
  theme(legend.position="none")+
  scale_color_manual(values=c("#e39010", "#e31063", "#13a558"))+
  xlim(0,100)+
  theme_classic()

#kolmogorov-smirnov
subsetnct20<-c(subset(df,subset = Cell_Line =="NCT20")$Nuclei_signal)
subsetsv40<-c(subset(df,subset = Cell_Line =="2xSV40")$Nuclei_signal)
subsetnct15<-c(subset(df,subset = Cell_Line =="NCT15")$Nuclei_signal)
ks.test(subsetnct20, subsetsv40)
ks.test(subsetnct15, subsetsv40)
ks.test(subsetnct15, subsetnct20)

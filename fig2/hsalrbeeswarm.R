library(ggplot2)
library(ggbeeswarm)
library(forcats)
df<-data.frame(HSALRcy5data) 
dfgroups<-c("scramble","sv40","myospreader")
dfscramblesubset<-(subset(df, treatment=="scramble"))
dfscramble<-dfscramblesubset[sample(nrow(dfscramblesubset), 150, replace = FALSE),]
dfsvsubset<-(subset(df, treatment=="sv40"))
dfsv<-dfsvsubset[sample(nrow(dfsvsubset), 150, replace = FALSE),]
dfmyosubset<-(subset(df, treatment=="myospreader"))
dfmyo<-dfmyosubset[sample(nrow(dfmyosubset), 150, replace = FALSE),]
dfsample<-rbind(dfscramble,dfsv,dfmyo)
p<- ggplot(dfsample, aes(x=forcats::fct_relevel(treatment, "scramble","sv40","myospreader"), y=cy5, color=treatment)) +
  geom_beeswarm(cex = 1.7, size=12) +
  scale_color_manual(values=c("#13a558", "#9010e2ff", "#e39010"))+
  theme_classic()+
  ylim(0,9000)
p

#violinplot
ggplot(dfsubset, aes(x=forcats::fct_relevel(treatment, "scramble","sv40","myospreader"), y=cy5, fill=treatment)) +
  geom_violin(size=3, color="#000000") +
  stat_summary(fun.y=mean, geom="point", shape=23, size=2)+
  theme_classic()+
  scale_fill_manual(values=c("#13a558", "#9010e2ff", "#e39010"))+
  ylim(0,9000)+
  theme(legend.position="none")


#CDF plot
ggplot(df, aes(x=cy5, color=forcats::fct_relevel(treatment, "scramble","sv40","myospreader"))) + stat_ecdf(geom="line", size=6)+
  scale_color_manual(values=c("#9010e2ff",  "#e39010", "#13a558"))+
  xlim(0,7500)+
  theme_classic()+
  theme(legend.position="none")

#kolmogorov-smirnov
subsetmyo<-c(subset(df,subset = treatment =="myospreader")$cy5)
subsetsv<-c(subset(df,subset = treatment =="sv40")$cy5)
subsetscramble<-c(subset(df,subset = treatment =="scramble")$cy5)
ks.test(subsetmyo, subsetsv)
ks.test(subsetscramble, subsetsv)
ks.test(subsetscramble, subsetmyo)

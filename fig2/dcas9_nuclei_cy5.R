library(ggplot2)
library(forcats)
df<-data.frame(HSALRcy5data_aavnuclei) 
#violinplot
p<-ggplot(df, aes(x=forcats::fct_relevel(treatment, "scramble","sv40","myospreader"), y=cy5data, fill=treatment)) +
  geom_violin(size=3, color="#000000") +
  stat_summary(fun.y=mean, geom="point", shape=23, linewidth=2)+
  theme_classic()+
  scale_fill_manual(values=c("#13a558", "#9010e2ff", "#e39010"))+
  ylim(0,9000)+
  theme(legend.position="none")
p

#CDF plot
ggplot(df, aes(x=cy5data, color=forcats::fct_relevel(treatment, "scramble","sv40","myospreader"))) + stat_ecdf(geom="line", size=6)+
  scale_color_manual(values=c("#9010e2ff",  "#e39010", "#13a558"))+
  xlim(0,7500)+
  theme_classic()+
  theme(legend.position="none")
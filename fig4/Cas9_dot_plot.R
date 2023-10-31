library(ggplot2)
df<-data.frame(RTPCR_cas9_data)
df$Treatment<- factor(df$Treatment, levels=c("PBS", "2xSV40/MDXsg", "Myospreader/MDXsg"))
df$Muscle<- factor(df$Muscle, levels=c("TA", "Gast","Quad","TRI"))
p<-ggplot(df, aes(x=Muscle, y=PercentRescue, fill=Treatment)) +
  geom_dotplot(binaxis='y', stackdir='center',
               position=position_dodge(.75))+
  ylim(0,4)
p + scale_fill_manual(values=c("#37b3f9", "#e39010", "#13a558")) + theme_classic()

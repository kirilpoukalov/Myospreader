library(ggplot2)
df<-data.frame(dcas9_HSALR_data)
df$Treatment<- factor(df$Treatment, levels=c("PBS","2xSV_Scramble","2xSV_CUG", "myospreader_CUG"))
p<-ggplot(df, aes(x=Treatment, y=Gene.Expression.Ratio, fill=Treatment)) +
  geom_dotplot(binaxis='y', stackdir='center',
               position=position_dodge(.5))+
  ylim(0,3)
p + scale_fill_manual(values=c("#37b3f9","#9010e3", "#e39010", "#13a558")) + theme_classic()

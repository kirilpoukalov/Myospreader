library(ggplot2)
df<-data.frame(C2C12saCas9_data)
df$Treatment<- factor(df$Treatment, levels=c("PBS","2xSV40", "Myospreader"))
p<-ggplot(df, aes(x=Treatment, y=Gene.Expression.Ratio, fill=Treatment)) +
  geom_dotplot(binaxis='y', stackdir='center',
               position=position_dodge(.5))+
  ylim(0,1.5)
p + scale_fill_manual(values=c("#37b3f9", "#e39010", "#13a558")) + theme_classic()

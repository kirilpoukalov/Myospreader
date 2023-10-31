library(ggplot2)
df<-data.frame(Discord_data_r)
df$Treatment<- factor(df$Treatment, levels=c("PBS", "2xSV40", "Myospreader"))
p<-ggplot(df, aes(x=Treatment, y=Discordance, fill=Treatment)) +
  geom_dotplot(binaxis='y', stackdir='center',
               position=position_dodge(.75))+
  ylim(0,.2)
p + scale_fill_manual(values=c("#37b3f9", "#e39010", "#13a558")) + theme_classic()

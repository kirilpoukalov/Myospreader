library(ggplot2)
df<-data.frame(AI14RTPCR_cas)
df$Treatment<- factor(df$Treatment, levels=c("PBS", "2xSV40", "Myospreader"))
df$Muscle<- factor(df$Muscle, levels=c("TA", "Gastroc", "Quad", "Tricep"))
p<-ggplot(df, aes(x=Muscle, y=Gene.Expression.Ratio, fill=Treatment)) +
  geom_dotplot(binaxis='y', stackdir='center',
               position=position_dodge(.5), dotsize = .90)+
ylim(0,3.81)
p + scale_fill_manual(values=c("#37b3f9", "#e39010", "#13a558")) + theme_classic()

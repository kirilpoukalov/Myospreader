library(ggplot2)
df<-data.frame(AI14_RTPCR)
df$Treatment<- factor(df$Treatment, levels=c("Myospreader", "2xSV40", "PBS"))
df$Muscle<- factor(df$Muscle, levels=c("TA", "Gastroc", "Quad", "Tricep"))
p<-ggplot(df, aes(x=Muscle, y=Gene.Expression.Ratio, fill=Treatment)) +
  geom_dotplot(binaxis='y', stackdir='center',
               position=position_dodge(.5))
  theme_classic()
p + scale_fill_brewer(palette="Dark2") + theme_minimal()

library(ggplot2)
df<-data.frame(WesternData_saCas9) 
df$Treatment<- factor(df$Treatment, levels=c("PBS", "2xSV40", "Myospreader"))
df$Muscle<- factor(df$Muscle, levels=c("Gastroc", "Quad", "Tricep"))
p<-ggplot(df, aes(x=Muscle, y=Cas9, fill= Treatment)) + 
  geom_dotplot(binaxis='y', stackdir='center',
               position=position_dodge(.5))+
  ylim(0,7)
p + scale_fill_manual(values=c("#37b3f9", "#e39010", "#13a558")) + theme_classic()

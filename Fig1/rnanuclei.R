library(ggplot2)
df<-data.frame(gfprnanucleiratioR)
ggplot(df, aes(x=virus, y=percent)) +
  geom_dotplot(binaxis='y', stackdir='center', position=position_dodge(.75))+
  ylim(0,0.3)+
  scale_fill_manual(values=c("#37b3f9")) + theme_classic()

library(ggplot2)
p<-ggplot(df, aes(x=virus, y=pecent)) + 
  geom_dotplot(binaxis='y', stackdir='center', fill="magenta")+
  ylim(0,0.3)+
  theme_classic()
p
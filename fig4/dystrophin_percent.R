library(rstatix)
df<-data.frame(Dystrophin_data) 
Fibers_list<-c(x1=c(unique(df$Fiber)))
treatment<-c()
percent<-c()
fibers<-c()

for (i in Fibers_list) {
  signalau<-c()
  subset<-subset(df, subset = Fiber == i)
  signalau<-append(signalau,subset$Gray_Value)
  quantile<-quantile(signalau, .1) 
  names(quantile) <- NULL
  signalau<-signalau-quantile
  treatment<-append(treatment,subset[1, c("Treatment")])
  percent<-append(percent,sum(signalau > 60)/length(signalau))
  fibers<-append(fibers, i)
}
data<-data.frame(percent,treatment,fibers)
games_howell_test(data, formula=percent~treatment, conf.level = 0.95, detailed = FALSE)

library(ggplot2)
library(forcats)
data$Treatment<- factor(data$treatment, levels=c("PBS", "SV40", "Myospreader", "WT"))
p<-ggplot(data, aes(x=forcats::fct_relevel(treatment,"PBS", "SV40", "Myospreader", "WT"), y=percent, fill=treatment)) +
  geom_dotplot(binaxis='y', stackdir='center',
  position=position_dodge(.5), dotsize = 1.4)+
  ylim(0,.5)+
  stat_summary(fun=mean, geom="point", shape=23, size=.5)
p + scale_fill_manual(values=c("#13a558","#37b3f9", "#e39010", "red")) + theme_classic() + theme(legend.position="none")

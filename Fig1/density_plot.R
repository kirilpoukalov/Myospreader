library(ggplot2)
library(dplyr)
library(forcats)
df<-nuclei
fibers<-c(x1=c(unique(df$fiber)))
subset<-subset(df, subset = fiber == "myo_3")

signalau<-c()
for (i in fibers) {
  subset<-subset(df, subset = fiber == i)
  signalau<-append(signalau,subset$mean/mean(subset$mean))
}
fiberau<-data.frame("treatment"=df$treatment,
                    "fiber"=df$fiber,
                    "signalau"=signalau)
# density plot
p<-ggplot(fiberau, aes(x=signalau, color=forcats::fct_rev(reorder(treatment,treatment)))) +
  geom_density(size=6) +
  theme_classic() +
  theme(legend.position="none")+
  ylim(0,1.5)+
  scale_color_manual(values=c("#e39010","#13a558"))

p

#CDF plot
ggplot(fiberau, aes(x=signalau, color=forcats::fct_rev(reorder(treatment,treatment)))) + stat_ecdf(geom = "step", size=2)+
theme(legend.position="none")+
  scale_color_manual(values=c("#e39010","#13a558"))


#kolmogorov-smirnov
subsetmyo<-c(subset(fiberau,subset = treatment =="myo")$signalau)
subsetsv<-c(subset(fiberau,subset = treatment =="sv")$signalau)
ks.test(subsetmyo, subsetsv)
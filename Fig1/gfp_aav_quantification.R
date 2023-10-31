df<-nuclei
fibers<-c(x1=c(unique(df$fiber)))
subset<-subset(df, subset = fiber == "myo_3")
sd(subset$mean)

Covs<-c()
for (i in fibers) {
  subset<-subset(df, subset = fiber == i)
  Covs<-append(Covs,sd(subset$mean)/mean(subset$mean))
}
fibercovs<-data.frame(x1=fibers,
                    x2=Covs)
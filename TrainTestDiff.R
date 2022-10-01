#
#author: Manisha Sirsat
#department: Data Management and Risk Analysis
#organization: InnovPlantProtect, Elvas, Portugal
#website: https://iplantprotect.pt/
#

library(tidyverse)
getwd()
df<-readxl::read_xlsx("/home/DataHub/WheatGP/Analysis/TrainTestRdiff/TestTrain_diff.xlsx")
head(df)
df$Model<-factor(df$Model, c("RF_py","extraTrees_py", "GB_py", "adaboost_py", "Xgboost_py", "mlp_py", "LASSO_r","ridge_r", "elasticnet_r", "BayesA_r", "BRR_r", "BL_r"))

df %>% pivot_longer(cols=c(VT:BayesA),names_to = "FS",values_to = "Rdiff")
df<-df %>% pivot_longer(cols=c(VT:BayesA),names_to = "FS",values_to = "Rdiff")
ggplot(df,aes(x=FS,y=Rdiff))+geom_boxplot()+facet_wrap(~Dataset)
ggplot(df,aes(x=Model,y=Rdiff))+geom_boxplot()+facet_wrap(~Dataset)
ggplot(df,aes(x=Model,y=Rdiff))+geom_boxplot()+facet_wrap(~Dataset)+theme(axis.text.x = element_text(angle=90))
ggplot(df,aes(x=Model,y=Rdiff))+geom_boxplot()+facet_wrap(~Dataset)+theme(axis.text.x = element_text(angle=90))+geom_rect(aes(xmin=-Inf,xmax=Inf, ymin=0, ymax=Inf),fill="yellow")
ggplot(df,aes(x=Model,y=Rdiff))+geom_rect(aes(xmin=-Inf,xmax=Inf, ymin=0, ymax=Inf),fill="yellow")+geom_boxplot()+facet_wrap(~Dataset)+theme(axis.text.x = element_text(angle=90))
ggplot(df,aes(x=Model,y=Rdiff))+geom_rect(aes(xmin=-Inf,xmax=Inf, ymin=0, ymax=Inf),fill="lightred",alpha=0.5)+geom_boxplot()+facet_wrap(~Dataset)+theme(axis.text.x = element_text(angle=90))
ggplot(df,aes(x=Model,y=Rdiff))+geom_rect(aes(xmin=-Inf,xmax=Inf, ymin=0, ymax=Inf),fill="red",alpha=0.5)+geom_boxplot()+facet_wrap(~Dataset)+theme(axis.text.x = element_text(angle=90))
ggplot(df,aes(x=Model,y=Rdiff))+geom_rect(aes(xmin=-Inf,xmax=Inf, ymin=0, ymax=Inf),fill="red",alpha=0.8)+geom_boxplot()+facet_wrap(~Dataset)+theme(axis.text.x = element_text(angle=90))
?geom_rect
ggplot(df,aes(x=Model,y=Rdiff))+geom_tile(aes(xmin=-Inf,xmax=Inf, ymin=0, ymax=Inf),fill="red",alpha=0.8)+geom_boxplot()+facet_wrap(~Dataset)+theme(axis.text.x = element_text(angle=90))
ggplot(df,aes(x=Model,y=Rdiff))+annotate("rect", xmin=-Inf,xmax=Inf, ymin=0, ymax=Inf, alpha=0.2, fill="red")+geom_boxplot()+facet_wrap(~Dataset)+theme(axis.text.x = element_text(angle=90))
ggplot(df,aes(x=Model,y=Rdiff))+annotate("rect", xmin=-Inf,xmax=Inf, ymin=0, ymax=Inf, alpha=0.2, fill="red")+annotate("rect", xmin=-Inf,xmax=Inf, ymin=-Inf, ymax=0, alpha=0.2, fill="green")+geom_boxplot()+facet_wrap(~Dataset)+theme(axis.text.x = element_text(angle=90))
ggplot(df,aes(x=Model,y=Rdiff))+annotate("rect", xmin=-Inf,xmax=Inf, ymin=0, ymax=Inf, alpha=0.2, fill="red")+annotate("rect", xmin=-Inf,xmax=Inf, ymin=-Inf, ymax=0, alpha=0.2, fill="green")+geom_boxplot()+facet_wrap(~Dataset)+theme(axis.text.x = element_text(angle=90))+theme_classic()
ggplot(df,aes(x=Model,y=Rdiff))+annotate("rect", xmin=-Inf,xmax=Inf, ymin=0, ymax=Inf, alpha=0.2, fill="red")+annotate("rect", xmin=-Inf,xmax=Inf, ymin=-Inf, ymax=0, alpha=0.2, fill="green")+geom_boxplot()+facet_wrap(~Dataset)+theme_bw()+theme(axis.text.x = element_text(angle=90))
ggplot(df,aes(x=FS,y=Rdiff))+annotate("rect", xmin=-Inf,xmax=Inf, ymin=0, ymax=Inf, alpha=0.2, fill="red")+annotate("rect", xmin=-Inf,xmax=Inf, ymin=-Inf, ymax=0, alpha=0.2, fill="green")+geom_boxplot()+facet_wrap(~Dataset)+theme_bw()+theme(axis.text.x = element_text(angle=90))
min(df$Rdiff)
max(df$Rdiff)
View(df)
df %>% filter(Rdiff<=0.05 && Rdiff>=-0.05)
df %>% filter(Rdiff>=-0.05)
df %>% filter(Rdiff>=-0.05 && Rdiff<=0.05)
df %>% filter(Rdiff>=-0.05) %>% filter(Rdiff<=0.05)
df %>% filter(Rdiff>=-0.05) %>% filter(Rdiff<=0.05) %>% group_by(Model,Dataset) %>% summarize(n())
df %>% filter(Rdiff>=-0.05) %>% filter(Rdiff<=0.05) %>% group_by(Model,Dataset) %>% summarize(n()) %>% View()
df %>% filter(Rdiff>=-0.05) %>% filter(Rdiff<=0.05) %>% group_by(Model) %>% summarize(n()) %>% View()
df$FS <- factor(df$FS, c("VT","MI","Corr_Matrix","BayesA"))
ggplot(df,aes(x=FS,y=Rdiff))+annotate("rect", xmin=-Inf,xmax=Inf, ymin=0, ymax=Inf, alpha=0.2, fill="red")+annotate("rect", xmin=-Inf,xmax=Inf, ymin=-Inf, ymax=0, alpha=0.2, fill="green")+geom_boxplot()+facet_wrap(~Dataset)+theme_bw()+theme(axis.text.x = element_text(angle=90))+ ylab("\u03B4R")
ggplot(df,aes(x=Model,y=Rdiff))+annotate("rect", xmin=-Inf,xmax=Inf, ymin=0, ymax=Inf, alpha=0.2, fill="red")+annotate("rect", xmin=-Inf,xmax=Inf, ymin=-Inf, ymax=0, alpha=0.2, fill="green")+geom_boxplot()+facet_wrap(~Dataset)+theme_bw()+theme(axis.text.x = element_text(angle=90))+ ylab("\u03B4R")
df %>% filter(Rdiff<-0.05) %>% filter(Rdiff>0.05) %>% group_by(Model) %>% summarize(n()) %>% View()
df %>% filter(Rdiff< -0.05) %>% filter(Rdiff>0.05) %>% group_by(Model) %>% summarize(n()) %>% View()
df %>% filter(abs(Rdiff)>0.05) %>% View()
df %>% filter(abs(Rdiff)>0.05)  %>% group_by(FS) %>% summarize(n())
df  %>% group_by(FS) %>% summarize(n())
df %>% filter(abs(Rdiff)>0.05 && Model %in% c("elasticnet", "Lasso", "Xgboost", "adaboost", "GB", "RF", "extraTrees"))  %>% group_by(FS) %>% summarize(n())
df %>% filter(abs(Rdiff)>0.05 && Model %in% c("elasticnet", "LASSO", "Xgboost", "adaboost", "GB", "RF", "extraTrees"))  %>% group_by(FS) %>% summarize(n())
df %>% filter(abs(Rdiff)>0.05 & Model %in% c("elasticnet", "LASSO", "Xgboost", "adaboost", "GB", "RF", "extraTrees"))  %>% group_by(FS) %>% summarize(n())
df %>% filter(abs(Rdiff)>0.05 & Model %in% c("elasticnet", "LASSO", "Xgboost", "adaboost", "GB", "RF", "extraTrees"))  %>% View()
method<-df %>% unique(pull(Model))
method<- unique(df$Model)
method<-as.data.frame(method)
method
type=c(rep("tree",5),"DL",rep("linear",3),rep("Bayes",3))
method$type<-type
method
df<-left_join(df,method)
Model<- unique(df$Model)
method<-as.data.frame(Model)
method$type<-type
method
df<-left_join(df,method)
df %>% filter(abs(Rdiff)>0.05 & Model %in% c("elasticnet", "LASSO", "Xgboost", "adaboost", "GB", "RF", "extraTrees"))  %>% group_by(FS,type) %>% summarize(n())
method
df %>% filter(abs(Rdiff)>0.05 & Model %in% c("elasticnet", "LASSO", "Xgboost", "adaboost", "GB", "RF", "extraTrees"))  %>% group_by(Dataset,type) %>% summarize(n())
df %>% filter(abs(Rdiff)>0.05 & Model %in% c("elasticnet", "LASSO", "Xgboost", "adaboost", "GB", "RF", "extraTrees"))  %>% View()
df %>% filter(abs(Rdiff)<=0.05) %>% group_by(Model) %>% summarize(n())
df %>% filter(abs(Rdiff)<=0.05) %>% group_by(Model) %>% summarize(count=n()) %>% arrange(-count)

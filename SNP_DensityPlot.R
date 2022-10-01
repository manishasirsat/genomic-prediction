#
#author: Manisha Sirsat
#department: Data Management and Risk Analysis
#organization: InnovPlantProtect, Elvas, Portugal
#website: https://iplantprotect.pt/
#

#setting the directory
path<- '/home/DataHub/WheatGP/Analysis/SNP_DensityPlot/'
setwd(path)

library("CMplot")

#reading features by VT_loc1
VT_loc1<- read.csv('Loc1/VT_Loc1.csv', sep = ',')
class(VT_loc1)

CMplot(VT_loc1,type="p",plot.type="d",bin.size=1e6,chr.den.col=c("darkgreen", "yellow", "red"),file="jpg",memo="SNP_Density_VT_loc1",dpi=300,
       main="",file.output=TRUE,verbose=TRUE,width=9,height=6,  bin.range=c(1, 10))

#reading features by MI_loc1
MI_loc1<- read.csv('Loc1/MI_Loc1.csv', sep = ',')

CMplot(MI_loc1,type="p",plot.type="d",bin.size=1e6,chr.den.col=c("darkgreen", "yellow", "red"),file="jpg",memo="SNP_Density_MI_loc1",dpi=300,
       main="",file.output=TRUE,verbose=TRUE,width=9,height=6,  bin.range=c(1, 10))

#reading features by Corr_Matrix_loc1
Corr_Matrix_loc1<- read.csv('Loc1/Corr_Matrix_Loc1.csv', sep = ',')

CMplot(Corr_Matrix_loc1,type="p",plot.type="d",bin.size=1e6,chr.den.col=c("darkgreen", "yellow", "red"),file="jpg",memo="SNP_Density_CorrMatrix_loc1",dpi=300,
       main="",file.output=TRUE,verbose=TRUE,width=9,height=6,  bin.range=c(1, 10))

#reading features by BayesA_loc
BayesA_loc1<- read.csv('Loc1/BayesA_Loc1.csv', sep = ',')

CMplot(BayesA_loc1,type="p",plot.type="d",bin.size=1e6,chr.den.col=c("darkgreen", "yellow", "red"),file="jpg",memo="SNP_Density_BayesA_loc1",dpi=300,
       main="",file.output=TRUE,verbose=TRUE,width=9,height=6,  bin.range=c(1, 10))

#reading features by VT_loc2
VT_loc2<- read.csv('Loc2/VT_Loc2.csv', sep = ',')
class(VT_loc2)

CMplot(VT_loc2,type="p",plot.type="d",bin.size=1e6,chr.den.col=c("darkgreen", "yellow", "red"),file="jpg",memo="SNP_Density_VT_loc2",dpi=300,
       main="",file.output=TRUE,verbose=TRUE,width=9,height=6,  bin.range=c(1, 10))

#reading features by MI_loc2
MI_loc2<- read.csv('Loc2/MI_Loc2.csv', sep = ',')

CMplot(MI_loc2,type="p",plot.type="d",bin.size=1e6,chr.den.col=c("darkgreen", "yellow", "red"),file="jpg",memo="SNP_Density_MI_loc2",dpi=300,
       main="",file.output=TRUE,verbose=TRUE,width=9,height=6,  bin.range=c(1, 10))

#reading features by Corr_Matrix_loc2
Corr_Matrix_loc2<- read.csv('Loc2/Corr_Matrix_Loc2.csv', sep = ',')

CMplot(Corr_Matrix_loc2,type="p",plot.type="d",bin.size=1e6,chr.den.col=c("darkgreen", "yellow", "red"),file="jpg",memo="SNP_Density_CorrMatrix_loc2",dpi=300,
       main="",file.output=TRUE,verbose=TRUE,width=9,height=6, bin.range=c(1, 10))

#reading features by BayesA_loc
BayesA_loc2<- read.csv('Loc2/BayesA_Loc2.csv', sep = ',')

CMplot(BayesA_loc2,type="p",plot.type="d",bin.size=1e6,chr.den.col=c("darkgreen", "yellow", "red"),file="jpg",memo="SNP_Density_BayesA_loc2",dpi=300,
       main="",file.output=TRUE,verbose=TRUE,width=9,height=6,  bin.range=c(1, 10))


#reading features by VT_loc3
VT_loc3<- read.csv('Loc3/VT_Loc3.csv', sep = ',')
class(VT_loc3)

CMplot(VT_loc3,type="p",plot.type="d",bin.size=1e6,chr.den.col=c("darkgreen", "yellow", "red"),file="jpg",memo="SNP_Density_VT_loc3",dpi=300,
       main="",file.output=TRUE,verbose=TRUE,width=9,height=6,  bin.range=c(1, 10))

#reading features by MI_loc3
MI_loc3<- read.csv('Loc3/MI_Loc3.csv', sep = ',')

CMplot(MI_loc3,type="p",plot.type="d",bin.size=1e6,chr.den.col=c("darkgreen", "yellow", "red"),file="jpg",memo="SNP_Density_MI_loc3",dpi=300,
       main="",file.output=TRUE,verbose=TRUE,width=9,height=6,  bin.range=c(1, 10))

#reading features by Corr_Matrix_loc3
Corr_Matrix_loc3<- read.csv('Loc3/Corr_Matrix_Loc3.csv', sep = ',')

CMplot(Corr_Matrix_loc3,type="p",plot.type="d",bin.size=1e6,chr.den.col=c("darkgreen", "yellow", "red"),file="jpg",memo="SNP_Density_CorrMatrix_loc3",dpi=300,
       main="",file.output=TRUE,verbose=TRUE,width=9,height=6,  bin.range=c(1, 10))

#reading features by BayesA_loc
BayesA_loc3<- read.csv('Loc3/BayesA_Loc3.csv', sep = ',')

CMplot(BayesA_loc3,type="p",plot.type="d",bin.size=1e6,chr.den.col=c("darkgreen", "yellow", "red"),file="jpg",memo="SNP_Density_BayesA_loc3",dpi=300,
       main="",file.output=TRUE,verbose=TRUE,width=9,height=6,  bin.range=c(1, 10))


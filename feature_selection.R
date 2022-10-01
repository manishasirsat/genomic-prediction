#
#author: Manisha Sirsat
#department: Data Management and Risk Analysis
#organization: InnovPlantProtect, Elvas, Portugal
#website: https://iplantprotect.pt/
#

#first let’s get all libraries in place.
source('library.R')

fs_BayesA <- function(X_train, X_test, loc, FSMethod, y_train, n_features) {
  FSMethod ='BayesA'
  
  #converting to matrix
  X_train <- as.matrix(X_train)
  y_train <- as.matrix(y_train)
  
  #feature Selection: Use BayesA from BGLR package to select features with largest abs(coefficients) ####################
  ETA<-list(list(X=X_train, model='BayesA'))
  fm<-BGLR(y=y_train,ETA=ETA,verbose=FALSE, nIter=5000,burnIn=1000)
  coef <- abs(fm$ETA[[1]]$b)
  coef_df <- as.data.frame(coef)
  plot(abs(coef),col=4,cex=.5, type='o', main='Features selection with largest abs(coefficients) using BayesA', xlab = 'Marker position')
  dev.off()
  coefs <- cbind(snps = rownames(coef_df), coef_df)
  coef_desc <- coefs[order(coefs$coef, decreasing = TRUE), ]
  top_features<- head(coef_desc, n_features)
  print(top_features)
  write.table(data_frame(top_features$snps), file= sprintf('Results/FeatureLists/FeatureList_BayesA_%s.txt', loc), sep=',', row.names = TRUE, quote=FALSE)

  #converting in data frames
  X_train <- as.data.frame(X_train)

  #transforming the selected features for train and test set
  X_train<- X_train[rownames(top_features)]
  X_test<- X_test[rownames(top_features)]
  
  #removing the following files
  file.remove('varE.dat')
  file.remove('mu.dat')
  file.remove('ETA_1_ScaleBayesA.dat')
  
  return(list(X_train, X_test, loc, FSMethod))
}


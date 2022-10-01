#
#author: Manisha Sirsat
#department: Data Management and Risk Analysis
#organization: InnovPlantProtect, Elvas, Portugal
#website: https://iplantprotect.pt/
#

#setting the directory 
path= '/home/DataHub/WheatGP'
setwd(path)

#first let’s get all libraries in place.
source('library.R')

manual_pearson <- function(testOutput, lev=NULL, model=NULL) {
  a <- testOutput$pred 
  b <- testOutput$obs 
  r=cor(a, b, method = c('pearson'))
  names(r) <- c('manual_pearson')
  r
}

#defining parameter grids
stats_methods <- function(X_train, y_train, X_test, y_test, loc, FSMethod) {
  #converting to matrix
  X_train <- as.matrix(X_train)
  y_train <- as.matrix(y_train)
  X_test <- as.matrix(X_test)
  y_test <- as.matrix(y_test)
  
  if (FSMethod == 'VT' & loc == 'Loc1') {
    bayesian_param_grid <- list(data.frame(nIter=10000, burnIn=3000),
                                data.frame(nIter=10000, burnIn=3000),
                                data.frame(nIter=10000, burnIn=3000))
    penalized_param_grid <- list(data.frame(alpha = 1,
                                            lambda = seq(0.0001, 0.20, length = 10)),
                                 data.frame(alpha = 0,
                                            lambda = seq(0.0001, 1, length = 10)),
                                 data.frame(alpha = 0:1,
                                            lambda = seq(0.0001, 0.20, length = 10))
    )
    penalized_methods(X_train, y_train, X_test, y_test, loc, FSMethod, penalized_param_grid)
    bayesian_methods(X_train, y_train, X_test, y_test, loc, FSMethod, bayesian_param_grid)
  } 
  if (FSMethod == 'MI' & loc == 'Loc1') {
    bayesian_param_grid <- list(data.frame(nIter=10000, burnIn=3000),
                                data.frame(nIter=10000, burnIn=3000),
                                data.frame(nIter=10000, burnIn=3000))
    penalized_param_grid <- list(data.frame(alpha = 1,
                                            lambda = seq(0.0001, 0.20, length = 10)),
                                 data.frame(alpha = 0,
                                            lambda = seq(0.0001, 1, length = 10)),
                                 data.frame(alpha = 0.5,
                                            lambda = seq(0.0001, 0.50, length = 10))
    )
    penalized_methods(X_train, y_train, X_test, y_test, loc, FSMethod, penalized_param_grid)
    bayesian_methods(X_train, y_train, X_test, y_test, loc, FSMethod, bayesian_param_grid)
  }
  
  if (FSMethod == 'Corr_Matrix' & loc == 'Loc1') {
    bayesian_param_grid <- list(data.frame(nIter=10000, burnIn=3000),
                                data.frame(nIter=10000, burnIn=3000),
                                data.frame(nIter=10000, burnIn=3000))
    penalized_param_grid <- list(data.frame(alpha = 1,
                                            lambda = seq(0.0001, 0.20, length = 10)),
                                 data.frame(alpha = 0,
                                            lambda = seq(0.0001, 1, length = 10)),
                                 data.frame(alpha = 0.5,
                                            lambda = seq(0.0001, 0.59, length = 10))
    )
    penalized_methods(X_train, y_train, X_test, y_test, loc, FSMethod, penalized_param_grid)
    bayesian_methods(X_train, y_train, X_test, y_test, loc, FSMethod, bayesian_param_grid)
  }
  
  if (FSMethod == 'BayesA' & loc == 'Loc1') {
    bayesian_param_grid <- list(data.frame(nIter=10000, burnIn=3000),
                                data.frame(nIter=10000, burnIn=3000),
                                data.frame(nIter=10000, burnIn=3000))
    penalized_param_grid <- list(data.frame(alpha = 1,
                                            lambda = seq(0.0001, 0.22, length = 10)),
                                 data.frame(alpha = 0,
                                            lambda = seq(0.0001, 1, length = 10)),
                                 data.frame(alpha = 0:1,
                                            lambda = seq(0.0001, 0.20, length = 10))
    )
    penalized_methods(X_train, y_train, X_test, y_test, loc, FSMethod, penalized_param_grid)
    bayesian_methods(X_train, y_train, X_test, y_test, loc, FSMethod, bayesian_param_grid)
  }
  
  if (FSMethod == 'VT' & loc == 'Loc2') {
    bayesian_param_grid <- list(data.frame(nIter=9000, burnIn=3000),
                                data.frame(nIter=9000, burnIn=3000),
                                data.frame(nIter=9000, burnIn=3000))
    penalized_param_grid <- list(data.frame(alpha = 1,
                                            lambda = seq(0.0001, 0.22, length = 10)),
                                 data.frame(alpha = 0,
                                            lambda = seq(0.0001, 1, length = 10)),
                                 data.frame(alpha = 0:1,
                                            lambda = seq(0.0001, 0.29, length = 10))
    )
    penalized_methods(X_train, y_train, X_test, y_test, loc, FSMethod, penalized_param_grid)
    bayesian_methods(X_train, y_train, X_test, y_test, loc, FSMethod, bayesian_param_grid)
  } 
  if (FSMethod == 'MI' & loc == 'Loc2') {
    bayesian_param_grid <- list(data.frame(nIter=9000, burnIn=3000),
                                data.frame(nIter=9000, burnIn=3000),
                                data.frame(nIter=9000, burnIn=3000))
    penalized_param_grid <- list(data.frame(alpha = 1,
                                            lambda = seq(0.0001, 0.88, length = 10)),
                                 data.frame(alpha = 0,
                                            lambda = seq(0.0001, 1, length = 10)),
                                 data.frame(alpha = 0.5,
                                            lambda = seq(0.0001, 1, length = 10))
    )
    penalized_methods(X_train, y_train, X_test, y_test, loc, FSMethod, penalized_param_grid)
    bayesian_methods(X_train, y_train, X_test, y_test, loc, FSMethod, bayesian_param_grid)
  }
  
  if (FSMethod == 'Corr_Matrix' & loc == 'Loc2') {
    bayesian_param_grid <- list(data.frame(nIter=9000, burnIn=3000),
                                data.frame(nIter=9000, burnIn=3000),
                                data.frame(nIter=9000, burnIn=3000))
    penalized_param_grid <- list(data.frame(alpha = 1,
                                            lambda = seq(0.0001, 0.88, length = 10)),
                                 data.frame(alpha = 0,
                                            lambda = seq(0.0001, 1, length = 10)),
                                 data.frame(alpha = 0.5,
                                            lambda = seq(0.0001, 1, length = 10))
    )
    penalized_methods(X_train, y_train, X_test, y_test, loc, FSMethod, penalized_param_grid)
    bayesian_methods(X_train, y_train, X_test, y_test, loc, FSMethod, bayesian_param_grid)
  }
  
  if (FSMethod == 'BayesA' & loc == 'Loc2') {
    bayesian_param_grid <- list(data.frame(nIter=9000, burnIn=3000),
                                data.frame(nIter=9000, burnIn=3000),
                                data.frame(nIter=9000, burnIn=3000))
    penalized_param_grid <- list(data.frame(alpha = 1,
                                            lambda = seq(0.0001, 1, length = 10)),
                                 data.frame(alpha = 0,
                                            lambda = seq(0.0001, 2, length = 10)),
                                 data.frame(alpha = 0:1,
                                            lambda = seq(0.0001, 0.77, length = 10))
    )
    penalized_methods(X_train, y_train, X_test, y_test, loc, FSMethod, penalized_param_grid)
    bayesian_methods(X_train, y_train, X_test, y_test, loc, FSMethod, bayesian_param_grid)
  }
  
  if (FSMethod == 'VT' & loc == 'Loc3') {
    bayesian_param_grid <- list(data.frame(nIter=8000, burnIn=3000),
                                data.frame(nIter=8000, burnIn=3000),
                                data.frame(nIter=8000, burnIn=3000))
    penalized_param_grid <- list(data.frame(alpha = 1,
                                            lambda = seq(0.0001, 0.44, length = 10)),
                                 data.frame(alpha = 0,
                                            lambda = seq(0.0001, 1, length = 10)),
                                 data.frame(alpha = 0:1,
                                            lambda = seq(0.0001, 0.33, length = 10))
    )
    penalized_methods(X_train, y_train, X_test, y_test, loc, FSMethod, penalized_param_grid)
    bayesian_methods(X_train, y_train, X_test, y_test, loc, FSMethod, bayesian_param_grid)
  } 
  if (FSMethod == 'MI' & loc == 'Loc3') {
    bayesian_param_grid <- list(data.frame(nIter=8000, burnIn=3000),
                                data.frame(nIter=8000, burnIn=3000),
                                data.frame(nIter=8000, burnIn=3000))
    penalized_param_grid <- list(data.frame(alpha = 1,
                                            lambda = seq(0.0001, 0.44, length = 10)),
                                 data.frame(alpha = 0,
                                            lambda = seq(0.0001, 1, length = 10)),
                                 data.frame(alpha = 0.5,
                                            lambda = seq(0.0001, 0.88, length = 10))
    )
    penalized_methods(X_train, y_train, X_test, y_test, loc, FSMethod, penalized_param_grid)
    bayesian_methods(X_train, y_train, X_test, y_test, loc, FSMethod, bayesian_param_grid)
  }
  
  if (FSMethod == 'Corr_Matrix' & loc == 'Loc3') {
    bayesian_param_grid <- list(data.frame(nIter=8000, burnIn=3000),
                                data.frame(nIter=8000, burnIn=3000),
                                data.frame(nIter=8000, burnIn=3000))
    penalized_param_grid <- list(data.frame(alpha = 1,
                                            lambda = seq(0.0001, 0.30, length = 10)),
                                 data.frame(alpha = 0,
                                            lambda = seq(0.0001, 1, length = 10)),
                                 data.frame(alpha = 0.5,
                                            lambda = seq(0.0001, 1, length = 10))
    )
    penalized_methods(X_train, y_train, X_test, y_test, loc, FSMethod, penalized_param_grid)
    bayesian_methods(X_train, y_train, X_test, y_test, loc, FSMethod, bayesian_param_grid)
  }
  
  if (FSMethod == 'BayesA' & loc == 'Loc3') {
    bayesian_param_grid <- list(data.frame(nIter=8000, burnIn=3000),
                                data.frame(nIter=8000, burnIn=3000),
                                data.frame(nIter=8000, burnIn=3000))
    penalized_param_grid <- list(data.frame(alpha = 1,
                                            lambda = seq(0.0001, 0.30, length = 10)),
                                 data.frame(alpha = 0,
                                            lambda = seq(0.0001, 1, length = 10)),
                                 data.frame(alpha = 0:1,
                                            lambda = seq(0.0001, 0.33, length = 10))
    )
    penalized_methods(X_train, y_train, X_test, y_test, loc, FSMethod, penalized_param_grid)
    bayesian_methods(X_train, y_train, X_test, y_test, loc, FSMethod, bayesian_param_grid)
  }
}

#defining a function for implementing the BayesA, bayesian ridge regression, and bayesian	 lasso methods
bayesian_methods <- function(X_train, y_train, X_test, y_test, loc, FSMethod, bayesian_param_grid) {
  
  models <- c('BayesA', 'BRR', 'BL')
  ctrl <- 1
  for (i in models) {
    model<-i
    directory <- sprintf('Results/bayesianSaveEffects/%s_%s_%s', model, FSMethod, loc)
    if (file.exists(directory)) {
      cat("The directory already exists")
    } else {
      dir.create(sprintf('Results/bayesianSaveEffects/%s_%s_%s', model, FSMethod, loc))}
    #setting the temp working directory
    setwd(directory)
    #setting seed for the random number generator
    set.seed(13)      #setting seed for the random number generator
    folds<-4
    nIter<-bayesian_param_grid[[ctrl]]$nIter; burnIn=bayesian_param_grid[[ctrl]]$burnIn
    y<-y_train
    sets<-rep(1:10,60)[-1]
    sets<-sets[order(runif(nrow(X_train)))]
    cor.cv<-rep(NA,times=(folds+1))
    names(cor.cv)<-c(paste('fold=',1:folds,sep=''),'Pooled')
    w<-rep(1/nrow(X_train),folds) ## weights for pooled correlations and MSE
    yHatCV<-numeric()

    for(fold in 1:folds)
    {
      print(paste('fold =',fold))
      test<-which(sets==1)
      yNa<-y
      yNa[test]<-NA                   #masking grain yields for validation set
      prefix<-paste('PM_%s',model,'_fold_',fold,'_',sep='')
      set.seed(13)     #setting seed for the random number generator
      fmBayes<-BGLR(y=yNa,ETA=list(list(X=X_train, model=model, saveEffects=TRUE)), nIter=nIter, burnIn=burnIn, thin = 2, saveAt=sprintf('%s_', model))
      yHatCV[test]<-fmBayes$yHat[test]
      w[fold]<-w[fold]*length(fmBayes$test)
      cor.cv[fold]<-cor(fmBayes$yHat[test], y[test])
      }
    
    cor.cv[5]<-mean(cor.cv[1:4])
    
    #calculating an accuracy using R-squared function
    R2 = function(y_test, yHat){
      cor(y_test, yHat)^2
    }
    #scoring metrics on train set
    train_pcc <- cor.cv[5]
    train_mse <- mean((y_train - fmBayes$yHat)^2)
    train_R2 <- R2(y_train, fmBayes$yHat)
    
    #goodness of fit and related statistics 
    fmBayes$fit
    fmBayes$varE
    
    #setting the main working directory
    setwd('/home/DataHub/WheatGP')
    
    #residual variance
    varE<-scan(file=sprintf('Results/bayesianSaveEffects/%s_%s_%s/%s_varE.dat', model, FSMethod, loc, model))
    plot(varE,type='o',col=2,cex=.5,
         ylab=expression(sigma[epsilon]^2),
         xlab='Sample',main=paste('Residual Variance:', model));
    abline(h=fmBayes$varE,col=4,lwd=2);
    abline(v=fmBayes$burnIn/fmBayes$thin,col=4)
    
    #scoring metrics on test set
    yHatBayes<-X_test%*%fmBayes$ETA[[1]]$b
    test_pcc <- cor(y_test, yHatBayes)
    test_R2 <- R2(y_test, yHatBayes)
    
    yHatBayes<- as.data.frame(yHatBayes)
    names(yHatBayes)[1] <- 'Yield'

    #saving prediction plot
    tmp<-range(c(y_test,yHatBayes))
    png(filename=sprintf('Results/Figures/%s_%s_%s.png', model, FSMethod, loc ))
    #dev.new(width=10, height=10, unit="in")
    plot(yHatBayes$Yield~y_test,xlab='Actual values',ylab='Predicted values', col ='#0073C2FF', pch=19, lty=2, cex=1.5, main=paste('Actual and predicted grain yield by', model, 'and FS:', FSMethod, 'on', loc), 
         xlim=tmp, ylim=tmp); abline(a=0,b=1,col=4,lwd=2)
    dev.off()
    
    #creating a data frame of the actual and predicted yield values
    #output= data.frame(y_test, yHatBayes) 
    
    #rounding the result values
    train_pcc<-round(train_pcc, 3)
    test_pcc<-round(test_pcc, 3)
    
    #saving the results
    res <- c ('\ntrain_pcc, test_pcc:', model, train_pcc, test_pcc)
    write.table(res, file=sprintf('Results/ModelResults/Results_%s_%s.csv', FSMethod, loc), append=TRUE, quote=F, row.names = FALSE)
  }
}

#defining a function for implementing the lasso, ridge and elasticnet methods
penalized_methods <- function(X_train, y_train, X_test, y_test, loc, FSMethod, penalized_param_grid) {
  models <- c('lasso', 'ridge', 'elasticnet')
  ctrl <- 1
  for (i in models) { 
    model<-i
    set.seed(17) #setting seed for the random number generator
    trainCtrl <- caret::trainControl(method = 'cv', 
                                     number = 4,
                                     savePredictions = TRUE,
                                     returnResamp = 'all', # save losses across all models
                                     classProbs = FALSE,
                                     summaryFunction = manual_pearson
    )
    
    y_train<-data.frame(y_train)
    X_train <- data.frame(X_train) 
    X_train['Yield']<- y_train['Yield']
    
    #fitting the model
    set.seed(42)    #setting seed for the random number generator
    penalized_model <- caret::train(Yield ~., 
                                    data=X_train, 
                                    method = 'glmnet',
                                    metric = 'manual_pearson',
                                    trControl = trainCtrl,
                                    tuneGrid = penalized_param_grid[[ctrl]])
    
    #checking the model summary
    penalized_model 
    
    #plotting the model across all of the tuning parameters
    plot(penalized_model)
    
    #best tuning parameter (alpha, lambda)
    penalized_model$bestTune$lambda
    
    #scoring metrics on train set
    train_pcc <- mean(penalized_model$results$manual_pearson)
    
    #predicting the model on the test dataset
    y_pred <- predict(penalized_model, data.frame(X_test))
    
    #calculating an accuracy using R-squared function
    R2 = function(y_test, penalized_model_pred){
      cor(y_test, y_pred)^2
    }
    
    #scoring metrics on test set
    test_pcc <- cor(y_test, y_pred)
    test_R2 <- R2(y_test, y_pred)
    
    #saving prediction plot
    tmp<-range(c(y_test,y_pred))
    png(filename=sprintf('Results/Figures/%s_%s_%s.png', model, FSMethod, loc ))
    #dev.new(width=10, height=10, unit="in")
    plot(y_pred~y_test,xlab='Actual values',ylab='Predicted values', col ='#0073C2FF', pch=19, lty=2, cex=1.5, main=paste('Actual and predicted grain yield by', model, 'and FS:', FSMethod, 'on', loc), 
         xlim=tmp, ylim=tmp); abline(a=0,b=1,col=4,lwd=2)
    dev.off()
    
    #saving predicted Y
    output= data.frame(y_test, round(y_pred,2))     
    #write.table(output, file='Result/BayesA_Output.dat', sep=',', row.names=T, quote=F)
    
    #saving the results
    res_param <- c ('\nmodel name and its parameters:\n', model, penalized_model$bestTune$lambda)
    write.table(res_param, file=sprintf('Results/HyperParameters/BestParameter_%s_%s.csv', FSMethod, loc), append=TRUE, quote=F, row.names = FALSE)
    
    #rounding the result values
    train_pcc<-round(train_pcc, 3)
    test_pcc<-round(test_pcc, 3)
    
    #saving the results
    res_result <- c ('\ntrain_pcc, test_pcc:', model, train_pcc, test_pcc)
    write.table(res_result, file=sprintf('Results/ModelResults/Results_%s_%s.csv', FSMethod, loc), append=TRUE, quote=F, row.names = FALSE)
    print(train_pcc)
    
    #incrementing the counter  
    ctrl<-ctrl+1
  }
}
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Manisha Sirsat
@department: Data Management and Risk Analysis
@organization: InnovPlantProtect, Elvas, Portugal
@website: https://iplantprotect.pt/

"""

import os
os. chdir("/home/DataHub/WheatGP")

import warnings
warnings.filterwarnings("ignore")

#First let’s get all libraries in place.
from library import *
from rpy2.robjects import pandas2ri
pandas2ri.activate()

#importing learning functions
from ml_dl_methods import *


###### Modelling location_1 (PUL17_F5) dataset ################################################
#calling one of the following feature selection functions
##first FS method is Variance Threshold (VT)
##second FS method is mutual information (MI)
##third FS method is Correlation Matric (Corr_Matrix)

# 1. Feature selection using VT ##############
#importing the data preprocessing function from location 1
from preprocess_loc1 import *
#calling data processing function
preprocess_loc1=preprocess_loc1()
#receiving function returns into variables
X_train = preprocess_loc1[0]
X_test = preprocess_loc1[1]
y_train = preprocess_loc1[2]
y_test =  preprocess_loc1[3]
loc = preprocess_loc1[4]
X_corr = preprocess_loc1[5]
#importing feature selection functions
from feature_selection import *
#setting null string in variable FSMethod 
FSMethod=''
FuncReturn = fs_vt(X_train, X_test, loc, FSMethod, thold=0.75)
#receiving function returns into variables
X_train = FuncReturn[0]
X_test = FuncReturn[1]
loc = FuncReturn[2]
FSMethod = FuncReturn[3]
#caling all DL and ML methods to model location_1 (PUL17_F5) dataset
methods(X_train, y_train, X_test, y_test, loc, FSMethod)
#defining the R function and loading the instance in the Python
r.source('stats_methods.R')
#loading the function that is defined in R
stats_methods = robjects.globalenv['stats_methods']
#caling all stats methods to model location_1 (PUL17_F5) dataset
stats_methods(X_train, y_train, X_test, y_test, loc, FSMethod)


# 2. Feature Selection using MI ##############
#importing the data preprocessing function from location 1
from preprocess_loc1 import *
#calling data processing function
preprocess_loc1=preprocess_loc1()
#receiving function returns into variables
X_train = preprocess_loc1[0]
X_test = preprocess_loc1[1]
y_train = preprocess_loc1[2]
y_test =  preprocess_loc1[3]
loc = preprocess_loc1[4]
X_corr = preprocess_loc1[5]
#importing feature selection functions
from feature_selection import *
#setting null string in variable FSMethod 
FSMethod=''
FuncReturn = fs_mi(X_train, X_test, loc, FSMethod, y_train, pctl=10)
#receiving function returns into variables
X_train = FuncReturn[0]
X_test = FuncReturn[1]
loc = FuncReturn[2]
FSMethod = FuncReturn[3]
#caling all DL and ML methods to model location_1 (PUL17_F5) dataset
methods(X_train, y_train, X_test, y_test, loc, FSMethod)
#defining the R function and loading the instance in the Python
r.source('stats_methods.R')
#loading the function that is defined in R
stats_methods = robjects.globalenv['stats_methods']
#caling all stats methods to model location_1 (PUL17_F5) dataset
stats_methods(X_train, y_train, X_test, y_test, loc, FSMethod)




# 3. Feature Selection using Corr_Matrix ##############
#importing the data preprocessing function from location 1
from preprocess_loc1 import *
#calling data processing function
preprocess_loc1=preprocess_loc1()
#receiving function returns into variables
X_train = preprocess_loc1[0]
X_test = preprocess_loc1[1]
y_train = preprocess_loc1[2]
y_test =  preprocess_loc1[3]
loc = preprocess_loc1[4]
X_corr = preprocess_loc1[5]
#importing feature selection functions
from feature_selection import *
#setting null string in variable FSMethod 
FSMethod=''
FuncReturn = corr_matrix(X_train, X_test, loc, FSMethod, X_corr, corr_val=0.8)
#receiving function returns into variables
X_train = FuncReturn[0]
X_test = FuncReturn[1]
loc = FuncReturn[2]
FSMethod = FuncReturn[3]
#caling all DL and ML methods to model location_1 (PUL17_F5) dataset
methods(X_train, y_train, X_test, y_test, loc, FSMethod)
#defining the R function and loading the instance in the Python
r.source('stats_methods.R')
#loading the function that is defined in R
stats_methods = robjects.globalenv['stats_methods']
#caling all stats methods to model location_1 (PUL17_F5) dataset
stats_methods(X_train, y_train, X_test, y_test, loc, FSMethod)




# 4. Feature Selection using BayesA ##############
#importing the data preprocessing function from location 1
from preprocess_loc1 import *
#calling data processing function
preprocess_loc1=preprocess_loc1()
#receiving function returns into variables
X_train = preprocess_loc1[0]
X_test = preprocess_loc1[1]
y_train = preprocess_loc1[2]
y_test =  preprocess_loc1[3]
loc = preprocess_loc1[4]
X_corr = preprocess_loc1[5]
#importing feature selection functions
from feature_selection import *
#setting null string in variable FSMethod 
FSMethod=''
#defining the R function and loading the instance in the Python
r.source('./feature_selection.R')
#loading the function that is defined in R
fs_BayesA = robjects.globalenv['fs_BayesA']
FuncReturn = fs_BayesA(X_train, X_test, loc, FSMethod, y_train, n_features=5500)
#Only for fs_BayesA: receiving function returns into variables
X_train = FuncReturn[0]
X_test = FuncReturn[1]
loc = FuncReturn[2][0]
FSMethod = FuncReturn[3][0]
#caling all DL and ML methods to model location_1 (PUL17_F5) dataset
methods(X_train, y_train, X_test, y_test, loc, FSMethod)
#defining the R function and loading the instance in the Python
r.source('stats_methods.R')
#loading the function that is defined in R
stats_methods = robjects.globalenv['stats_methods']
#caling all stats methods to model location_1 (PUL17_F5) dataset
stats_methods(X_train, y_train, X_test, y_test, loc, FSMethod)



###### Modelling location_2 (PUL18_DH) dataset ######################################################
# 1. Feature Selection using VT ##############
#importing the preprocessing dataset from location 2
from preprocess_loc2 import *
#calling data processing function
preprocess_loc2=preprocess_loc2()
#receiving function returns into variables
X_train = preprocess_loc2[0]
X_test = preprocess_loc2[1]
y_train = preprocess_loc2[2]
y_test =  preprocess_loc2[3]
loc = preprocess_loc2[4]
X_corr = preprocess_loc2[5]
#importing feature selection functions
from feature_selection import *
#setting null string in variable FSMethod 
FSMethod=''
FuncReturn = fs_vt(X_train, X_test, loc, FSMethod, thold=0.80)
#Only for fs_BayesA: receiving function returns into variables
X_train = FuncReturn[0]
X_test = FuncReturn[1]
loc = FuncReturn[2]
FSMethod = FuncReturn[3]
#caling all DL and ML methods to model location_2 (PUL18_DH) dataset
methods(X_train, y_train, X_test, y_test, loc, FSMethod)
#defining the R function and loading the instance in the Python
r.source('stats_methods.R')
#loading the function that is defined in R
stats_methods = robjects.globalenv['stats_methods']
#caling all stats methods to model location_1 (PUL17_F5) dataset
stats_methods(X_train, y_train, X_test, y_test, loc, FSMethod)




# 2. Feature Selection using MI ##############
#importing the preprocessing dataset from location 2
from preprocess_loc2 import *
#calling data processing function
preprocess_loc2=preprocess_loc2()
#receiving function returns into variables
X_train = preprocess_loc2[0]
X_test = preprocess_loc2[1]
y_train = preprocess_loc2[2]
y_test =  preprocess_loc2[3]
loc = preprocess_loc2[4]
X_corr = preprocess_loc2[5]
#importing feature selection functions
from feature_selection import *
#setting null string in variable FSMethod 
FSMethod=''
FuncReturn = fs_mi(X_train, X_test, loc, FSMethod, y_train, pctl=10)
#Only for fs_BayesA: receiving function returns into variables
X_train = FuncReturn[0]
X_test = FuncReturn[1]
loc = FuncReturn[2]
FSMethod = FuncReturn[3]
#caling all DL and ML methods to model location_2 (PUL18_DH) dataset
methods(X_train, y_train, X_test, y_test, loc, FSMethod)
#defining the R function and loading the instance in the Python
r.source('stats_methods.R')
#loading the function that is defined in R
stats_methods = robjects.globalenv['stats_methods']
#caling all stats methods to model location_1 (PUL17_F5) dataset
stats_methods(X_train, y_train, X_test, y_test, loc, FSMethod)



# 3. Feature Selection using Corr_Matrix ##############
#importing the preprocessing dataset from location 2
from preprocess_loc2 import *
#calling data processing function
preprocess_loc2=preprocess_loc2()
#receiving function returns into variables
X_train = preprocess_loc2[0]
X_test = preprocess_loc2[1]
y_train = preprocess_loc2[2]
y_test =  preprocess_loc2[3]
loc = preprocess_loc2[4]
X_corr = preprocess_loc2[5]
#importing feature selection functions
from feature_selection import *
#setting null string in variable FSMethod 
FSMethod=''
FuncReturn = corr_matrix(X_train, X_test, loc, FSMethod, X_corr, corr_val=0.8)
#receiving function returns into variables
X_train = FuncReturn[0]
X_test = FuncReturn[1]
loc = FuncReturn [2]
FSMethod = FuncReturn[3]
#caling all DL and ML methods to model location_2 (PUL18_DH) dataset
methods(X_train, y_train, X_test, y_test, loc, FSMethod)
#defining the R function and loading the instance in the Python
r.source('stats_methods.R')
#loading the function that is defined in R
stats_methods = robjects.globalenv['stats_methods']
#caling all stats methods to model location_1 (PUL17_F5) dataset
stats_methods(X_train, y_train, X_test, y_test, loc, FSMethod)



# 4. Feature Selection using BayesA ##############
#importing the preprocessing dataset from location 2
from preprocess_loc2 import *
#calling data processing function
preprocess_loc2=preprocess_loc2()
#receiving function returns into variables
X_train = preprocess_loc2[0]
X_test = preprocess_loc2[1]
y_train = preprocess_loc2[2]
y_test =  preprocess_loc2[3]
loc = preprocess_loc2[4]
X_corr = preprocess_loc2[5]
#importing feature selection functions
from feature_selection import *
#setting null string in variable FSMethod 
FSMethod=''
#defining the R function and loading the instance in the Python
r.source('./feature_selection.R')
#loading the function that is defined in R
fs_BayesA = robjects.globalenv['fs_BayesA']
FuncReturn = fs_BayesA(X_train, X_test, loc, FSMethod, y_train, n_features=5500)
#Only for fs_BayesA: receiving function returns into variables
X_train = FuncReturn[0]
X_test = FuncReturn[1]
loc = FuncReturn[2][0]
FSMethod = FuncReturn[3][0]
#caling all DL and ML methods to model location_2 (PUL18_DH) dataset
methods(X_train, y_train, X_test, y_test, loc, FSMethod)
#defining the R function and loading the instance in the Python
r.source('stats_methods.R')
#loading the function that is defined in R
stats_methods = robjects.globalenv['stats_methods']
#caling all stats methods to model location_1 (PUL17_F5) dataset
stats_methods(X_train, y_train, X_test, y_test, loc, FSMethod)


###### Modelling location_3 (LND18_DH) dataset ######################################################
# 1. Feature Selection using VT ##############
#importing the preprocessing dataset from location 3
from preprocess_loc3 import *
#calling data processing function
preprocess_loc3=preprocess_loc3()
#receiving function returns into variables
X_train = preprocess_loc3[0]
X_test = preprocess_loc3[1]
y_train = preprocess_loc3[2]
y_test =  preprocess_loc3[3]
loc = preprocess_loc3[4]
X_corr = preprocess_loc3[5]
#importing feature selection functions
from feature_selection import *
#setting null string in variable FSMethod 
FSMethod=''
FuncReturn = fs_vt(X_train, X_test, loc, FSMethod, thold=0.75)
#receiving function returns into variables
X_train = FuncReturn[0]
X_test = FuncReturn[1]
loc = FuncReturn [2]
FSMethod = FuncReturn[3]
#caling all DL and ML methods to model location_3 (LND18_DH) dataset
methods(X_train, y_train, X_test, y_test, loc, FSMethod)
#defining the R function and loading the instance in the Python
r.source('stats_methods.R')
#loading the function that is defined in R
stats_methods = robjects.globalenv['stats_methods']
#caling all stats methods to model location_1 (PUL17_F5) dataset
stats_methods(X_train, y_train, X_test, y_test, loc, FSMethod)



# 2. Feature Selection using MI ##############
#importing the preprocessing dataset from location 3
from preprocess_loc3 import *
#calling data processing function
preprocess_loc3=preprocess_loc3()
#receiving function returns into variables
X_train = preprocess_loc3[0]
X_test = preprocess_loc3[1]
y_train = preprocess_loc3[2]
y_test =  preprocess_loc3[3]
loc = preprocess_loc3[4]
X_corr = preprocess_loc3[5]
#importing feature selection functions
from feature_selection import *
#setting null string in variable FSMethod 
FSMethod=''
FuncReturn = fs_mi(X_train, X_test, loc, FSMethod, y_train, pctl=10)
#receiving function returns into variables
X_train = FuncReturn[0]
X_test = FuncReturn[1]
loc = FuncReturn [2]
FSMethod = FuncReturn[3]
#caling all DL and ML methods to model location_3 (LND18_DH) dataset
methods(X_train, y_train, X_test, y_test, loc, FSMethod)
#defining the R function and loading the instance in the Python
r.source('stats_methods.R')
#loading the function that is defined in R
stats_methods = robjects.globalenv['stats_methods']
#caling all stats methods to model location_1 (PUL17_F5) dataset
stats_methods(X_train, y_train, X_test, y_test, loc, FSMethod)



# 3. Feature Selection using Corr_Matrix ##############
#importing the preprocessing dataset from location 3
from preprocess_loc3 import *
#calling data processing function
preprocess_loc3=preprocess_loc3()
#receiving function returns into variables
X_train = preprocess_loc3[0]
X_test = preprocess_loc3[1]
y_train = preprocess_loc3[2]
y_test =  preprocess_loc3[3]
loc = preprocess_loc3[4]
X_corr = preprocess_loc3[5]
#importing feature selection functions
from feature_selection import *
#setting null string in variable FSMethod 
FSMethod=''
FuncReturn = corr_matrix(X_train, X_test, loc, FSMethod, X_corr, corr_val=0.8)
#receiving function returns into variables
X_train = FuncReturn[0]
X_test = FuncReturn[1]
loc = FuncReturn [2]
FSMethod = FuncReturn[3]
#caling all DL and ML methods to model location_3 (LND18_DH) dataset
methods(X_train, y_train, X_test, y_test, loc, FSMethod)
#defining the R function and loading the instance in the Python
r.source('stats_methods.R')
#loading the function that is defined in R
stats_methods = robjects.globalenv['stats_methods']
#caling all stats methods to model location_1 (PUL17_F5) dataset
stats_methods(X_train, y_train, X_test, y_test, loc, FSMethod)



# 4. Feature Selection using BayesA ##############
#importing the preprocessing dataset from location 3
from preprocess_loc3 import *
#calling data processing function
preprocess_loc3=preprocess_loc3()
#receiving function returns into variables
X_train = preprocess_loc3[0]
X_test = preprocess_loc3[1]
y_train = preprocess_loc3[2]
y_test =  preprocess_loc3[3]
loc = preprocess_loc3[4]
X_corr = preprocess_loc3[5]
#importing feature selection functions
from feature_selection import *
#setting null string in variable FSMethod 
FSMethod=''
#defining the R function and loading the instance in the Python
r.source('./feature_selection.R')
#loading the function that is defined in R
fs_BayesA = robjects.globalenv['fs_BayesA']
FuncReturn = fs_BayesA(X_train, X_test, loc, FSMethod, y_train, n_features=5500)
#Only for fs_BayesA: receiving function returns into variables
X_train = FuncReturn[0]
X_test = FuncReturn[1]
loc = FuncReturn[2][0]
FSMethod = FuncReturn[3][0]
#caling all DL and ML methods to model location_3 (LND18_DH) dataset
methods(X_train, y_train, X_test, y_test, loc, FSMethod)
#defining the R function and loading the instance in the Python
r.source('stats_methods.R')
#loading the function that is defined in R
stats_methods = robjects.globalenv['stats_methods']
#caling all stats methods to model location_1 (PUL17_F5) dataset
stats_methods(X_train, y_train, X_test, y_test, loc, FSMethod)


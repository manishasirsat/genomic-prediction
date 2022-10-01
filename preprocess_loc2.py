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

# first let’s get all libraries in place
from library import *

########## Data Preprocessing for Location 2 ###########################################################################
def preprocess_loc2():
    #loading the dataset of 'Lozada et al 2020' as a pandas data frame
    df = pd.read_csv('Data/GenomicDataLozada.csv', header = 0, sep = ";")
    #setting 'Beeding line' feature as an index
    df=df.set_index('Breeding line')
    #Dataset2: selecting data points of the location PUL18_DH
    df = df[(df['Population']=='PUL18_DH')]
    #saving location name in a variable 
    loc = 'Loc2'
    #separating genotype and phenotype from the df file
    X=df.iloc[:,:-1]
    y=df.iloc[:,-1:]
    #dropping population variable from genotypic data
    X=X.drop(['Population'], axis=1)      
    #copying for corrlation matrix feature selection method
    X_corr=X

    #data partitioning into train and validation:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=17)
    print(X_train.shape, y_train.shape)
    print(X_test.shape, y_test.shape) 
  
    #printing basic statistics: max, min, mean, sd
    print('min max mean sd')
    print('Train:', y_train.min(), y_train.max(), y_train.mean(), np.sqrt(y_train.var()))
    print('Test:', y_test.min(), y_test.max(), y_test.mean(), np.sqrt(y_test.var()))

    #ploting basic histograms
    #plt.title('Train / test data')
    #plt.hist(y_train, label='Train')
    #plt.hist(y_test, label='Test')
    #plt.legend(loc='best')
    #plt.show()
    
    return(X_train, X_test, y_train, y_test, loc, X_corr)

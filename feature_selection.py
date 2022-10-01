#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Manisha Sirsat
@department: Data Management and Risk Analysis
@organization: InnovPlantProtect, Elvas, Portugal
@website: https://iplantprotect.pt/

"""

from library import *
import random


########## 1. Feature Selection using Variance Threshold ###########################################################################

def fs_vt(X_train, X_test, loc, FSMethod, thold):
    random.seed(1234)
    FSMethod = 'VT'
    var_thres=VarianceThreshold(threshold=thold) # dropping constant features, 
    var_thres.fit(X_train)
    var_thres.get_support()
    X_train.columns[var_thres.get_support()]
    constant_columns = [column for column in X_train.columns
                        if column not in X_train.columns[var_thres.get_support()]]

    X_train.drop(constant_columns,axis=1)
    FeatureCount = X_train.columns[var_thres.get_support()].shape
    # saving the selected features by variance
    with open("Results/FeatureLists/FeaturesList_VT_%s.txt" % loc, "a") as text_file:
        text_file.write("Number of selected features: %d, \n\nList of the selected features by Variance Threshold on %s:\n\n%s" % (FeatureCount[0], loc, list(X_train.columns[var_thres.get_support()])))
    X_train = var_thres.transform(X_train)
    X_test = var_thres.transform(X_test)
    print(X_train.shape[1])
    return (X_train, X_test, loc, FSMethod)


########## 2. Feature Selection using Mutual Information ###########################################################################

def fs_mi(X_train, X_test, loc, FSMethod, y_train, pctl):
    random.seed(4567)
    FSMethod = 'MI'
    mutual_info = mutual_info_regression(X_train.fillna(0), y_train.values.ravel())
    mutual_info
    mutual_info = pd.Series(mutual_info)
    mutual_info.index = X_train.columns
    mutual_info.sort_values(ascending=False)  
    # selecting the top 'pctl' percentile
    selected_top_columns = SelectPercentile(mutual_info_regression, percentile = 10)
    selected_top_columns.fit(X_train.fillna(0), y_train.values.ravel())
    selected_top_columns.get_support()
    list(X_train.columns[selected_top_columns.get_support()])
    FeatureCount = X_train.columns[selected_top_columns.get_support()].shape
    #saving the selected features by mutual information
    with open("Results/FeatureLists/FeaturesList_MI_%s.txt" % loc , "a") as text_file:
        text_file.write("Number of selected features: %d,\n\nList of the selected features by Mutual Information on %s:\n\n%s" % (FeatureCount[0], loc, list(X_train.columns[selected_top_columns.get_support()])))
    X_train = selected_top_columns.transform(X_train)
    X_test = selected_top_columns.transform(X_test)
    return (X_train, X_test, loc, FSMethod, y_train)


########## 3. Feature Selection using Correlation Matrix ###########################################################################

def corr_matrix(X_train, X_test, loc, FSMethod, X_corr, corr_val):
    random.seed(7891)
    FSMethod = 'Corr_Matrix'
    corr_features = set() # creating set to hold the correlated features
    corr_matrix = X_corr.corr() #creating the correlation matrix (default to pearson)
    #displaying a heatmap of the correlation matrix
    #plt.figure(figsize=(11,11))
    #sns.heatmap(corr_matrix)
    for i in range(len(corr_matrix .columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > corr_val:
                colname = corr_matrix.columns[i]
                corr_features.add(colname)
        
    X_train.drop(labels=corr_features, axis=1, inplace=True)
    X_test.drop(labels=corr_features, axis=1, inplace=True)
    
    FeatureCount = X_train.columns.shape
    #saving the selected features by correlation matrix
    with open("Results/FeatureLists/FeaturesList_Corr_Matrix_%s.txt" % loc, "a") as text_file:
        text_file.write("Number of selected features: %d,\n\nList of the selected features by Correlation Matrix on %s:\n\n%s" % (FeatureCount[0], loc, list(X_train.columns)))  

    return(X_train, X_test, loc, FSMethod)

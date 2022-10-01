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

#first let’s get all libraries ¸
from library import *
from sklearn.metrics import make_scorer
from custom_measure import manual_pearson
import random

def create_mlp_py(X_train):
    # create model
    SNPs=X_train.shape[1] 
    #instantiate
    mlp_py = tf.keras.Sequential()
    # Add first layer
    mlp_py.add(tf.keras.layers.Dense(32, input_dim=SNPs, activation='relu'))
    # Add second layer
    mlp_py.add(tf.keras.layers.Dense(16, activation='relu'))
    mlp_py.add(Dropout(0.2))

    mlp_py.add(tf.keras.layers.Dense(1, activation='softplus'))
    #compile model
    mlp_py.compile(loss='mse', optimizer='adam', metrics=[correlation_coefficient_loss])
    # list some properties
    mlp_py.summary()
    
    return mlp_py

def methods(X_train, y_train, X_test, y_test, loc, FSMethod):
    
    if FSMethod == 'VT' and loc == 'Loc1':
        
        models_param_grid = [

        # 1st parameter grid, corresponding to RF
        {"n_estimators": np.linspace(2, 1500, 10).astype('int'),
         'max_depth':[int(x) for x in np.linspace(2, 2530, num = 10)], 
         'max_features': [0.001, 0.01, 0, 0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2']},
    
        # 2nd parameter grid, corresponding to ExtraTree
        {'n_estimators': np.linspace(2, 500, 10).astype('int'),
        'min_samples_split':range(0, 300, 3)},
    
        # 3rd parameter grid, corresponding to GradientBoostingRegressor
        {'learning_rate': [0.01, 0.1, 0.5, 1.0, 10.0],
         'max_features': [0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2', None],
         'max_depth': [3, 5, 10]},
    
        # 4th parameter grid, corresponding to Adaboost
        {"learning_rate": [0.05, 0.10, 0.15, 0.20, 0.25, 0.30],
        "n_estimators": np.linspace(2, 500, 6).astype('int')},
    
        # 5th parameter grid, corresponding to XGBRegressor
        {"learning_rate": [ 0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ],
         "max_depth": range(3, 100 ,2),
         "min_child_weight": range(1, 100, 2),
         "gamma": [ 0.0, 0.1, 0.2 , 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ],
         "colsample_bytree": [ 0.3, 0.4, 0.5 , 0.7, 0.9, 0.10 ]},
        
        # 6th parameter grid, corresponding to mlp               
        
         {"batch_size": [10, 20, 30, 40, 50, 60, 70],
         "epochs": [10, 50, 100, 150]}]
        
        ml_methods(X_train, y_train, X_test, y_test, loc, FSMethod, models_param_grid)
        
        
    elif FSMethod == 'MI' and loc == 'Loc1':
        
        models_param_grid = [
        # 1st parameter grid, corresponding to RF
        {"n_estimators": np.linspace(2, 1500, 10).astype('int'),
         'max_depth':[int(x) for x in np.linspace(2, 2530, num = 10)], 
         'max_features': [0.001, 0.01, 0, 0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2']},
    
        # 2nd parameter grid, corresponding to ExtraTree
        {'n_estimators': np.linspace(2, 700, 10).astype('int'),
         "min_samples_split": range(2, 15, 3)},
    
        # 3rd parameter grid, corresponding to GradientBoostingRegressor
        {'learning_rate': [0.01, 0.1, 0.5, 1.0, 10.0, 100.0],
         'max_features': [0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2', None],
         'max_depth': [3, 5, 10, 15]},
    
        # 4th parameter grid, corresponding to Adaboost
        {"learning_rate": [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40],
        "n_estimators": np.linspace(2, 500, 4).astype('int')},
    
        # 5th parameter grid, corresponding to XGBRegressor
        {"learning_rate": [ 0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ],
         "max_depth": range(3, 100 ,2),
         "min_child_weight": range(1, 100, 2),
         "gamma": [ 0.0, 0.1, 0.2 , 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ],
         "colsample_bytree": [ 0.3, 0.4, 0.5 , 0.7, 0.9, 0.10 ]},
         
         # 6th parameter grid, corresponding to mlp               
         {"batch_size": [10, 20, 30, 40, 50, 60, 70],
         "epochs": [10, 50, 100, 150]}]
        
        ml_methods(X_train, y_train, X_test, y_test, loc, FSMethod, models_param_grid)

    elif FSMethod == 'Corr_Matrix' and loc == 'Loc1':
        models_param_grid = [
        # 1st parameter grid, corresponding to RF
        {"n_estimators": np.linspace(2, 1500, 10).astype('int'),
         'max_depth':[int(x) for x in np.linspace(2, 2530, num = 10)], 
         'max_features': [0.001, 0.01, 0, 0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2']},
    
        # 2nd parameter grid, corresponding to ExtraTree
        {'n_estimators': np.linspace(2, 200, 10).astype('int'),
         "min_samples_split": range(2, 15, 3)},
    
        # 3rd parameter grid, corresponding to GradientBoostingRegressor
        {'learning_rate': [0.01, 0.1, 0.5, 1.0, 10.0, 100.0],
         'max_features': [0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2', None],
         'max_depth': [3, 5, 10]},
    
        # 4th parameter grid, corresponding to Adaboost
        {"learning_rate": [0.05, 0.10, 0.15, 0.20, 0.25, 0.30],
        "n_estimators": np.linspace(2, 1200, 10).astype('int')},
    
        # 5th parameter grid, corresponding to XGBRegressor
        {"learning_rate": [ 0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ],
         "max_depth": range(3, 100 ,2),
         "min_child_weight": range(1, 100, 2),
         "gamma": [ 0.0, 0.1, 0.2 , 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ],
         "colsample_bytree": [ 0.3, 0.4, 0.5 , 0.7, 0.9, 0.10 ]},
         
         # 6th parameter grid, corresponding to mlp               
         {"batch_size": [10, 20, 30, 40, 50, 60, 70, 80],
         "epochs": [10, 50, 100, 150]}]
        
        ml_methods(X_train, y_train, X_test, y_test, loc, FSMethod, models_param_grid)
        
    elif FSMethod == 'BayesA' and loc == 'Loc1':
        
        models_param_grid = [               
       
        # 1st parameter grid, corresponding to RF
        {"n_estimators": np.linspace(2, 1500, 10).astype('int'),
         'max_depth':[int(x) for x in np.linspace(2, 900, num = 10)], 
         'max_features': [0.001, 0.01, 0, 0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2']},
    
        # 2nd parameter grid, corresponding to ExtraTree
        {'n_estimators': np.linspace(2, 500, 10).astype('int'),
         "min_samples_split": range(2, 600, 3)},
    
        # 3rd parameter grid, corresponding to GradientBoostingRegressor
        {'learning_rate': [0.01, 0.1, 0.5, 1.0, 10.0, 100.0],
         'max_features': [0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2', None],
         'max_depth': [3, 5, 10]},
    
        # 4th parameter grid, corresponding to Adaboost
        {"learning_rate": [0.05, 0.10, 0.15, 0.20, 0.25, 0.30],
        "n_estimators": np.linspace(2, 1200, 10).astype('int')},
    
        # 5th parameter grid, corresponding to XGBRegressor
        {"learning_rate": [ 0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ],
         "max_depth": range(3, 100 ,2),
         "min_child_weight": range(1, 100, 2),
         "gamma": [ 0.0, 0.1, 0.2 , 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ],
         "colsample_bytree": [ 0.3, 0.4, 0.5 , 0.7, 0.9, 0.10 ]},
         
         # 6th parameter grid, corresponding to mlp               
         {"batch_size": [10, 30, 90, 120, 150],
         "epochs": [10, 50, 100, 150, 200]}]
        
        ml_methods(X_train, y_train, X_test, y_test, loc, FSMethod, models_param_grid)

        
    elif FSMethod == 'VT' and loc == 'Loc2':
        
        models_param_grid = [
        # 1st parameter grid, corresponding to RF
        {"n_estimators": np.linspace(2, 1500, 10).astype('int'),
         'max_depth':[int(x) for x in np.linspace(2, 200, num = 10)], 
         'max_features': [0.001, 0.01, 0, 0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2']},
    
        # 2nd parameter grid, corresponding to ExtraTree
        {'n_estimators': np.linspace(2, 500, 10).astype('int'),
         "min_samples_split": range(2, 20, 3)},
    
        # 3rd parameter grid, corresponding to GradientBoostingRegressor
        {'learning_rate': [0.01, 0.1, 0.5, 1.0, 10.0, 100.0],
         'max_features': [0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2', None],
         'max_depth': [3, 5, 10]},
    
        # 4th parameter grid, corresponding to Adaboost
        {"learning_rate": [0.05, 0.10, 0.15, 0.20, 0.25, 0.30],
        "n_estimators": np.linspace(2, 1000, 10).astype('int')},
    
        # 5th parameter grid, corresponding to XGBRegressor
        {"learning_rate": [ 0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ],
         "max_depth": range(3, 100 ,2),
         "min_child_weight": range(1, 100, 2),
         "gamma": [ 0.0, 0.1, 0.2 , 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ],
         "colsample_bytree": [ 0.3, 0.4, 0.5 , 0.7, 0.9, 0.10 ]},
         
         # 6th parameter grid, corresponding to mlp               
         {"batch_size": [10, 20, 30, 40, 50, 60, 70],
         "epochs": [10, 50, 100, 150, 200]}]
        
        ml_methods(X_train, y_train, X_test, y_test, loc, FSMethod, models_param_grid)

    elif FSMethod == 'MI' and loc == 'Loc2':
        
        models_param_grid = [
        # 1st parameter grid, corresponding to RF
        {"n_estimators": np.linspace(2, 1500, 10).astype('int'),
         'max_depth':[int(x) for x in np.linspace(2, 200, num = 10)], 
         'max_features': [0.001, 0.01, 0, 0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2']},
    
        # 2nd parameter grid, corresponding to ExtraTree
        {'n_estimators': np.linspace(2, 500, 10).astype('int'),
         "min_samples_split": range(2, 20, 2)},
    
        # 3rd parameter grid, corresponding to GradientBoostingRegressor
        {'learning_rate': [0.01, 0.1, 0.5, 1.0, 10.0, 100.0],
         'max_features': [0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2', None],
         'max_depth': [3, 5, 10]},
    
        # 4th parameter grid, corresponding to Adaboost
        {"learning_rate": [0.05, 0.10, 0.15, 0.20, 0.25, 0.30],
        "n_estimators": np.linspace(2, 450, 10).astype('int')},
    
        # 5th parameter grid, corresponding to XGBRegressor
        {"learning_rate": [ 0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ],
         "max_depth": range(3, 100 ,2),
         "min_child_weight": range(1, 100, 2),
         "gamma": [ 0.0, 0.1, 0.2 , 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ],
         "colsample_bytree": [ 0.3, 0.4, 0.5 , 0.7, 0.9, 0.10 ]},
         
         # 6th parameter grid, corresponding to mlp               
        {"batch_size": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
         "epochs": [10, 50, 100, 150, 200]}]
        
        ml_methods(X_train, y_train, X_test, y_test, loc, FSMethod, models_param_grid)

    elif FSMethod == 'Corr_Matrix' and loc == 'Loc2':  
        
        models_param_grid = [
        # 1st parameter grid, corresponding to RF
        {"n_estimators": np.linspace(2, 1200, 10).astype('int'),
         'max_depth':[int(x) for x in np.linspace(2, 200, num = 10)], 
         'max_features': [0.001, 0.01, 0, 0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2']},
    
        # 2nd parameter grid, corresponding to ExtraTree
        {'n_estimators': np.linspace(2, 500, 10).astype('int'),
         "min_samples_split": range(2, 600, 3)},
    
        # 3rd parameter grid, corresponding to GradientBoostingRegressor
        {'learning_rate': [0.01, 0.1, 0.5, 1.0, 10.0, 100.0],
         'max_features': [0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2', None],
         'max_depth': [3, 5, 10]},
    
        # 4th parameter grid, corresponding to Adaboost
        {"learning_rate": [0.05, 0.10, 0.15, 0.20, 0.25, 0.30],
        "n_estimators": np.linspace(2, 1500, 10).astype('int')},
    
        # 5th parameter grid, corresponding to XGBRegressor
        {"learning_rate": [ 0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ],
         "max_depth": range(3, 100 ,2),
         "min_child_weight": range(1, 100, 2),
         "gamma": [ 0.0, 0.1, 0.2 , 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ],
         "colsample_bytree": [ 0.3, 0.4, 0.5 , 0.7, 0.9, 0.10 ]},
         
          # 6th parameter grid, corresponding to mlp               
         {"batch_size": [10, 20, 30, 40, 50, 60, 70],
         "epochs": [10, 50, 100, 150]}]
        
        ml_methods(X_train, y_train, X_test, y_test, loc, FSMethod, models_param_grid)
        
    elif FSMethod == 'BayesA' and loc == 'Loc2':
        
         models_param_grid = [
         
         # 1st parameter grid, corresponding to RF
        {"n_estimators": np.linspace(2, 1100, 10).astype('int'),
         'max_depth':[int(x) for x in np.linspace(2, 2530, num = 10)], 
         'max_features': [0.001, 0.01, 0, 0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2']},
    
        # 2nd parameter grid, corresponding to ExtraTree
        {'n_estimators': np.linspace(2, 500, 10).astype('int'),
        "min_samples_split": range(2, 15, 3)},
    
        # 3rd parameter grid, corresponding to GradientBoostingRegressor
        {'learning_rate': [0.01, 0.1, 0.5, 1.0, 10.0, 100.0],
         'max_features': [0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2', None],
         'max_depth': [3, 5, 10]},
    
        # 4th parameter grid, corresponding to Adaboost
        {"learning_rate": [0.05, 0.10, 0.15, 0.20, 0.25, 0.30],
        "n_estimators": np.linspace(2, 1200, 10).astype('int')},
    
        # 5th parameter grid, corresponding to XGBRegressor
        {"learning_rate": [ 0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ],
         "max_depth": range(3, 100 ,2),
         "min_child_weight": range(1, 100, 2),
         "gamma": [ 0.0, 0.1, 0.2 , 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ],
         "colsample_bytree": [ 0.3, 0.4, 0.5 , 0.7, 0.9, 0.10 ]},
         
         # 6th parameter grid, corresponding to mlp               
        {"batch_size": [10, 20, 30, 40, 50, 60, 70],
         "epochs": [10, 50, 100, 150]}]
         
         ml_methods(X_train, y_train, X_test, y_test, loc, FSMethod, models_param_grid)

    elif FSMethod == 'VT' and loc == 'Loc3':
        
        models_param_grid = [
        # 1st parameter grid, corresponding to RF
        {"n_estimators": np.linspace(2, 1000, 10).astype('int'),
         'max_depth':[int(x) for x in np.linspace(2, 200, num = 10)], 
         'max_features': [0.001, 0.01, 0, 0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2']},
    
        # 2nd parameter grid, corresponding to ExtraTree
        {'n_estimators': np.linspace(2, 500, 10).astype('int'),
        "min_samples_split": range(2, 20, 3)},
    
        # 3rd parameter grid, corresponding to GradientBoostingRegressor
        {'learning_rate': [0.01, 0.1, 0.5, 1.0, 10.0, 100.0],
         'max_features': [0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2', None],
         'max_depth': [3, 5, 10, 15, 20]},
    
        # 4th parameter grid, corresponding to Adaboost
        {"learning_rate": [0.05, 0.10, 0.15, 0.20, 0.25, 0.30],
        "n_estimators": np.linspace(2, 1200, 10).astype('int')},
    
        # 5th parameter grid, corresponding to XGBRegressor
        {"learning_rate": [ 0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ],
         "max_depth": range(3, 100 ,2),
         "min_child_weight": range(1, 100, 2),
         "gamma": [ 0.0, 0.1, 0.2 , 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ],
         "colsample_bytree": [ 0.3, 0.4, 0.5 , 0.7, 0.9, 0.10, 0.12, 0.14]},
         
         # 6th parameter grid, corresponding to mlp               
         {"batch_size": [10, 20, 30, 40, 50, 60, 70, 80],
         "epochs": [10, 30, 60, 90, 110, 130]}]

        ml_methods(X_train, y_train, X_test, y_test, loc, FSMethod, models_param_grid)

    elif FSMethod == 'MI' and loc == 'Loc3':
        
        models_param_grid = [
        # 1st parameter grid, corresponding to RF
        {"n_estimators": np.linspace(2,1100, 10).astype('int'),
         'max_depth':[int(x) for x in np.linspace(2, 200, num = 10)], 
         'max_features': [0.001, 0.01, 0, 0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2']},
    
        # 2nd parameter grid, corresponding to ExtraTree
        {'n_estimators': np.linspace(2, 400, 10).astype('int'),
        "min_samples_split": range(2, 20, 3)},
    
        # 3rd parameter grid, corresponding to GradientBoostingRegressor
        {'learning_rate': [0.01, 0.1, 0.5, 1.0, 10.0, 100.0],
         'max_features': [0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2', None],
         'max_depth': [3, 5, 10]},
    
        # 4th parameter grid, corresponding to Adaboost
        {"learning_rate": [0.01, 0.05, 0.10, 0.15],
        "n_estimators": np.linspace(2, 500, 10).astype('int')},
    
        # 5th parameter grid, corresponding to XGBRegressor
        {"learning_rate": [ 0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ],
         "max_depth": range(3, 100 ,2),
         "min_child_weight": range(1, 100, 2),
         "gamma": [ 0.0, 0.1, 0.2 , 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ],
         "colsample_bytree": [ 0.3, 0.4, 0.5 , 0.7, 0.9, 0.10 ]},
         
         # 6th parameter grid, corresponding to mlp               
         {"batch_size": [10, 20, 30, 40, 50, 60, 70],
         "epochs": [10, 50, 100, 150]}]
        
        ml_methods(X_train, y_train, X_test, y_test, loc, FSMethod, models_param_grid)

    elif FSMethod == 'Corr_Matrix' and loc == 'Loc3':  
        
        models_param_grid = [
        # 1st parameter grid, corresponding to RF
        {"n_estimators": np.linspace(2, 1000, 10).astype('int'),
         'max_depth':[int(x) for x in np.linspace(2, 200, num = 10)], 
         'max_features': [0.001, 0.01, 0, 0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2']},
    
        # 2nd parameter grid, corresponding to ExtraTree
        {'n_estimators': np.linspace(2, 300, 10).astype('int'),
        "min_samples_split": range(2, 20, 3)},
    
        # 3rd parameter grid, corresponding to GradientBoostingRegressor
        {'learning_rate': [0.01, 0.1, 0.5, 1.0, 10.0, 100.0],
         'max_features': [0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2', None],
         'max_depth': [3, 5, 10]},
    
        # 4th parameter grid, corresponding to Adaboost
        {"learning_rate": [0.05, 0.10, 0.15, 0.20, 0.25, 0.30],
        "n_estimators": np.linspace(2, 1100, 10).astype('int')},
    
        # 5th parameter grid, corresponding to XGBRegressor
        {"learning_rate": [ 0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ],
         "max_depth": range(3, 100 ,2),
         "min_child_weight": range(1, 100, 2),
         "gamma": [ 0.0, 0.1, 0.2 , 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ],
         "colsample_bytree": [ 0.3, 0.4, 0.5 , 0.7, 0.9, 0.10 ]},
         
         # 6th parameter grid, corresponding to mlp               
         {"batch_size": [10, 20, 30, 40, 50, 60],
         "epochs": [10, 30, 60, 90, 110]}]
        
        ml_methods(X_train, y_train, X_test, y_test, loc, FSMethod, models_param_grid)
        
    elif FSMethod == 'BayesA' and loc == 'Loc3':
        models_param_grid = [               
         
         # 1st parameter grid, corresponding to RF
        {"n_estimators": np.linspace(2, 1100, 10).astype('int'),
         'max_depth':[int(x) for x in np.linspace(2, 2530, num = 10)], 
         'max_features': [0.001, 0.01, 0, 0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2']},
    
        # 2nd parameter grid, corresponding to ExtraTree
        {'n_estimators': np.linspace(2, 400, 10).astype('int'),
        "min_samples_split": range(2, 20, 3)},
    
        # 3rd parameter grid, corresponding to GradientBoostingRegressor
        {'learning_rate': [0.01, 0.1, 0.5, 1.0, 10.0, 100.0],
         'max_features': [0.1, 0.25, 0.5, 0.75, 'sqrt', 'log2', None],
         'max_depth': [3, 5, 10]},
    
        # 4th parameter grid, corresponding to Adaboost
        {"learning_rate": [0.05, 0.10, 0.15, 0.20, 0.25, 0.30],
        "n_estimators": np.linspace(2, 1200, 10).astype('int')},
    
        # 5th parameter grid, corresponding to XGBRegressor
        {"learning_rate": [ 0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ],
         "max_depth": range(3, 100 ,2),
         "min_child_weight": range(1, 100, 2),
         "gamma": [ 0.0, 0.1, 0.2 , 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 ],
         "colsample_bytree": [ 0.3, 0.4, 0.5 , 0.7, 0.9, 0.10 ]},
         
         # 6th parameter grid, corresponding to mlp               
         {"batch_size": [10, 20, 30, 40, 50, 60],
         "epochs": [10, 30, 60, 90, 110]}]
        
        ml_methods(X_train, y_train, X_test, y_test, loc, FSMethod, models_param_grid)


########## Model Training on Location 1/2/3 (PUL17_F5/PUL18_DH/LND18_DH) dataset ##############
def ml_methods(X_train, y_train, X_test, y_test, loc, FSMethod, models_param_grid):    
    
    #defining a list of the ml methods, including mlp
    models_to_run = [RandomForestRegressor(random_state=11), ExtraTreesRegressor(random_state=12), GradientBoostingRegressor(random_state=10), AdaBoostRegressor(random_state=31), XGBRegressor(random_state=77), KerasRegressor(build_fn=lambda:create_mlp_py(X_train), verbose=1)]
    
    #defining the names of all methods
    model_names =['Random Forests', 'Extra Trees', 'Gradient Boosting', 'AdaBoost', 'XGBRegressor', 'MLP']
    
    #hyper-parameter list of the models
    models_param_grid = models_param_grid

    #fitting the models using 4-fold cross validation     
    for i,model in enumerate(models_to_run):
        algo_name= model_names[i]
        print(algo_name)
    
        def timer(start_time=None):
            if not start_time:
                start_time = datetime.now()
                return start_time
            elif start_time:
                thour, temp_sec = divmod((datetime.now() - start_time).total_seconds(), 3600)
                tmin, tsec = divmod(temp_sec, 60)
                print('\n Time taken: %i hours %i minutes and %s seconds.' % (thour, tmin, round(tsec, 2)))
        from datetime import datetime   
        start_time = timer(None) # timing starts from here
        
        randomGrid_search = RandomizedSearchCV(estimator=model, param_distributions=models_param_grid[i], 
                                               verbose=3, random_state=76, cv=4, 
                                               refit='TRUE', n_jobs=1)
        
        random.seed(134)
        randomGrid_search.fit(X_train, y_train.values.ravel())
    
        timer(start_time) # timing ends here

        randomGrid_search.best_params_ #checking the best selected hyper-parameters
        print(randomGrid_search.best_params_)
        reg= randomGrid_search.best_estimator_    
        score=cross_val_score(reg, X_train, y_train.values.ravel(), cv=4, scoring=make_scorer(manual_pearson)) # model selection using CV
        print(score)
        print('Correlation of CV: mean= %.3f, std= %.3f'% (score.mean(), score.std())) # printing the train score

        #predicting the accuracy on the test data 
        y_pred = reg.predict(X_test) 
        r2 = r2_score(y_test, y_pred) # coefficient of determination (R2)
        y_pred = pd.DataFrame(list(y_pred))
        y_pred.index=y_test.index
        y_pred.rename(columns={0: 'Yield'}, inplace=True)
    
        corr= manual_pearson(y_test,y_pred) #calculating the correlation between the predicted and observed values
        print('\n Correlation =',corr)
    
        #preparing the strings for saving purpose
        model_string1 = algo_name + ' and ' + FSMethod
        model_string2 = algo_name + '_' + FSMethod + '_' + loc
    
        #path to store the models result
        path = FSMethod + '_' + loc
    
        #exporting the best hyper-parameters
        with open("Results/HyperParameters/BestParameter_%s.csv" % path , "a") as text_file:
            text_file.write("Model name and it's best parameters: \n")
            text_file.write("%s, %s\n\n" % (algo_name, randomGrid_search.best_params_))  
  
        #exporting the output into a file
        with open("Results/ModelResults/Results_%s.csv" % path , "a") as text_file:
            text_file.write("Model name, train_corr, test_corr:\n")
            text_file.write("%s, %0.3f, %0.3f\n\n" % (algo_name, score.mean(), corr))   
   
        #visualizing actual of the test dataset vs predicted values 
        import matplotlib.pyplot as plt
        plt.switch_backend('agg')
        plt.scatter(y_test,y_pred, edgecolors=(0,0,0))
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
        plt.ylabel('Predicted values', fontsize=10)
        plt.xlabel('Actual values', fontsize=10)
        plt.title('Actual and predicted grain yield by %s on %s' % (model_string1, loc), fontsize=10)
        plt.show()
        plt.savefig("Results/Figures/%s" % model_string2 + ".png", dpi=300)
        plt.clf()

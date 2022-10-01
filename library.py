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

#first let’s get all libraries in place
import pandas as pd
import numpy as np
from numpy import arange
import seaborn as sns
from matplotlib import pyplot as plt
from scipy import stats
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import BayesianRidge
from sklearn.svm import LinearSVR
from xgboost import XGBRegressor
from math import sqrt
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import mutual_info_regression
from sklearn.feature_selection import VarianceThreshold
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import fbeta_score, make_scorer
from custom_measure import *
#importing rpy2
import rpy2.robjects as robjects
r = robjects.r

import subprocess as sp

#importing the Keras libraries and packages
import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LeakyReLU,PReLU,ELU
from keras.layers import Dropout
from keras.wrappers.scikit_learn import KerasRegressor
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Dense, Dropout, Flatten, GRU, SimpleRNN, LSTM, Bidirectional, Activation, TimeDistributed

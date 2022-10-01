#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Manisha Sirsat
@department: Data Management and Risk Analysis
@organization: InnovPlantProtect, Elvas, Portugal
@website: https://iplantprotect.pt/

"""

from library import *
import tensorflow as tf
from keras import backend as K


def manual_pearson(a,b):
    a_avg, b_avg = np.average(a), np.average(b)
    a_std, b_std = np.std(a), np.std(b)
    n = len(a)
    divisor = a_std * b_std * n
    numerator = np.sum(np.multiply(a-a_avg, b-b_avg))
    p_coef = numerator/divisor
    return p_coef    

def r_squared(y_true, y_pred):
    from keras import backend as K
    SS_res =  K.sum(K.square( y_true-y_pred ))
    SS_tot = K.sum(K.square( y_true - K.mean(y_true) ) )
    return ( 1 - SS_res/(SS_tot + K.epsilon()) )

    
def correlation_coefficient_loss(y_true, y_pred):
    x = y_true
    y = y_pred
    mx = K.mean(x, axis=0)
    my = K.mean(y, axis=0)
    xm, ym = x - mx, y - my
    r_num = K.sum(xm * ym)
    x_square_sum = K.sum(xm * xm)
    y_square_sum = K.sum(ym * ym)
    r_den = K.sqrt(x_square_sum * y_square_sum)
    r = r_num / r_den
    r = K.maximum(K.minimum(r, 1.0), -1.0)
    return 1 - K.square(r)
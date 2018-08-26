#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""
from collections import Counter
import numpy as np
import random
import scipy.stats as ss
import matplotlib.pyplot as plt


def distance(p1,p2):
    '''Find distance between the p1 and p2'''
    return np.sqrt(np.sum(np.power(p2-p1,2)))

def majority_vote_short(votes):
    '''
    scipy stats mstats mode
    returns an array of the modal(the most common) value in the passed array
    '''
    mode,count=ss.mstats.mode(votes)
    return mode

def find_nearest_neighbors(p,points,k=None):
    distances=np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i]=distance(p,points[i])
    index_=np.argsort(distances)
    #print(index_)
    #print(distances[index_])
    return index_[0:k]

def knn_predict(p,points,y,k=None):
    #Predict the class of p based on majority vote...
    ind_=find_nearest_neighbors(p,points,k)
    return majority_vote_short(y[ind_])

def main():
    print('SINCHIGUANO CESAR')


    votes=[1,3,2,1,2,3,2,2,3]
    print(majority_vote_short(votes))

    X=np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
    y=np.array([0,0,0,0,1,1,1,1,1])
    point=np.array([2.5,2])

    indexDISTANCE=find_nearest_neighbors(point,X,k=3)
    print(X[indexDISTANCE])


    print(len(y))
    y_tst=knn_predict(np.array([2.5,2.7]),X,y,k=2)
    print('Predicted',y_tst)




if __name__=='__main__':
	main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 18:20:15 2023

@author: a007678
"""
import numpy as np

class Centile:
    def __init__(self,LH,scores):
        self.LH = LH
        self.scores = scores
        
    def __str__(self):
        return f'LHs: {self.LH}, Scores: {self.scores}'
    
    def LHtoCycle(self, num_to_add):
        '''
        This method returns the LH days reported as days of a standard 28 day cycle.

        Returns
        -------
        None.

        '''
        LH_array = np.array(self.LH)
        return(LH_array + num_to_add)
    



def calcPercentile(pd_dataframe=None, LH=None, scores=None):
    '''
    
    calcPercentile function takes an array of scores and returns percentile values.
    
    '''
    
    if pd_dataframe != None:
        result = pd_dataframe
    elif LH != None and scores !=None:
        result = LH
    else:
        print("provide dataframe or LH and scores.")
        return
    
    print("running")
    return(result)

if __name__ == '__main__':
    calcPercentile()
    c1 = Centile([1,2,3],[0.5,0.4,0.75])
    


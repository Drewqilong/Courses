# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 18:48:55 2019

@author: drewqilong
"""
import pandas as pd
import numpy as np

class Week1(object):
    def __init__(self, data_file=None):

        self.data_file = data_file
        self.df_data = pd.read_csv(self.data_file)
    
    def calculate(self):
        cols = [c for c in self.df_data.columns if c not in ["object"]]
        df_median = self.df_data[cols].median()
        print('\n' + "Median")
        print(df_median)
        
        df_max = self.df_data[cols].max()
        print('\n' + "Max")
        print(df_max)
        
        df_min = self.df_data[cols].min()
        print('\n' + "Min")
        print(df_min)
        
        df_filter = self.df_data[cols]
#        df_outliers = df_outliers[df_outliers.iloc[:,1:2] > 1]
        
        # Extract values and row, column names
        arr = df_filter.values
        index_names = df_filter.index
        col_names = df_filter.columns
        #  Get indices where outliers are
        R,C = np.where(np.logical_or(arr>1,arr<0))
        # Arrange those in columns and put out as a dataframe
        out_arr = np.column_stack((index_names[R],col_names[C],arr[R,C]))
        df_outliers = pd.DataFrame(out_arr,columns=[['row_name','col_name','outliers']])
        print(df_outliers)


if __name__ == '__main__':
    data_process = Week1(data_file='H:\Github\DS\sonar_hw1.csv')
    data_process.calculate()
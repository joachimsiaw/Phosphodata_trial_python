# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =============================================================================
# Pseudocode

# import libraries
import panda
import numpy as np
# define file path and save path to a variable
filepath = 'C:/Users/joach_000/OneDrive/Course/Python/Phospho data_python trial.csv'

# Read file
file = pandas.read_csv(filepath,  encoding='latin1')
file.replace(np.nan, "", inplace=True)
print(file)
#### CLEAN DATA
#Drop column 2 of file
file_1 = file.drop('Index in Detail', axis=1)
print(file_1)
 
#Drop 1st 3 rows in file_1 and renamedit file_2, 3, 4

file_2 = file_1.drop(file_1.index[0])
print (file_2)
file_3 = file_2.drop(file_1.index[1])
file_4 = file_3.drop(file_1.index[2])
print(file_4)

file_5 = file_4.rename({"Fold change" : "fold_change"}, inplace = True)
print(file_5)
file_4 = file_4.rename({'Gene name' : 'gene_name'})
print (file_4)
file# Look into column 1 which corresponds to Fold change
#      if Fold change < 0
# print 
for index, row in file_4.iterrows():
    for number in "Fold change":
        if number < 0:
            print (row["Fold change"], row["Gene name"])
            
        
     
            
    
    
#        then print fold change and corresponding gene name in column 3 
#    	if Fold change < -1.5
# 	then print gene name and corresponding fold change and save as List_fold_change<-1.5
# 
# if Fold change > 0
#        then print fold change and corresponding gene name in column 3 
#    	if Fold change > 1.5
# 	then print gene name and corresponding fold change and save as List_fold_change>1.5
# 
# =============================================================================


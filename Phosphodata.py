# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =============================================================================
# Pseudocode

# import libraries
import pandas
import numpy as np
# define file path and save path to a variable
filepath = 'C:/Users/joach_000/OneDrive/Course/Python/Phospho data_python trial.csv'

# Read file
file = pandas.read_csv(filepath,  encoding='latin1')
file.replace(np.nan, "", inplace=True)
print(file)
#### CLEAN DATA

file_1 = file.drop('XX', axis=1)
print(file_1)



# Look into column 1 which corresponds to Fold change
#      if Fold change < 0
# print 

for x in file_1.iterrows():
    print(type(x[1]))

  
for index, row in file_1.iterrows():

    print(row["Fold change"], row["Gene name"])
            
    
    
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


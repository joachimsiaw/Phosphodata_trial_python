# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =============================================================================
# Pseudocode

# import libraries
import pandas as pd
import numpy as np
# define file path and save path to a variable
filepath = 'C:/Users/joach_000/OneDrive/Course/Python/V. Leishmania DE genes.csv'

# Read file
file = pd.read_csv(filepath,  encoding='latin1')

print(file)

# type of data  of each column

print(file.dtypes)

#Basic stats on the dataframe.

print(file.describe())

# sorting the data by fold change to visually inspect range of fold change

file_sorted = file.sort_values(by=['Fold_change'])
print(file_sorted)



file.plot.bar()

# Extract names of genes with Fold change >= 1.5 or <= -1.5

# Plot a graph of all genes with fold change in the range of 1.5 <= fold_change <= -1.5

# list of  top 10 most upregulated genes 
# list of top 10 most downregulated genes

# =============================================================================


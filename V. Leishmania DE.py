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

# Extract names of genes with Fold change >= abs 1.5

file_foldchange = file[abs(file.Fold_change) >= 1.5]

# Plot a graph of all genes with fold change >= abs 1.5

file_foldchange.plot.bar()

# sorting the data by fold change 

file_sorted = file.sort_values(by=['Fold_change'])
print(file_sorted)

# list of  top 10 most downregulated genes

top10_downregulated = file_sorted.head(10)
print(top10_downregulated)

# list of top 10 most upregulated genes

top10_upregulated = file_sorted.tail(10)
print (top10_upregulated)
 
#sort top10_upregulated by fold change descending order to have the most upreulated gene on top

top10_upregulated_sorted = top10_upregulated.sort_values(by=['Fold_change'], ascending=False)
print(top10_upregulated_sorted)


# =============================================================================


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
 
#sort top10_upregulated by fold change in descending order to have the most upreulated gene on top

top10_upregulated_sorted = top10_upregulated.sort_values(by=['Fold_change'], ascending=False)
print(top10_upregulated_sorted)

# Extract Gene_name and Fold_change columns in the top10 files 

top10_downregulated_extract = top10_downregulated[['Gene_name', 'Fold_change']]
print(top10_downregulated_extract)

top10_upregulated_extract = top10_upregulated_sorted[['Gene_name', 'Fold_change']]
print(top10_upregulated_extract)

#Merge top10 extract files from both up and downregulated dataframes into one data frame

merge = [top10_upregulated_extract, top10_downregulated_extract]
top10_merge = pd.concat(merge, ignore_index=True)
print(top10_merge)

#Plot graph of top 10 most up and ttop 10 most down regulated gene

top10_merge.plot.bar(x='Gene_name', y='Fold_change', color='b' )


# Hexaginal bin plot of entire dataframe to view distibution of FDR

file.plot.hexbin(x='Fold_change', y='FDR', gridsize=20)

#Extract separate lists of all down and up regulated genes from file

file_downregulated=file[file['Fold_change']<0]  
print(file_downregulated)
file_upregulated=file[file['Fold_change']>0]  
print(file_upregulated)

#create a dictionary of the lists generated

pieces={'x': file_upregulated, 'y': file_downregulated}

#concatenate pieces
file2=pd.concat(pieces)
print(file2)

# =============================================================================


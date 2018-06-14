# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =============================================================================
# Pseudocode

# import libraries
import pandas as pd
import matplotlib.pyplot as plt

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

fold_change_greater = file[abs(file.Fold_change) >= 1.5]

Gene_extract = [fold_change_greater['Gene_name'], fold_change_greater['Fold_change']]
Gene_extract_df= pd.concat(Gene_extract, axis=1)

# Plot a graph of all genes with fold change >= abs 1.5 in pd

Gene_extract_df.plot.bar()

# Hexaginal bin plot of entire dataframe to view distribution of FDR

file.plot.hexbin(x='Fold_change', y='FDR', gridsize=20)

#Extract separate lists of all down and up regulated DE genes from file

file_downregulated=file[file['Fold_change']<0]  
print(file_downregulated)
file_upregulated=file[file['Fold_change']>0]  
print(file_upregulated)


#Counting the number of up and downregulated DE genes in file

number_of_up_genes=(file_upregulated['Fold_change'].count())
print(number_of_up_genes)
number_of_down_genes=(file_downregulated['Fold_change'].count())
print(number_of_down_genes)

#Making a list of the gene counts
Number_of_genes=[number_of_up_genes,number_of_down_genes]
Type_of_gene_regulation=['upregulated', 'downregulated']
colors=['green', 'blue']

#Ploting a bar chart of DE genes with matplot library
plt.bar(Type_of_gene_regulation,Number_of_genes,color=colors)
plt.ylabel('Number of genes')
plt.title('Barchart-Distribution of number of DE genes in V.leishmania patients')
plt.show()

#Plot of pie chat of DE genes
plt.pie(Number_of_genes, colors=colors, labels=Number_of_genes)
plt.legend(Type_of_gene_regulation)
plt.title('Piechart-Distribution of number of DE genes in V.leishmania patients')
plt.show()

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

#Plot graph of top 10 most up and top 10 most down regulated gene with pd

top10_merge.plot.bar(x='Gene_name', y='Fold_change', color='b' )

#Plot graph of top 10 most up and top 10 most down regulated gene with matplotlib
genename=top10_merge['Gene_name']
foldchange=top10_merge['Fold_change']
plt.bar(genename,foldchange,color='green')
plt.xlabel('Gene name', fontsize=16)
plt.ylabel('Fold change', fontsize=16)
plt.title('Top 20 most DE genes', fontsize=20)
plt.show()

# -*- coding: utf-8 -*-
"""
@author: Nicholas Dowell
"""

import pandas as pd


#Part A - Read the file into a pandas dataframe
df = pd.read_csv('m1_w2_ds1.csv')

#Part B - use Class Labelling on any string '1 5 255'
from sklearn.preprocessing import LabelEncoder

#The column named 'PUBCHEM_COORDINATE_TYPE' is the only column with '1 5 255' in it
class_le = LabelEncoder()
#the fit_transform method calculates labels for the provided column
y = class_le.fit_transform(df['PUBCHEM_COORDINATE_TYPE'].values)

df['PUBCHEM_COORDINATE_TYPE'] = y   #sets each value in the column to its calculated label  (in this case all zeroes)
#note: labelEncoder takes care of the labelling process so the user need not specify labels

'''
Part C-  Map all ordinal data columns to numbers
Ordinal data is data where the categories are in an implied order,
 but their magnitudes are not necessarily consistent.
 an example wouyld be Small, Medium, Large.

Ordinal Data is in one column:
    PUBCHEM_TOTAL_CHARGE  (POSITIVE, NEGATIVE, ZERO)
'''
positivity_mapping = {'POSITIVE' : 1, 'NEGATIVE' : -1, 'ZERO' : 0}

df['PUBCHEM_TOTAL_CHARGE'] = df['PUBCHEM_TOTAL_CHARGE'].map(positivity_mapping)

'''
Part D - Handle the remaining categorical data in the last column: 'apol'

'''
#getdummies using pandas
#literally does the whole thing in one line of code.
df = pd.get_dummies(df)
#The apol column is now One-Hot encoded
#get_dummies actually encodes every column that has strings in it,
#   so the user needs to be careful! In this case if we had not already encoded two columns in our desired way, they would have been encoded here.

'''
Part E - replace missing values with the mean from the column
'''

for column in df:     #This loop iterates over the column names in a dataframe
    df[column] = df[column].fillna(df[column].mean(skipna = True))
    #each column finds its own mean (skipping nan), and replaces nans with the mean
'''
Part F - find mean of each row, mean of each column, sd of columns, sd of rows.
'''
# (i)The mean of values in each column
print("MEAN VALUES OF COLUMNS")
print(df.mean(axis = 0))

#(ii) The mean values in each row
print("MEAN VALUES OF EACH ROW")
print(df.mean(axis = 1))

# (iii)The standard deviation (STD) of the values in each column and  print the result
print("STANDARD DEVIATION OF EACH COLUMN")
print(df.std(axis = 0))

# (iv) The standard deviation (STD) of the values in each row and  print the result
print("STANDARD DEVIATION OF EACH ROW")
print(df.std(axis = 1))





###############################
###         PART 2          ###
###############################

# 1. Scatter Plot first 10 columns and rows
    #I will use seaborn pairplot to do this.

import seaborn as sns
#cols stores the head of each column as a string - This will make access easier
cols =             ['CID',
                    'IC50',
                    'class',
                    'PUBCHEM_XLOGP3_AA',
                    'PUBCHEM_EXACT_MASS',
                    'PUBCHEM_MOLECULAR_WEIGHT',
                    'PUBCHEM_CACTVS_TPSA',
                    'PUBCHEM_MONOISOTOPIC_WEIGHT',
                    'PUBCHEM_TOTAL_CHARGE',
                    'PUBCHEM_HEAVY_ATOM_COUNT',
                    ]

#plots each column against all the others
sns.pairplot(df.loc[0:10, cols])




# 2. Heatmap the first 10 columns and rows
#This Heatmap is a correlation matrix like we saw in a previous example
import numpy as np
#This code is the same code from the code samples provided.
plt.figure()
cm = np.corrcoef(df[cols].values.T) # calculates a correlation coefficient for each pair of columns
sns.set(font_scale=0.6) #formatting for the visual

#plots the heatmap
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 8}, yticklabels=cols, xticklabels=cols)
plt.show()


#df[cols].values.T   What is going on in this packed line of code??
    #df[cols] is a dataframe
    #.values returns a numpy array containing the same values
    #np_array.T returns the transpose of the array.
    #so the whole thing just turns the dataframe on its own side.




#3. Are there any Outlier points?
# To answer this, I will look at the pairplot above.
# the outliers I find here are relative to the small subset of the data I am looking at in the 10 rows and 10 columns
#row indexes are provided in terms of their position within the data, not within the csv file, so row 0 is the first row of data
'''
Two of the CID values in the 22 million range are far apart from the other 8 at 11 million
26000 and 18000 are outliers in the IC50 column
the Class column is completely uniform
PUBCHEM_XLOGP3_AA - 5.1 and 4.1 are outliers
PUBCHEM_EXACT_MASS   353, 353, and 395 are all outliers
PUBCHEM_MOLECULAR_WEIGHT - There don't seem to be any outliers- the data is spread widely though
PUBCHEM_CACTVS_TPSA - One value is an outlier all the awy up at 109
PUBCHEM_MONOISOTOPIC_WEIGHT - no outliers
PUBCHEM_TOTAL_CHARGE - All values are -1, so there are no outliers
PUBCHEM_HEAVY_ATOM_COUNT - One outlier at value of 32
'''



#4. Find Quantiles
# I will assume quartiles are what is wanted since the n is not specified for n-quantile

import matplotlib.pyplot as plt
#make my own dataframe ftr with only the first 10 rows of data - should have dont this first
# FTR stands for First Ten Rows ( and ten columns)
ftr = df.loc[0:10, cols]



fix, axs = plt.subplots(1, 10)

for i in range(10):
    plt.sca(axs[i])

    ftr.boxplot(column=cols[i])

#prints the 25%, 50%, and 75% quantiles for each column in the entire dataframe

q = df.quantile(q = [.25, .50, .75], axis=0)
print(q)




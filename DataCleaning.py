# -*- coding: utf-8 -*-
"""
@author: Nicholas Dowell
"""

import pandas as pd


#Part A - Read the file into a pandas dataframe
df = pd.read_csv('m1_w2_ds1.csv')

#Part B - use Class Labelling on any string '1 5 255'
from sklearn.preprocessing import LabelEncoder

#looking at the column named 'PUBCHEM_COORDINATE_TYPE'
class_le = LabelEncoder()
#the fit_transform method calculates labels for the provided column
y = class_le.fit_transform(df['PUBCHEM_COORDINATE_TYPE'].values)

df['PUBCHEM_COORDINATE_TYPE'] = y   #sets each value in the column to its calculated label  (in this case all zeroes)
#note: labelEncoder takes care of the labelling process so the user need not specify labels

'''
Part C-  Map all ordinal data columns to
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
Part F - 
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









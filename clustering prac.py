#'''
# Import libraries necessary for this project
import numpy as np
import pandas as pd
from IPython.display import display # Allows the use of display() for DataFrames

# Import supplementary visualizations code visuals.py
#import visuals as vs

# Pretty display for notebooks
#%matplotlib inline

# Load the wholesale customers dataset
try:
    data = pd.read_csv("customers.csv")
    data.drop(['Region', 'Channel'], axis = 1, inplace = True)
    print "Wholesale customers dataset has {} samples with {} features each.".format(*data.shape)
except:
    print "Dataset could not be loaded. Is the dataset missing?"

# TODO: Select three indices of your choice you wish to sample from the dataset
indices = [150, 200, 210, 211]

# Create a DataFrame of the chosen samples
samples = pd.DataFrame(data.loc[indices], columns = data.keys()).reset_index(drop = True)
#print "Chosen samples of wholesale customers dataset:"
display(samples)
#'''

pd.set_option('display.height', 500)
pd.set_option('display.max_rows', 500)

print data[data['Milk'] == 55][data['Detergents_Paper'] >= 0][data['Fresh'] >= 0]
print min(data['Milk'])
#47, 383, 
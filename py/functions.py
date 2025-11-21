#imports
import pandas as pd
import numpy as np

#all helper functions used

def data_grabber():
    data = pd.read_csv("sdss_100k_galaxy_classification_dr18.csv")
    return data

data = data_grabber()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

data.head()
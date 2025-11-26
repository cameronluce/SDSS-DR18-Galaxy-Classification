#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#all helper functions used below
url = "https://www.kaggle.com/api/v1/datasets/download/bryancimo/sdss-galaxy-classification-dr18"

def data_grabber():
    data = pd.read_csv(url, encoding='ISO-8859-1')
    return data

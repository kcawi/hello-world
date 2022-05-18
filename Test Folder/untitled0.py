# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 16:15:19 2022
DAEN 690-004 Spring 2022 GMU
@author: Kimberly Cawi
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd 
from sklearn.preprocessing import PowerTransformer, QuantileTransformer

FAI_Noah_df = pd.read_csv(
        'FAI_USW00026411_Noah_01012017_12312021_all temps_order2895112.csv')

cols1 = ["AWND", "PRCP","SNOW", "TMAX"]
def test_transformers(columns):
    pt = PowerTransformer()
    qt = QuantileTransformer(n_quantiles=500, output_distribution='normal')
    fig = plt.figure(figsize=(20,30))
    j = 1
    for i in columns:
        array = np.array(FAI_Noah_df[i]).reshape(-1, 1)
        y = pt.fit_transform(array)
        x = qt.fit_transform(array)
        plt.subplot(3,3,j)
        sns.histplot(array, bins = 50, kde = True)
        plt.title(f"Original Distribution for {i}")
        plt.subplot(3,3,j+1)
        sns.histplot(x, bins = 50, kde = True)
        plt.title(f"Quantile Transform for {i}")
        plt.subplot(3,3,j+2)
        sns.histplot(y, bins = 50, kde = True)
        plt.title(f"Power Transform for {i}")
        j += 4
test_transformers(cols1)


# Generate data on commute times.
FAI_Noah_df['PRCP']

FAI_Noah_df['PRCP'].plot.hist(grid=True, bins=20, rwidth=0.9,
                   color='#607c8e')
plt.title('Precipitation')
plt.xlabel('Inches')
plt.ylabel('Counts')
plt.grid(axis='y', alpha=0.75)



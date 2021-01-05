#%%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rc('font', family='NanumBarunGothic')

df = pd.read_csv('https://bit.ly/ds-house-price-clean')

df.plot()


# %%

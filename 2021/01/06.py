#%%
import matplotlib.pyplot as plt
from numpy.lib.shape_base import column_stack
import pandas as pd
import numpy as np

plt.rc('font', family='NanumBarunGothic')

df = pd.read_csv('https://bit.ly/ds-house-price-clean')

# 여러개의 plot을 그리는 방법 (subplots) - s 가 붙습니다.

#plt.subplots(행의 개수, 열의 갯수)

data = np.arange(1, 51)

fig, axes = plt.subplots(2, 3)

axes[0,0].plot(data)
axes[0,1].plot(data * data)
axes[0,2].plot(data ** 3)
axes[1,0].plot(data % 10)
axes[1,1].plot(-data)
axes[1,2].plot(data // 20)

plt.tight_layout()
plt.show()

# %%
from IPython.display import Image


Image('https://matplotlib.org/_images/anatomy.png')

# 타이틀

plt.plot([1, 2, 3], [3, 6, 9])
plt.plot([1,2,3], [2,4,9])
plt.title("This is title.")

plt.xlabel('people', fontsize=20)
plt.ylabel('family', fontsize=20)
plt.show()


# %%

plt.plot(np.arange(10), np.arange(10)*2)
plt.plot(np.arange(10), np.arange(10)**2)
plt.plot(np.arange(10), np.log(np.arange(10)))

# 타이틀 


#%%
import matplotlib.pyplot as plt
from numpy.lib.shape_base import column_stack
import pandas as pd
import numpy as np

plt.rc('font', family='NanumBarunGothic')

df = pd.read_csv('https://bit.ly/ds-house-price-clean')

# df.plot()


# data = np.arange(1,100)
# data




# 다중 그래프 (multiple graphs)

# 1개의 canvas 안에 다중 그래프 그리기

# data = np.arange(1, 51)
# data2 = np.arange(51, 101)


# plt.plot(data)
# plt.plot(data2)
# plt.plot(data2+50)
# plt.show()


# 2개의 figure로 나누어서 다중 그래프 그리기

# data = np.arange(100, 201)
# data2 = np.arange(200, 301)

# plt.plot(data)
# # figure는 새로운 그래프를 그림
# plt.figure()
# plt.plot(data2)
# plt.show()



# 여러개 의 plot을 그리는 방법(subplot)

# subplot(row, column, index)

# data = np.arange(100, 201)
# plt.subplot(2, 1, 1)
# # plt.subplot(211)
# plt.plot(data)

# data2 = np.arange(200, 301)
# plt.subplot(2, 1, 2)
# # plt.subplot(212)
# plt.plot(data2)

# plt.show()


data = np.arange(100, 201)
plt.subplot(1, 3, 1)
# plt.subplot(211)
plt.plot(data)

data2 = np.arange(200, 301)
plt.subplot(1, 3, 2)
# plt.subplot(212)
plt.plot(data2)

data3 = np.arange(300, 401)
plt.subplot(1, 3, 3)
# plt.subplot(212)
plt.plot(data3)

plt.show()
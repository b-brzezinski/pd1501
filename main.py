import numpy as np

data = np.load('data/ex3_data.npy')

filter = np.isnan(data)
print(filter.sum(axis=0))
print(np.any(filter,axis=1).sum())
data_new=data[~np.any(filter,axis=1)][::]
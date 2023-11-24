import create_dataset_sklearn

import dbscan
import matplotlib.pyplot as plt

# (1) Generate data

nsample = 20
case = "varied_blobs1"
X = create_dataset_sklearn.create_dataset(nsample, case)

# (2) Create model

minpts = 3
epsilon = 0.3
model = dbscan.dbscan(minpts, epsilon)

# (3) Fit model

model.fit(X)
print("Fitting time: {}".format(model.time_fit))


print(X)

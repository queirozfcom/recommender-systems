# naive-knn-algorithm

`naive-knn.py` is a naïve implementation of the k-nearest neighbours algorithm for classification and regression.

It expects a **pandas** dataframe as input as well as the following parameters:

- **k** the number of neighbours to use (integer, default 3)
- **d** the column index to use as the target feature to be predicted (integer, default=0)
- **split** the proportion of the number of samples to use in the training index (float, between 0.0 and 1.0, default 0.8)
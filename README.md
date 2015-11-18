# Recommender systems

## Comments

### List 1

### List 2

- ex 3,4:

 - It seems that the average of the rating of one ITEM over all users that rated it performs slightly better (i.e. is a slightly better predictor for the actual rating) than the average of the rating of one USER over all items he/she rated:

 - 5 runs of `list2/ex3.jl` (using user average) averaged **0.833** error.
 - 5 runs of `list2/ex4.jl` (using item average) averaged **0.813** error.

- ex 5

 - For exercise 5, I've experimented using *both* the average rating by the user *and* the average rating given for the item  when predicting a rating given by a user for an item. Each "guess" was given equal weight

 - 5 runs of `list2/ex5.jl` averaged **0.795** error

### Item-based K-Nearest Neighbours Algorithm

 > Based upon [Andre Ng's CS 229 notes](http://cs229.stanford.edu/proj2008/Wen-RecommendationSystemBasedOnCollaborativeFiltering.pdf)

`item-based-knn/item-based-knn.py` is a naïve implementation of the k-nearest neighbours algorithm applied for recommending items.

The general idea is to find items that are similar to a movie *m* so that we can determine what rating a user *u* would give for movie *m*, given that user *u* has not yet seen movie *m*. I have used the **adjusted cosine similarity** between movies a and b, as follows:

![adjusted cosine similarity](http://latex2png.com/output//latex_6561357334a98e738333f703f88f90b3.png)

Sample results can be found in file `item-based-knn/results.csv`, which is of the form: 

    USER_ID,ITEM_ID,ORIGINAL_RATING,PREDICTED_RATING,ROOT_SQUARED_ERROR

### SVD Algorithm

This algorithm tries to decompose and discover a *low-dimensional* approximation of the **user-movie** matrix (**A**), where each row represents a user and each column represents a movie, and element **Aij** represents the *rating* user *i* gave to movie *j*.

Each user *u* and movie *m* have a **feature vector**, modelled in the same feature-space. Unknown ratings can be inferred by performing the dot product between the feature vectors for user *u* and movie *m*.

It can be accessed in `svd/svd.py`.


# recommendation_systems

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

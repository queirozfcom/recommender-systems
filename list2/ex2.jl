using DataArrays,DataFrames
using PyCall

@pyimport matplotlib.pyplot as plt
@pyimport matplotlib.figure as pyfigure

function main()

  path = "../ml-100k/u.data"
  df = readrel(path,'\t')

  num_ratings = aggregate(df,:rating,length)[:item_id_length]
  ratings = 1:5

  plt.bar(ratings,num_ratings)
  plt.xlabel("RATING_GIVEN")
  plt.ylabel("NUMBER_OF_RATINGS_GIVEN")
  plt.xticks([1,2,3,4,5])
#   plt.tick_params(axis="x")

#   plt.figure(figsize=(40,10))

  plt.show()

end

function readrel(relpath,delimiter=',')

  base = dirname(@__FILE__)

  if relpath[1] == '/'
    relpathwslash = relpath
  else
    relpathwslash = string("/",relpath)
  end

  path = string(base,relpathwslash)

  df = readtable(path,separator = delimiter)

  names!(df,[:user_id,:item_id,:rating,:timestamp])

  df

end

main()

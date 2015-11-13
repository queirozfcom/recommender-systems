using DataArrays,DataFrames
using PyCall

@pyimport matplotlib.pyplot as plt
@pyimport matplotlib.figure as pyfigure

function main()

  path = "../ml-100k/u.data"
  df = readrel(path,'\t')

  usergroups= sort(aggregate(df,:user_id,length), cols = :rating_length, rev=true)

  user_ids = usergroups[:user_id]

  indexes = 1:length(user_ids)

  num_ratings = usergroups[:rating_length]
  plt.figure(figsize=(40,10))
  plt.xlabel("USER_IDS")
  plt.ylabel("NUMBER_OF_RATINGS")
  plt.bar(indexes,num_ratings)
  plt.xticks(user_ids,rotation=45)

  plt.show()

end

# data =

#df[:user_id]

# describe(d)

# row = data[:]

# println(row)

# usergroups = groupby(x -> x[:x1],data)



# ndims(usergroups)

# for i in usergroups
#   println(length(i))
# end

# for i in usergroups
#   println(i[1])
# end


# digits = imap(i -> parseint(string(i[1][1])), groupedbyuser)

# println(digits)

# for i in usergroups

#   print("user_id: ")
#   print(i[1][1])
# #   print("  length: ")
# #   println(length(i))
# end

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

#   readdlm(path,delimiter)

end

# length([1,2,3])

# main()

# readrel("../ml-100k/u.data",'\t')

# str = "/foobar"

# str[1] == '/'

main()

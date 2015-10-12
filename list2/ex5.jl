using DataArrays,DataFrames,StatsBase

function main()

  path = "../ml-100k/u.data"
  df = readrel(path,'\t')

  indices = shuffle([1:size(df,1)])

  # number of unique users
  totalusers = size(aggregate(df,:user_id,length),1)
  # total number of ratings
  totalratings = length(indices)

  # training

  trainingsetlimit = int(totalratings*(8/10))
  trainingindices  = indices[1:trainingsetlimit]
  trainingset      = df[trainingindices,:]

  # aggregating by ITEMS
  avgratingsbyitem  = aggregate(trainingset,:item_id,mean)[ [:item_id,:rating_mean] ]
  # and by USERS
  avgratingsbyuser  = aggregate(trainingset,:user_id,mean)[ [:user_id,:rating_mean] ]

  # global average for all items
  globalavgbyitem = mean(avgratingsbyitem[:rating_mean])

  # global average for all users
  globalavgbyuser = mean(avgratingsbyuser[:rating_mean])

  # test

  testsetlimit   = trainingsetlimit + (totalratings - trainingsetlimit)
  testindices    = indices[trainingsetlimit:testsetlimit]
  testset        = df[testindices,:]

  global sumerror = 0.0

  testratings = testset[:,[:user_id,:item_id,:rating]]

  totaltestinstances = size(testratings,1)

  for row in eachrow(testratings)

    # guess based upon the item itself
    item_id = row[:item_id]

    if item_id in avgratingsbyitem[:item_id]
      guessbyitem = avgratingsbyitem[:rating_mean][avgratingsbyitem[:item_id] .== item_id]
    else
      guessbyitem = globalavgbyitem
    end

    # guess based upon the user
    user_id = row[:user_id]

    if user_id in avgratingsbyuser[:user_id]
      guessbyuser = avgratingsbyuser[:rating_mean][avgratingsbyuser[:user_id] .== user_id]
    else
      guessbyuser = globalavgbyuser
    end

    actual = row[:rating]

    guess = (guessbyitem + guessbyuser)/2

    error = abs(actual-guess)
    sumerror += error

#     print("user_id: ")
#     print(user_id)
#     print(" guess: ")
#     print(guess)
#     print(" actual: ")
#     print(actual)
#     print(" error: ")
#     println(abs(actual-guess))

  end

  # dividing the error by the number of instances in the test set
  mae = sumerror/totaltestinstances

  mae

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

mae = main()
println(mae)

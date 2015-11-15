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
  trainavgratings  = aggregate(trainingset,:user_id,mean)[ [:user_id,:rating_mean] ]

  # spanning all users
  globalavg = mean(trainavgratings[:rating_mean])

  # test

  testsetlimit   = trainingsetlimit + (totalratings - trainingsetlimit)
  testindices    = indices[trainingsetlimit:testsetlimit]
  testset        = df[testindices,:]

  global sumerror = 0.0

  useridsandratings = testset[:,[:user_id,:rating]]

  totaltestinstances = size(useridsandratings,1)

  for row in eachrow(useridsandratings)

    user_id = row[:user_id]

    if user_id in trainavgratings[:user_id]
      guess = trainavgratings[:rating_mean][trainavgratings[:user_id] .== user_id]
    else
      guess = globalavg
    end

    actual = row[:rating]

    error = abs(actual-guess)
    sumerror += error

    # printing stuff
    # print("user_id: ")
    # print(user_id)
    # print(" guess: ")
    # print(guess)
    # print(" actual: ")
    # print(actual)
    # print(" error: ")
    # println(abs(actual-guess))

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

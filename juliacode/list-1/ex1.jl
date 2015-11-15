function main(input)

  numcols = size(input)[2]
  numrows = size(input)[1]

  output = Int32[]

  for i=1:numrows
    row = input[i,:]
    newrow = mknewmatrixrow(row)

    # in the first loop, output will be empty
    if size(output,1) == 0
      output = newrow
    else
      output = vcat(output,newrow)
    end
  end

  output
end

function mknewmatrixrow(inputrowmatrix)

  numrows = size(inputrowmatrix)[1]
  numcols = size(inputrowmatrix)[2]

  @assert numrows == 1

  outputrow = Int32[]

  largestindex = 1

  for i=1:numcols
    if inputrowmatrix[i] > inputrowmatrix[largestindex]
      largestindex = i
    end
  end

  for i=1:numcols
    if i == largestindex
      push!(outputrow,1)
    else
      push!(outputrow,0)
    end
  end

  outputrowmatrix = reshape(outputrow,1,numcols)
  @assert size(outputrowmatrix)[2] == numcols
  outputrowmatrix
end

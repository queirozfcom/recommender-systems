# a function that takes an nx2 matrix and returns a new nx2 matrix
# where each element is a 1 or a 0, depending upon whether it's the largest
# or smallest value in that row in the input matrix
function winner_matrix(input)

  numcols = size(input)[2]

  output = Vector{Int32}[]

  if numcols != 2
    throw(ArgumentError("Input matrix must have exactly 2 columns"))
  else
    numrows = size(input)[1]

    for i=1:numrows
      left = input[i,:][1]
      right = input[i,:][2]

      if left > right
        newpair = [1,0]
      elseif right > left
        newpair = [0,1]
      else
        newpair = [1,0]
      end

      push!(output,newpair)
    end
    output
  end
end


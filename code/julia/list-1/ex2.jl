function main(inputmatrix)

  println("Initial matrix looks like this:")
  println(inputmatrix)

  # an array of tuples representing the positions
  # dummy initialization so that it's never empty
  top3positions = [(1,1),(1,2),(1,3)]

  numrows = size(inputmatrix)[1]
  numcols = size(inputmatrix)[2]

  for i=1:numrows
    for j=1:numcols
      elem = (i,j)
      top3positions = updatepositions(inputmatrix,top3positions,elem)
    end
  end

  position1 = top3positions[1]
  position2 = top3positions[2]
  position3 = top3positions[3]

  outputmatrix = deepcopy(inputmatrix)

  outputmatrix[position1[1],position1[2]] = 0
  outputmatrix[position2[1],position2[2]] = 0
  outputmatrix[position3[1],position3[2]] = 0

  println("At the end, it looks like this:")
  println(outputmatrix)

  outputmatrix
end

function updatepositions(matrix,oldpositions,newposition)

  # from largest to smallest
  positions = orderpositions(matrix,oldpositions)

  position1 = positions[1]
  position2 = positions[2]
  position3 = positions[3]

  # value1 >= value2 >= value3
  value1 = matrix[position1[1],:][position1[2]]
  value2 = matrix[position2[1],:][position2[2]]
  value3 = matrix[position3[1],:][position3[2]]

  newvalue = matrix[newposition[1],:][newposition[2]]

  if newvalue > value1
    positions[3] = positions[2]
    positions[2] = positions[1]
    positions[1] = newposition
  elseif newvalue > value2
    positions[3]= positions[2]
    positions[2] = newposition
    # no change in positions[1]
  elseif newvalue > value3
    positions[3] = newposition
    # no change in positions[1] or positions[2]
  else
    # nothing to do
  end

  positions

end

function orderpositions(matrix,positions)

  @assert size(positions)[1] == 3

  position1 = positions[1]
  position2 = positions[2]
  position3 = positions[3]

  value1 = matrix[position1[1],:][position1[2]]
  value2 = matrix[position2[1],:][position2[2]]
  value3 = matrix[position3[1],:][position3[2]]

  if(value1 >= value2 >= value3)
    orderedpositions = [position1,position2,position3]
  elseif(value1 >= value3 >= value2)
    orderedpositions = [position1,position3,position2]
  elseif(value2 >= value1 >= value3)
    orderedpositions = [position2,position1,position3]
  elseif(value2 >= value3 >= value1)
    orderedpositions =  [position2,position3,position1]
  elseif(value3 >= value1 >= value2)
    orderedpositions = [position3,position1,position2]
  elseif(value3 >= value2 >= value1)
    orderedpositions = [position3,position2,position1]
  end

  @assert size(orderedpositions)[1] == 3

  orderedpositions
end

M = [5 10 -5 22; 1 33 15 3; 8 29 12 1;3 11 39 20]

main(M)

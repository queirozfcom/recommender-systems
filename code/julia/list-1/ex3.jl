function formatmatrix(inputmatrix)

  numrows = size(inputmatrix,1)
  numcols = size(inputmatrix,2)

  trans = inputmatrix'

  firstcol = trans[1,:]
  outputmatrix = map(x -> x/sum(firstcol),firstcol)

  for i=2:numcols
    row = trans[i,:]
    newrow = map(x -> x/sum(row),row)
      outputmatrix = vcat(outputmatrix,newrow)
  end
  outputmatrix'
end


mat = [1 2 3; 4 5 6]

println(formatmatrix(mat))

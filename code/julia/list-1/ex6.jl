using PyCall
using Distributions

@pyimport matplotlib.pyplot as plt
@pyimport matplotlib.figure as pyfigure
@pyimport matplotlib.pylab as pylab
@pyimport matplotlib.colors as colors


function main(keepinput=true)

  #
  # 1 means white, 0 means black
  #

  # number of lines in filter
  n = 500
  # number of columns in filter
  m = 500
  # radius of the filter circle
  r = 60
  # filter off if nothing, keep input
  x = keepinput ? nothing : 0
  # filter on
  y = 1

  filterfunc = f_cria_func_transf(n,m,r,x,y)

  # 1 is white, 0 is black
  inputmatrix = rand(n,m)

  filterfunc(inputmatrix)

end

function f_cria_func_transf(n,m,r,x,y)

  function applyfilter(inputmatrix)

    # input matrix must be at least as large as the requested filter
    @assert size(inputmatrix,1) >= n
    @assert size(inputmatrix,2) >= m
    # only square matrices
    @assert m == n

    totalsize = n*m

    outputmatrix = reshape(deepcopy(inputmatrix),1,totalsize)

    # add indices to elements so that we know where we are
    outputmatrix = collect(enumerate(outputmatrix))

    # apply the filter per se
    # each (index,element) tuple becomes a single filtered element



    filtered = map( tuple -> mapper(tuple[1],tuple[2],x,y,r,m,n),outputmatrix)

    # turn it back into a matrix
    filtered = reshape(filtered,n,m)

    # display
    plt.matshow(filtered,cmap = plt.get_cmap("hot") )
    plt.show()

  end
end

# returns a possibly filtered element
function mapper(index,elem,off,on,radius,numrows,numcols)

  if withinradius(numrows,numcols,radius,index)
    on
  else
    if off == nothing
      elem
    else
      off
    end
  end

end

function withinradius(numrows,numcols,radius,elemindex)

  # otherwise we can't find the center of the filter circle
  @assert numrows == numcols

  center = if numrows % 2 == 0
    (numrows/2,numcols/2)
  else
    ((numrows+1)/2,(numcols+1)/2)
  end

  # this is the position of the element we want to evaluate
  element_i = div(elemindex,numcols) +1
  element_j = elemindex % numcols +1

  # do you remember pythagoras' theorem?
  dist1 = abs(center[1]-element_i)
  dist2 = abs(center[2]-element_j)
  hyp = sqrt( (dist1^2) + (dist2^2) )

  if hyp <= radius
    true
  else
    false
  end

end


# main(true) sets the off state of the filter to be the original input
# main(false) sets the off state of the filter be 0 (i.e. black)
main(true)

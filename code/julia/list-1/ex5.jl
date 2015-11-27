using PyCall
using Distributions

@pyimport matplotlib.pyplot as plt
@pyimport matplotlib.figure as pyfigure

function main()

  dist = Normal(20,5)

  samples = rand(dist,100)
  x = 1:100
  plt.figure(figsize=(40,120))
  plt.plot(x,samples,color="red")
  plt.show()

end

main()

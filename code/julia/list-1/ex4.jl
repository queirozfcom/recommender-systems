using PyCall
using Distributions

@pyimport matplotlib.pyplot as plt
@pyimport matplotlib.figure as pyfigure

function part1()

  un = Uniform(-2,2)

  samples = rand(un,500)
  x = 1:500
  oneoverx = map(elem -> 1/elem,x)

  plt.figure(figsize=(20,10))

  # unif
  plt.xlim(xmin=-50,xmax=550)
  plt.ylim(ymin=-5,ymax=5)
  plt.grid()
  plt.plot(x,samples,color="red")

  # sin(x)
  plt.xlim(xmin=-50,xmax=550)
  plt.ylim(ymin=-5,ymax=5)
  plt.grid()
  plt.plot(1:500,sin(x),color="blue")

  # cos(x)
  plt.xlim(xmin=-50,xmax=550)
  plt.ylim(ymin=-5,ymax=5)
  plt.grid()
  plt.plot(1:500,cos(x),color="green")

  # sin(1/x)
  plt.xlim(xmin=-50,xmax=550)
  plt.ylim(ymin=-5,ymax=5)
  plt.grid()
  plt.plot(1:500,sin(oneoverx),color="black")

  # cos(1/x)
  plt.xlim(xmin=-50,xmax=550)
  plt.ylim(ymin=-5,ymax=5)
  plt.grid()
  plt.plot(1:500,cos(oneoverx),color="pink")

  plt.show()

end

function part2()
  un = Uniform(-2,2)

  samples = rand(un,500)
  x = 1:500
  oneoverx = map(elem -> 1/elem,x)

  plt.figure(figsize=(20,10))

  # unif
  plt.subplot(331)
  plt.xlim(xmin=-50,xmax=550)
  plt.ylim(ymin=-5,ymax=5)
  plt.grid()
  plt.plot(x,samples,color="red")

  # sin(x)
  plt.subplot(332)
  plt.xlim(xmin=-50,xmax=550)
  plt.ylim(ymin=-5,ymax=5)
  plt.grid()
  plt.plot(1:500,sin(x),color="blue")

  # cos(x)
  plt.subplot(333)
  plt.xlim(xmin=-50,xmax=550)
  plt.ylim(ymin=-5,ymax=5)
  plt.grid()
  plt.plot(1:500,cos(x),color="green")

  # sin(1/x)
  plt.subplot(334)
  plt.xlim(xmin=-50,xmax=550)
  plt.ylim(ymin=-5,ymax=5)
  plt.grid()
  plt.plot(1:500,sin(oneoverx),color="black")

  # cos(1/x)
  plt.subplot(335)
  plt.xlim(xmin=-50,xmax=550)
  plt.ylim(ymin=-5,ymax=5)
  plt.grid()
  plt.plot(1:500,cos(oneoverx),color="pink")

  plt.show()

end

part2()

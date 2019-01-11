from pylab import *

Z = np.random.random((1440,900))

imshow(Z, cmap=get_cmap("Spectral"), interpolation='nearest')
show()

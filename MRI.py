import numpy as np
import matplotlib.pyplot as plt

from phantominator import shepp_logan

# Build phantom
img = shepp_logan(128)
# Centered Fourier Transform
kData = np.fft.fftshift(np.fft.fft2(img))

# View (run twice to fix plot size)
fig = plt.figure()
a = fig.add_subplot(1, 2, 1)
plt.rcParams['figure.figsize'] = [15, 15]
imgplot = plt.imshow(img)
imgplot.set_cmap('gray')
a.axis('off')
a.set_title('Shepp-Logan phantom',fontsize=25)

a = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(np.abs(kData))
imgplot.set_clim(0.0, 200)
imgplot.set_cmap('gray')
a.axis('off')
a.set_title('k-Space Data',fontsize=25)

 # Solution pt. 1
mask = np.zeros((128,128))
mask[48:79,48:79] = 1

kDataCenter = np.multiply(mask,kData)
imgLowpass = np.abs(np.fft.ifft2(np.fft.ifftshift(kDataCenter)))


 # View
fig = plt.figure()
a = fig.add_subplot(1, 2, 1)
imgplot = plt.imshow(np.abs(kDataCenter))  # put the name of masked k-space data matrix
imgplot.set_clim(0.0, 200)
imgplot.set_cmap('gray')
a.axis('off')
a.set_title('k-Space Data',fontsize=25)

a = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(imgLowpass) # put the name of reconstructed image
imgplot.set_cmap('gray')
a.axis('off')
a.set_title('Reconstructed Image',fontsize=25)
plt.show()

import imageio.v3 as iio

filenames = ["PIC3.jpg", "PIC2.jpg", "PIC1.jpg"]
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('affan.gif', images, duration = 500, loop = 0)
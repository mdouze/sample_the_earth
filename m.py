import numpy as np

rs = np.random.RandomState(123)

for i in range(1000):

  xyz = rs.randn(3)
  xyz /= np.sqrt((xyz ** 2).sum())

  x, y, z = xyz

  long = np.arctan2(y, x) * 180 / np.pi
  lat = np.arcsin(z) * 180 / np.pi

  # print long, lat
  print '<a href="https://www.google.com/maps/@%.7f,%.7f,1268m/data=!3m1!1e3">%.7f,%.7f</a><br>' % (lat, long, lat, long)
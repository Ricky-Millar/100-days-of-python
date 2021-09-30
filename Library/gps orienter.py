import pyproj
geodesic = pyproj.Geod(ellps='WGS84')
fwd_azimuth,back_azimuth,distance = geodesic.inv(0, -50, 0, 50)
print(fwd_azimuth,back_azimuth,distance)
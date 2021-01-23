from geopy.distance import geodesic

newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(geodesic(newport_ri, cleveland_oh).km)


krakow = (50.0611671, 19.9453291)
hobart = (-42.8781275, 147.3214182)

print(geodesic(krakow, hobart).km)


# 1ft = 0.3048 m


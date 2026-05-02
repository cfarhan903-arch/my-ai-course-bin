import numpy as np

address, longitude, lat, postalCode = np.genfromtxt('FastFoodRestaurants.csv', delimiter=',', usecols=(0,4,5,7), unpack=True, dtype=str, encoding='utf-8', skip_header=1, invalid_raise=False)
print("Address: ", address)
print("Longitude: ", longitude)
print("Latitude: ", lat)
print("Postal Code: ", postalCode)

# fast food restaurant longitude - statistics operations
print("fast food restaurant longitude mean: ", np.mean(longitude))
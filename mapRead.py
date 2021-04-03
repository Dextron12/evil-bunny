with open("default.map", 'r') as f:
    data = f.read()

m = []
data = data.split("-")
mapSize = data[-1].split(",")
mapSize[0] = int(mapSize[0])
mapSize[1] = int(mapSize[1])
print(mapSize)
del data[-1]

print(data)

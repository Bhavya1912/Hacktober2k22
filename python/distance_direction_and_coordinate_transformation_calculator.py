import math
#euclidean distance calculator
#input the lat, long and radius. Add - for S and W

LatA = float(input("Enter latitude A in decimal degrees (south is negative):"))
LongA = float(input("Enter longitude A in decimal degrees (north is negative):"))
LatB = float(input("Enter latitude B in decimal degrees (south is negative):"))
LongB = float(input("Enter longitude B in decimal degrees (north is negative):"))
R = float(input("Enter a radius:"))

#calculate the distance between the points A and B
#find the colatitudes

a = math.radians( 90 - (LatB))
b = math.radians( 90 - (LatA))
C = math.radians(LongA - LongB)

# calculate c

cosc = math.cos(a) * math.cos(b) + math.sin(a) * math.sin(b) * math.cos(C)
c= math.acos(cosc)

#calculate distance

Dist= R * c

#output distance

print('The distance between A and B is:', round(Dist/1000, 2), 'Km')


#calculate the direction
#get I and II

I = math.sin(C)
II = math.tan(math.radians(LatB)) * math.cos(math.radians(LatA)) - math.sin(math.radians(LatA)) * math.cos(C)

#breakup formula
i = I**2
ii= II**2
s = i + ii
s2 = math.sqrt(s)
t = math.degrees(math.atan(I/(II - s2))) 

#calculate direction from A to B

AB = 2 * t + 180

#output direction
print('Direction from A to B is',AB, 'decimal degrees')

#get III

III = math.tan(math.radians(LatA)) * math.cos(math.radians(LatB)) - math.sin(math.radians(LatB)) * math.cos(C)

#breakup fromula
iii = III**2
s1 = i + iii
s22 = math.sqrt(s1)
t2 = math.degrees(math.atan(I/(-III+ s22)))

#calculate direction from B to A

BA = 2 * t2 + 180

#output direction
print('Direction from B to A is ',BA, 'decimal degrees')

#convert x and y coordinates to eastings and northings and back to x and y coordinates
#Get user input
R = input("Please enter a radius (m):")
R = float(R)

y = input("Please enter Northings (y):")
y = float(y)

x = input("Please enter Eastings (x):")
x = float(x)

Lon0 = input("Please enter origin of Longitude (in decimal degrees):")
Lon0 = float(Lon0)

Lat0 = input("Please enter origin of Latitude (in decimal degrees):")
Lat0 = float(Lat0)

#Get latitude and longitude of points
D = float(y) / float(R) + float(Lat0)
xR = float(x) / float(R)

lat = math.asin(math.sin(D) * math.cos(xR))
lat = math.degrees(lat)

lon = math.radians(Lon0) + math.atan(math.tan(xR) / math.cos(D))
lon = math.degrees(lon)

#Output latitude and longitude
print("Inverse transformation: \nThe latitude of the point in decimal degrees is: ", round(lat,4), "(rounded)","\nlatitude unrounded:",lat, "\nThe longitude of the point in decimal degrees is ", round(lon,4),"(rounded)", "\nlongitude unrounded:", lon)

#Forward transformation to obtain x and y
B = math.cos(math.radians(lat)) * math.sin(math.radians(lon)- math.radians(Lon0))

x = R * math.asin(B)

    #break down formula for y
tanlat = math.tan(math.radians(lat))
coslon = math.cos(math.radians(lon) - math.radians(Lon0))

y = R * (math.atan(tanlat/coslon) - Lat0)

#Output x and y
print("Forward transformation:\ny is:",round(y,2),"(rounded)","\ny unrounded:",y, "\nx is:", round(x,2),"(rounded)", "\nx unrounded:",x)


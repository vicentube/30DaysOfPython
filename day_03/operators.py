# Day 3 of 30 Days Of Python

age = 50                # 1
height = 1.80           # 2
complex_number = 2 + 3j # 3

print('*** Area of a triangle ***') # 4
base = int(input('Enter base: '))
height = int(input('Enter height: '))
area = 0.5 * base * height
print('The area of the triangle is', area)

print('*** Perimeter of a triangle ***') # 5
a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
perimeter = a + b + c
print('The perimeter of the triangle is', perimeter)

print('*** Area and perimeter of a rectangle ***') # 6
length = int(input('Enter length: '))
width = int(input('Enter width: '))
area = length * width
perimeter = 2 * (length + width)
print('The area of the rectangle is', area, 'and its perimeter is', perimeter)

import math # 7
print('*** Area and circumference of a circle ***')
radius = int(input('Enter radius: '))
area = math.pi * (radius ** 2)
circum = 2 * math.pi * radius
print('The area of the circle is', area, 'and its circumference is', circum)

slope1 = 2 # 8
xinter1 = 1
yinter1 = -2

x1 = 2 # 9
y1 = 2
x2 = 6
y2 = 10
slope2 = (y2 - y1)/(x2 - x1)
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print('Slope is', slope2, 'and distance is', distance)

print('Calculated slopes are equal:', slope1 == slope2) # 10

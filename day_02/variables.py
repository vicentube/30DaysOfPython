# Day 2: 30 Days of python programming

# Level 1

first_name = 'John'
last_name = 'Smith'
full_name = 'John Smith'
country = 'USA'
city = 'New York'
age = 50
year = 2000
is_married = False
is_true = True
is_light_on = True
one, two, three = 1, 2, 3

# Level 2

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(one), type(two), type(three))

print(len(first_name))

print('First name length: ', len(first_name))
print('Last name length: ', len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
print(num_one)
print(num_two)
print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

import math
radius_str = input('Enter the circle radius in m: ')
radius = int(radius_str)
area_of_circle = math.pi * (radius ** 2)
print('Area of a', radius, 'm radius circle is:', area_of_circle, 'm^2')
circum_of_circle = 2 * math.pi * radius
print('Circumference of a', radius, 'm radius circle is:', circum_of_circle, 'm')

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country = input('Enter your country: ')
age = input('Enter your age: ')
print(first_name, last_name, 'is', age, 'years old and lives in', country)
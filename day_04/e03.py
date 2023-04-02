# 3
company = 'Coding For All'

#4
print('company:', company)

#5
print('len(company):', len(company))

#6
print('upper():', company.upper())

#7
print('lower():', company.lower())

#8
print('capitalize():', company.capitalize())
print('title():', company.title())
print('swapcase():', company.swapcase())

#9
print('Cut out first word:', company[7:])

#10
print('Contains Coding:', company.find('Coding') != -1)

#11
print('Replacing Coding for Python:', company.replace('Coding', 'Python'))

#12
str = 'Python for Everyone'
print(f'Replace Everyone to All in {str}:', str.replace('Everyone', 'All'))

#13
print('split(\' \'):', company.split(' '))

#14
str = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(f'Split "{str}" at the comma:', str.split(', '))

#15
print('Character at index 0:', company[0])

#16
print('Last index:', len(company) - 1)

#17
print('Character at index 10:', company[10])

#18
str = 'Python For Everyone'
words = str.split(' ')
letter1 = words[0][0]
letter2 = words[1][0]
letter3 = words[2][0]
acronym = [letter1, letter2, letter3]
print(f'Acronym for "{str}":', ''.join(acronym))

#19
str = 'Coding For All'
words = str.split(' ')
letter1 = words[0][0]
letter2 = words[1][0]
letter3 = words[2][0]
acronym = [letter1, letter2, letter3]
print(f'Acronym for "{str}":', ''.join(acronym))

#20
print('Position of first occurrence of \'C\':', company.index('C'))

#21
print('Position of first occurrence of \'F\':', company.index('F'))

#22
str = 'Coding For All People'
print(f'Position of the last occurrence of \'l\' in "{str}":', str.rfind('l'))

#23

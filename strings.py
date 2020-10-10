name = 'Brad'
age = 33

#Concatenate
# print('Hello I am ' + name + ' and I am ' + str(age))

# String Formatting
# Arguments By Position
# print('{0} {2} {0} {1}'.format('a', 'b', 'c'))

#Arguments by Name
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (only in 3.6+)
print(f'My name is {name} and I am {age}')

#string methods
s = 'hEllo there world'

#Capitalize first letter
print(s.capitalize())

#Capitalize every letter
print(s.upper())

#Lowercase every letter
print(s.lower())

#Swapcase
print(s.swapcase())

#Get length
print(len(s))

#Repalce
print(s.replace('world', 'everyone'))
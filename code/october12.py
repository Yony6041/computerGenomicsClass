import math
import re

# Diferent ways to define a function in python
def f(x,y):
    z = x**2 + y**2
    return z
r = f(0.705, 0.705)

lambaFunction = lambda x,y: x**2 + y**2

l = [1,2,3,4,5]
k = [x**2 for x in l]

# This is a regular expresion
p = re.compile('01[01]00')

pat1 = re.compile('Genomica')

pat2 = re.compile('Computacional')

#To find a pattern in a string
def find(pattern, chain):
    val = 'v' if re.match(pattern,chain) else 'n'
    if(val =='v'):
        return True
    else: 
        return False

findPattern = lambda pattern, chain: True if re.match(pattern, chain) else False

print(str(r))
print(l)
print(k)
print(type(p))
print(str(lambaFunction))
print('v' if re.match(pat1,'Genomica') else 'n')
print(find(r'G[aeiou]nomica', 'Genomica'))
print(findPattern(r'G[aeiou]nomica', 'Genomica'))





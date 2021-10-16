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


# match() is re at the beggining of the string?
# search() Scans trough the chain the times re appears
# findall() Returns a list of all the substrings where re is
# finditer() Returns an iterator, you can use it with next()
# group() Returns a string find by re
# start() Returns the first occurance of the re
# end() Returns the last position of the occurance
# span() Returns a tuple with (start, end) of the occurance of re
# search
search2 = lambda pattern, chain: 'Its here!' if re.search(pattern, chain) else 'It aint heeere'

print(search2(pat2, 'Genomica Computacional'))


adn_bci = 'ATTCCTA TTACTGT GCTTACAA 01001 GATTACA'

pat = r'\d\d\d\d\d'

print(re.search(pat, adn_bci))
v = re.search(pat, adn_bci)
print(v.start())
print(v.end())
print(adn_bci[v.start():v.end()])

print(re.findall(r'\D+', adn_bci))
pat = r'\D\D\D\D\D\D'
iterator = re.finditer(pat, adn_bci)
print(re.finditer(pat, adn_bci))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


pattern = r'(TTA){2,}'

dnaChain = 'ATTCTTATTACTA TTGTTGTTGTTTCCTGTGCTTACAA'
pat = r'TT..T'
print('finding the pattern TT..T in' + dnaChain)
iterator = re.finditer(pat, dnaChain)
print(next(iterator))
print(next(iterator))
print(next(iterator))


cad = 'ATTCTTATTACTA TTGTTGTTGTTTCCTGTGCTTACAA TTCTTCTTCA'
pat = r'(TT.){2,3}'

iterator = re.finditer(pat,cad)
print(re.findall(pat,cad))

#print(list(iterator))



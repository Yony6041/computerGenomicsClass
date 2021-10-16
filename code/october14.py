import re

#Inheritance in python 

#regular class constructor 
class dog(object):
    def __init__(self):
        pass
    def bark(self):
        if(self.size == 'big'):
            return 'WOOF!'
        elif(self.size == 'medium'):
            return 'Woof!'
        elif(self.size == 'little'):
            return 'awa awa!'
        else:
            return None

class cat(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size


# instance of a class
p = dog()

miel =  cat('miel', 'little')


telefonos = ['553-191-1122', '(55)-3451-9932', '9323-123-39391', 'A22-2924-1914', '(432)3-43321']
pat1 = r'(\d{3}-){2}\d{4}'
pat2 = r'\(\d\d\)(-\d{4}){2}'
patron = pat1 + "|" + pat2
for tel in telefonos:
    print("Examinando {}".format(tel))
    print(re.match(patron,tel))
    
correos = ["sergiohzlz@gmail.com", "sergiohzlz @ gmail.com", "marisol@ciencias.unam.mx", "daniel@ciencias", "naye@ciencias.unam.mx", " naye@ciencias.unam.mx ", "099@x.com"]
correos.append('berithyjr@gmail.com')
print(correos)
correos.pop()
print(correos)
pat = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
for cor in correos:
    print("Examinado {} ".format(cor))
    print(re.search(pat, cor))


class A():
    a=1
    print(f'this is not in init:{a}')
    def __init__(self):
        self.b = 2
        print(f'this is in init a: {self.a}  b:{self.b}')
    def test(self):
        self.d =222
    
    @property                                                      
    def price(self): #查看属性值                                           
        print ('@property ') 


a = A()
A.a = 10

b = A()

b.a = 20
print(b.a)
print(a.a)
A.c = 123
print(b.c)

b.test()
print(b.d)


class AnimalClassic:
    pass

#此为新式类，Python 2.2始支持
class Animal(object):
    pass

print(dir(AnimalClassic))
print(dir(Animal))
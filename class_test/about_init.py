
class A():
    a=1
    print(f'this is not in init:{a}')
    def __init__(self):
        self.b = 2
        print(f'this is in init a: {self.a}  b:{self.b}')


a = A()
A.a = 10
A.c = 123
b = A()

b.a = 20
print(b.a)
print(a.a)
print(b.c)

class A:
    pass

class B(A):
    def show(self): 
        print("B")

class C(A):
    def show(self): 
        print("C")

class D(B, C): # always start form the left
    pass

d = D()
print(D.__mro__)
print(d.show())

# D -> B -> C -> A


# super()

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

c = C()
c.show()

# A -> B -> C -> A

# super() with arguments

class A:
    def show(self, x):
        print("A")
        print(x)

class B(A):
    def show(self, x):
        print("B")
        super().show(x)

class C(A):
    def show(self, x):
        print("C")
        super().show(x)

c = C()
c.show(10)

# A -> B -> C -> A


# super() with arguments and keyword arguments

class A:
    def show(self, x, y=10):
        print("A")
        print(x)
        print(y)

class B(A):
    def show(self, x, y=10):
        print("B")
        super().show(x, y)

class C(A):
    def show(self, x, y=10):
        print("C")
        super().show(x, y)

c = C()
c.show(10, 20)

# A -> B -> C -> A


# super() with arguments and keyword arguments

class A:
    def show(self, x, y=10):
        print("A")
        print(x)
        print(y)

class B(A):
    def show(self, x, y=10):
        print("B")
        super().show(x, y=20)

class C(A):
    def show(self, x, y=10):
        print("C")
        super().show(x, y=20)

c = C()
c.show(10, 20)

# A -> B -> C -> A  

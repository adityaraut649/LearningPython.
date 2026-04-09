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




class A:
    def show(self):
        print("This is A")


class B(A):
    def show(self):
        super().show()   # calling parent method
        print("This is B")


b = B()
b.show()
#This is A.  , This is B


print("----------super() with Constructor (__init__)--------------")


class A:
    def __init__(self):
        print("A constructor")


class B(A):
    def __init__(self):
        print("B constructor")
        super().__init__()


b = B()


print("----------Multiple Inheritance - methods calling--------------")


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


class D(B, C):
    def show(self):
        print("D")
        super().show()


d = D() # D B C A
d.show()


class A:
    def show(self):
        print("This is A")


class B(A):
    def show(self):
        print("This is B")


class C(A):
    def show(self):
        print("This is C")


class D(B, C):
    pass


# Creating an instance
d = D()
d.show()  # Output: This is B


print(D.__mro__)



print("----------------------------------------")


class A:
    def __init__(self):
        print("A is initialized")


class B(A):
    def __init__(self):
        super().__init__()
        print("B is initialized")


class C(A):
    def __init__(self):
        super().__init__()
        print("C is initialized")


class D(B, C):
    def __init__(self):
        super().__init__()
        print("D is initialized")


# Creating an instance
d = D()


print("_------------------------------------")


class A:
    pass


class B(A): 
    pass
class C(A): 
    pass


class D(B, C): 
    pass
class E(C): 
    pass


class F(D, E): 
    pass


print(F.mro())

# F D B E C A Obj
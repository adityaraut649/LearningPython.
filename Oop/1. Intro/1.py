# polymorphism

#1.  What is the polymorphism?
#ans: Polymorphism is the ability of an object to take on many forms.

#2. What is the difference between inheritance and polymorphism?
#ans: Inheritance is the ability of an object to take on many forms. Polymorphism is the ability of an object to take on many forms.

#3. Type of polymorphism?
#ans: 1. Duck typing
#     2. Method overriding
#     3. Method overloading
#     4. Operator overloading

print('----------Method Overriding(Runtime Polymorphism)----------')

# 1. Method Overriding
# ans: when a method is overridden, the method in the child class will be called instead of the method in the parent class.

class Perent:
    def Marry(self):
        print('I married in the age of 18')

class Child(Perent):
    def Marry(self):
        print('I married in the age of 21')
        
p = Perent()
c = Child()

p.Marry()
c.Marry()

print('----------Method Overloading(Compile Time Polymorphism)----------')
# Python doesn't support ture method overloading

class Perent:
    def Marry(self):
        print('I married in the age of 18')
    def Marry(self, age):
        print('I married in the age of', age)

p = Perent()
# p.Marry() error
p.Marry(23)
p.Marry(21)


# Using *args(0 .... n) list (Flexiable Argument , functional Arguments)

class Math:
    def add(self, *args):
        return sum(args)
    

m = Math()
print(m.add(1, 2, 3, 4, 5))
print(m.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# is method overloading supported in python?
# ans: No, it is not supported in python.

# in oreder to overcome this problem, we can use *args(0 .... n) list (Flexiable Argument , functional Arguments)






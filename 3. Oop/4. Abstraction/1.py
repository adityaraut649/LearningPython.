## Abstraction
# def: Abstraction is the process of hiding details and showing only essential features of an object.
#In Python, this is primarily achieved using Abstract Base Classes (ABC)

# Abstraction Classes Definition: An "incomplete class" that cannot be instantiated (you cannot create an object of this class).

#Abstract Method
#Definition: A method that has a declaration but no body/implementation (usually just has the pass keyword).

#Concrete Method
#Definition: A regular method that has a complete body and implementation.

print('----------Abstract Base Class(ABC)----------')
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def payment(self):
        pass

class Cash(Payment):
    def pay(self):
        print('Cash')

    def payment(self):
        print('Payment')

c = Cash()
c.pay()
c.payment()


print('----------Abstract Class(ABC)----------')
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
    
    # concrete method
    def payment(self):
        print('Payment')

class Cash(Payment):
    def pay(self):
        print('Cash')

c = Cash()
c.pay()
c.payment()







# This is a Decorater function

def smartdiv(func): 
    def innner(a, b):
      if b == 0:
         print("This is not divisiable form zero")        
      else:
         return func(a ,b)
    return innner 

@smartdiv
def div(a ,b):
    return a / b

div(10, 2)
div(10, 3)
div(10, 0)
My_list = [1, 2, 3, 4, 5]

def multiply():
    result = []
    for i in My_list:
        result.append(i ** 2)
    return result

print(multiply())

print("-----------------------")

def even():
    result = []
    for i in My_list:
        if i % 2 == 0:
            result.append(i)
    return result

print(even())

print("-----------------------")

def total_sum():
    total = 0
    for i in My_list:
        total = total + i
    return total

print(total_sum())


print("---------------------------Map----------------------------")
num = [1,2,3,4,5,6,7,8,9]
def double(x):
    return 2 * x
squares = list(map(double, num))
print(squares)

print("---------------------------Lamda----------------------------")

num = [1,2,3,4,5,6,7,8,9]
squares = list(map(lambda x: x * 2, num))
print(squares)


print("---------------------------Filter----------------------------")
num = [1,2,3,4,5,6,7,8,9]
def even(x):
    return x % 2 == 0
result = list(filter(even, num))
print(result)


print("---------------------------Lamda----------------------------")

num = [1,2,3,4,5,6,7,8,9]
result = list(filter(lambda x: x % 2 == 0, num))
print(result)

print("---------------------------reduce----------------------------")

from functools import reduce
num = [1,2,3,4,5,6,7,8,9]

def sum(a, b):
    return a + b

total = reduce(sum, num)
print(total)


print("---------------------------Lamda----------------------------")

num = [1,2,3,4,5,6,7,8,9]

total  = reduce(lambda x , y : x + y ,  num)
print(total)


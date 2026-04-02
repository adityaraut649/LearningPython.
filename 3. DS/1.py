# Lists Operations

# 1. create a list
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. print the list
print(list1)
print(list2)
print(list3)

# 3. length of the list
print(len(list1))
print(len(list2))
print(len(list3))

# 4. indexing
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])

# 5. indexing
list1[0] = 10
list1[1] = 20
list1[2] = 30
list1[3] = 40
print(list1)


# 6. delete index
del list1[0]
del list1[1]
print(list1)

# 7. for loop
for i in range(len(list1)):
    print(list1[i])
    

# 8. for loop 
for i in range(len(list1)):
    print(list1[i])
    list1[i] = list1[i] + 10
    

# list sclice 

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0:5])
print(nums[5:10])

# list sclice
num2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num2[0:5:2])
print(num2[5:10:2])

# list sclice
num3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = num3[0:5:2]
print(res)

num4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ams = num4[::2]
print(ams)

num5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ams = num5[1::2]
print(ams)





   

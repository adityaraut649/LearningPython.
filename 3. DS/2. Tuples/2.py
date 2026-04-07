# Tuples

# 1. create a tuple
tup1 = (1, 2, 3, 4, 5)
tup2 = ("a", "b", "c", "d", "e")
tup3 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(tup1)
print(tup2)
print(tup3)

# 2. print the tuple
print(len(tup1))
print(len(tup2))
print(len(tup3))

# 3. indexing
print(tup1[0])
print(tup1[1])
print(tup1[2])
print(tup1[3])

# 4. indexing
tup1[0] = 10
tup1[1] = 20
tup1[2] = 30
tup1[3] = 40
print(tup1)

# 5. delete index
del tup1[0]
del tup1[1]
print(tup1)

# 6. for loop
for i in range(len(tup1)):
    print(tup1[i])
    
# 7. for loop 
for i in range(len(tup1)):
    print(tup1[i])
    tup1[i] = tup1[i] + 10
    


         

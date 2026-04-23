# read file
# write file
# append file
# r


file = open("./demo.txt", "r")
print(file) #Object
print(file.read())
file.close()


with open("./demo.txt", "r") as f:
     li = f.readlines()
     l2 = f.readlines()
     print(li)
     print(l2)

with open("./demo.txt", "r") as f:
     li = f.readline()
     l2 = f.readline()
     print(li)
     print(l2) 

# Read file
with open("./demo.txt", "r") as f:
    print(f.read())

# Read lines twice properly
with open("./demo.txt", "r") as f:
    li = f.readlines()
    f.seek(0)
    l2 = f.readlines()
    print(li)
    print(l2)

# Read line by line
with open("./demo.txt", "r") as f:
    li = f.readline()
    l2 = f.readline()
    print(li)
    print(l2)

# Write (overwrite)
with open("./demo.txt", "w") as f:
    f.write("HI I AM KIN\n")

# Append
with open("./demo.txt", "a") as f:
    f.write("HI I AM FIX\n")

with open("./demo.txt", "a") as f:
    f.write("HI I AM GIN\n")


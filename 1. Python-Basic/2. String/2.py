# String Operations
s1 = "Hello"
s2 = "World"

s3 = s1 + s2
print(s3)

s4 = s1 + " " + s2
print(s4)

# Length of String
len(s1)
len(s2)
len(s3)
print(len(s4))

# Indexing
s1[0]
s1[1]
s1[2]
s1[-1]
s1[-2]

# Slicing
s1[1:3]
s1[:3]
s1[1:]
s1[:-1]

# Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

d = a + b
print(d)

e = a + b + " "
print(e)

f = a + " " + b + " "
print(f)

g = a + " " + b
print(g)

h = a + " " + b + " "   
print(h)

#Combining Strings
a = "Hello"
b = "World"
c = a + " " + b
print(c)

d = a + b
print(d)

e = a + b + " "
print(e)

f = a + " " + b + " "
print(f)

g = a + " " + b
print(g)

h = a + " " + b + " "   
print(h)

#String Methods
str.lower(s1)
str.upper(s1)
str.title(s1)
str.strip(s1)
str.split(s1)
str.join(s1)
str.replace(s1, s2)     
str.count(s1, s2)
str.find(s1, s2)
str.index(s1, s2)
str.startswith(s1, s2)

print(s1.lower())
print(s1.upper())
print(s1.title())
print(s1.strip())
print(s1.split())
print(s1.join())
print(s1.replace(s2))
print(s1.count(s2))
print(s1.find(s2))
print(s1.index(s2))     
print(s1.startswith(s2))

#Multiline String
s1 = """Hello
World"""
print(s1)

s2 = """
Hello
World
"""
print(s2)

# String Formatting
name = "John"
age = 25
print("My name is %s and I am %d years old" % (name, age))

# String Interpolation
name = "John"
age = 25
print(f"My name is {name} and I am {age} years old")

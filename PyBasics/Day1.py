from traceback import print_tb

x=5
y=3
print(x+y)

x = "Hello"*3
print(x)

x = 5
if x == 5:
    print("x is 5")
else:
    print("x is not 5")

#Walrus operator example
x = 0
var = (x := 6)
print("x is 6", var)

#Example of using above operators
x= 4.6
result = (square := x**2) - (6.6/square)
print(result)

# Example of a SyntaxError
#print(y = 6)  # This will raise a SyntaxError
print(y:=6)  # This is valid syntax using the walrus operator


#how to see the memory address of a variable
print(id(x))  # This will print the memory address of x

x = 5
y = x
print(id(x),id(y))  # Memory address of x

# Example of a binary
x = bin(65)
print("Binary value of 86 -->> ",x)

print('----------------------------------------------------')

#Example of division operation using single slash
x = 5
print('Division operation example -->> ',5/2)  # This will print 2.5

print('----------------------------------------------------')

#Example of division operation using double slashw11`

x= 5
print('Floor division operation example -->> ',-5//2)  # This will print 2

print('----------------------------------------------------')

# Python
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

#Some keywords in Python
# and as assert break class continue def del elif else except finally for from global if import in is
# lambda nonlocal not or pass raise return try while with yield

# Example of nonlocal keyword

def outter() :
    x= 10

    def inner():
        nonlocal x
        x += 5
        print(x)

    inner()
    print("Outter x is", x)

outter()


# Example of string
text = "Hello, World!"
print(text[0])  # Prints 'H'
print(text[7:12])  # Prints 'World'
print(text[-1])  # Prints '!'

# Example using list

l = [1, 2, 3, 4, 5]
print(l[0])  # Prints 1
print(l[1:3])  # Prints [2, 3]
print(l[-1])  # Prints 5

# Example using tuple
cities = ("New York", "Los Angeles", "Chicago")
print(cities[0])

#example using list
cities = ["New York", "Los Angeles", "Chicago"]
print(cities[-1])  # Prints 'New York'

cities += ["Houston", "Phoenix"]
cities.append("San Diego")
print(cities)


#shallow and deep copy example
import copy
original_list = [1, 2, [3, 4], 5]
shallow_copied_list = copy.copy(original_list)
deep_copied_list = copy.deepcopy(original_list)
shallow_copied_list[2][0] = 'changed'
deep_copied_list[2][1] = 'changed'
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)
print("Deep Copied List:", deep_copied_list)


#floor division example
x = 5
print(x//2)
print(x/2)
print(x % 2)

print(x**2)

str1 = "Sudip"
str2 = "Sudip"
print(str1 == str2)  # True, because the content is the same















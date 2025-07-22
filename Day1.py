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
print('Floor division operation example -->> ',5//2)  # This will print 2

print('----------------------------------------------------')




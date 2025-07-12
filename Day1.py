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


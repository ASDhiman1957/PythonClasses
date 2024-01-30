# Typecasting 
a = 50
b = 10
print(a+b)

a = "amitoj "
b = " singh"
print(a+b)

a = "50"
b = "10"
print(a*b)

a = 50
b = 10
print(a +b)

a = "15"
b = "7"
# c  = int(a) #throws an error if the string is not a valid integer
print(int (a )  +  int(b))
# Implicit TypeCasting 
# this is an integer type 
a = 10  
# this is a float type 
b =20.6
# It convert it into float type 
c = a+b
print(" c is which  type  ",type(c))  
print(" b is which type ", type(b))
print(" a is which type ",type(a))

# Implicit typecasting
num_int = 5         # Integer
num_float = 2.5     # Float

result = num_int + num_float   # Implicit typecasting: int is converted to float
print(result)
# if else statemnets 
a = int(((input("enter the number "))))
print("Your age is ",a)

print(a>20)
print(a<=20)
print(a==20)
if a>=20:
    print("you should drive the car")
else:
    print("you should not drive the car")

# applePrice = 210
# budget = 200
# if (applePrice <= budget):
#     print("Alexa, add 1 kg Apples to the cart.")
# else:
#     print("Alexa, do not add Apples to the cart.")

# elif statements 
n = 0
if (n < 0):
    print("Number is negative.")
elif (n == 0):
    print("Number is zero.")
else:
    print("Number is positive .")

print("I am happy now ")

# 2nd program
# Nested if Statements
num = 10
if(num>10):
    print("this is true ")
elif(num==10):
    if(num<=5):
        print("this number is lies between 1-10")
    elif(num>10 and num<20):
      print("this number is lies between 11-20")
    else:
         print("this number is greater than 20")       

else:print("this number is greater than zero")
# match case
# x = int(input("enter the number"))
# match x:
#     case 0 :
#         print("x is zero ")
#     case 4:
#         print(" case is 4")
#     case _ if x != 90:
#        print(x," is not 90")
#     case _ if x != 80:
#        print(x , " is not 80")
#     case _:
#        print(x)

a = int(input("eneter the number"))
match a :
    case 1:
        print("a is 1 ")
    case 2:
        print("a is 2")
    case _ if a ==  20:
        print(a , "is equal to 20")
    case _ if a!=20:
        print(a, "is mot equal to 20")
    case _:
        print(a)

        
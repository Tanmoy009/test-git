def add_fun(x,y):
    return x+y
def sub_fun(x,y):
    return x-y
def multi_fun(x,y):
    return x*y
def div_fun(x,y):
    return x//y
print("enter two number")
x= int(input("num1: "))
y= int(input("num2: "))
var = int(input("enter 1 to add, 2 to sub, 3 to multiply & 4 to division: "))

match var:
    case 1:
        print(add_fun(x,y))
    case 2:
        print(sub_fun(x,y))
    case 3:
        print(multi_fun(x,y))
    case 4:
        print(div_fun(x,y))
    case 5:
        print("nothing")

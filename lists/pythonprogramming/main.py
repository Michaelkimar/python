import operators
import others
import trig
# x=operators.add(12,34)

# print(x)
# y=operators.subtract(87,86)
# print(y)
# # another way to import :
# from operators import add
# x=add(3,4)
# print(x)

# z=others.cube(9)
# print(z)

operator=input("operator ")
if operator=="cube":
    num=eval(input("num: "))
    x=others.cube(num)
    print (x)

elif operator == "sin":
    angle=eval(input("angle in degrees "))
    sin_of_angle =trig.get_sine(angle)
    print(sin_of_angle)

elif operator == "tan":
    angle=eval(input("angle in degrees "))
    print(trig.get_tangent(angle))

elif operator == "cos":
    angle=eval(input("angle in degrees "))
    print(trig.get_cosine(angle))

else:
    num1=eval(input ("num 1: "))
    num2=eval(input("num 2: "))


    if operator=="+":
        x=operators.add(num1,num2)
        print(x)
    elif operator =="-":
        x=operators.subtract(num1,num2)
        print(x)
    elif operator=="*" or "x" or "X":
        x=operators.multiply(num1,num2)
        print(x)
    elif operator=="/":
        x=operators.divide(num1,num2) 
        print (x)





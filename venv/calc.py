from math import *
while True:
    print("Calculater")
    print("You want to add two number enter 'add' ")
    print("You want to Multiply two number enter 'multy' ")
    print("You want to devide two number enter 'devide' ")
    print("You want to sbtrat two nuber enter 'subs'")
    print("for Exit enter any other value")
    input_type=(input(":"))

    #additon
    if input_type=='add' :
        a=float(input("Input the first number :" ))
        b=float(input("Input the second number :"))
        print("answer is " ,a+b)
        break
    #Multification
    elif input_type=="multy" :
        a = float(input("Input the first number :"))
        b = float(input("Input the second number :"))

        print("answer is ", a * b)
        break
    #Devide
    elif input_type=="devide" :
        a = float(input("Input the first number :"))
        b = float(input("Input the second number :"))

        print("answer is ", a / b)
        break

    #Substraction
    elif input_type=="subs":
        a=float(input("Input the first number :" ))
        b=float(input("Input the second number :"))

        print("answer is " ,a-b)
        break

    else:
        print("-------------exit------------")
        print("Thank you")
        break









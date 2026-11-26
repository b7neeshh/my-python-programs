name=input("Hello friend what's your name? Enter your name here: ")
print("Nice to meet you",name)
print("Lets solve a maths problem in a calculator built by Bineesh")
first=int(input("Enter your first number: "))
second=int(input("Enter your second number: "))
addition=first+second
subtraction=first-second
multiplication=first*second
solve=input("What do you want to solve today? Addition,Subtraction,Multiplication,Division? Enter here: ").strip().lower()
if solve== "addition" :
    print("Your answer for addition is: ",addition)
elif solve== "subtraction" :
    print("Your answer for subtraction is: ",subtraction) 
elif solve== "multiplication" :
    print("Your answer for multiplication is",multiplication)    
elif solve== "division" :    
    if second== 0 :
        print("Division by zero is not possible")
    else :
        division=first/second
        print("Your answer for division is: ",division)
else:
    print("Invalid")            
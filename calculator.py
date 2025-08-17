import math
print("Welcome to the World of Calculations!")
i=1
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))  # Using float to allow decimal inputs
        except ValueError:
            print("Invalid input! Please enter a number.")

while i==1:
    print("What operation do you wish to perform: ")
    print(" 1.Division")
    print(" 2.Floor Division")
    print(" 3.Multiplication")
    print(" 4.Subtraction")
    print(" 5.Addition")
    print(" 6.Modulus")
    print(" 7.Power")
    print(" 8.Square root")
    print(" 9.Exit")
    choice=get_number("Enter your choice:")
    if choice >0 and choice <=9:


            answer=0


            if choice==5 :
                num1 = get_number("Enter first digit:")
                num2 = get_number("Enter the Second digit:")
                answer=num1+num2
                print(f"The answer is:", answer)
            elif choice==1:
                num1 = get_number("Enter first digit:")
                num2 = get_number("Enter the Second digit:")
                if num2 == 0:
                    print("Zero Division Error")
                else:
                    answer=num1/num2
                    print(f"The answer is:", answer)
            elif choice==3:
                num1 = get_number("Enter first digit:")
                num2 = get_number("Enter the Second digit:")
                answer=num1*num2
                print(f"The answer is:", answer)
            elif choice==4:
                num1 = get_number("Enter first digit:")
                num2 = get_number("Enter the Second digit:")
                answer=num1-num2
                print(f"The answer is:", answer)
            elif choice==6:
                num1 = get_number("Enter first digit:")
                num2 = get_number("Enter the Second digit:")
                answer=num1%num2
                print(f"The answer is:", answer)
            elif choice==2:
                num1 = get_number("Enter first digit:")
                num2 = get_number("Enter the Second digit:")
                answer=num1//num2
                print(f"The answer is:", answer)
            elif choice==7:
                num1 = get_number("Enter first digit:")
                num2 = get_number("Enter the Second digit:")
                answer=num1**num2
                print(f"The answer is:", answer)
            elif choice==8:
                num=get_number("Enter the digit:")
                if num<0:
                    print("Error")
                else:
                    answer=math.sqrt(num)
                    print(f"The answer is:", answer)
            elif choice==9:
                i=0


    else:
        print("Invalid choice")
print("Bye!Join us again soon")
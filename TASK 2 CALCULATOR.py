def add(a,z):
    return a+z
def subtract(a,z):
    return a-z
def Multiply(a,z):
    return a*z
def Divide(a,z):
    return a/z

print("Select Operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter Choice (1/2/3/4): ")
    
    if choice in['1','2','3','4']:
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number:"))
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1,num2)}")
            

        elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1,num2)}")

        elif choice == '3':
                    print(f"{num1} * {num2} = {Multiply(num1,num2)}") 

        elif choice == '4':
            if num2 !=0:
                print(f"{num1} / {num2} = {Divide(num1,num2)}")
            else:
                print("Error! Division by zero.")
                

        #Ask if the user wants anothercalculation
        next_calculation = input("Do you want to perform another calculation? (yes/no):")
        if next_calculation.lower() !='yes':
            break
    else:
        print("Invalid Input")

#Run the calculator
        calculator()       
        

                    

        

                        


    

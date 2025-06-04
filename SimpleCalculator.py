num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
operator=input("Enter the operator: ")
if operator=="+":
    print(f"The result is:{num1+num2}")
elif operator=="-":
    print(f"The resul is:{num1-num2}")
elif operator=="*":
    print(f"The resul is:{num1*num2}")
elif operator=="/" :
    print(f"The resul is:{num1/num2}") 
else:
    print("Invalid operator")
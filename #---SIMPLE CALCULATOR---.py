#---SIMPLE CALCULATOR---
history=[]


def calculate(a,b,op):
    if op == "+":
        return (a+b)
    elif op == "-":
        return (a-b)
    elif op == "*":
        return (a*b)
    elif op == "/":
        if b==0:
            print("Division not possible by 0")
        return (a/b)
    else:
        print ("Invalid Choice")
        

def show_history():
    if not history:
        print ("No Calculations Done")
    else:
        print("\n---Calculation History---")
        for h in history:
            print(h)
            

def calculator():
    print ("Smart Calculator")
    
    while True:
        print ("1. Calculate")
        print ("2. Show History")
        print ("3. Exit ")
        
        choice=input("Enter choice:")
        
        if choice =="3":
            print ("Thanks!")
            break
        
        elif choice=="2":
            show_history()
            continue
            
        elif choice == "1":
            try:
                a=float(input("Enter First Number:"))
                op=input("Enter operator(+,-,*,/):")
                b=float(input("Enter Second Number")) 
            except ValueError:
                print("Invalid Output")
                continue
            
            if op not in ["+","-","*","/"]:
                print("Invalid Operator")
                continue 
            
            
            result=calculate(a,b,op)
            output = "{} {} {} = {}".format(a, op, b, result)
            
            history.append(output)
            
            print("Result:",result)
        
        else:
            print("Invalid Choice")
            
calculator()
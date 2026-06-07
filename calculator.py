a,b=map(int,input("Enter two numbers: ").split())
op= input("Enter the operator(+,-,*,/): ")
if op=='+':
    print("Result:=",a+b)
elif op=='-':
    print("Result:=",a-b)
elif op=='*':
    print("Result:=",a*b)
elif op=="/":
    if b==0:
        print("cannot divide by zero")
    else:
        print("Result:=",a/b)
else:
    print("Invalid operator")
 
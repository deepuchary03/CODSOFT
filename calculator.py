print('Calculator:')
while True:
  print('OPERATIONS')
  print('1.Addition \n2.Substraction \n3.Multiplication\n4.Division\n5.Exit')
  print('enter your choice:')
  ch=input()
  
  if ch=="1":
    print("enter first number:")
    a=float(input())
    print("enter second number:")
    b=float(input())
    print('sUM:',(a+b))
  elif ch=="2":
    print("enter first number:")
    a=float(input())
    print("enter second number:")
    b=float(input())
    
  
    print('DIFFERENCE',(a-b))
  elif ch=="3":
    print("enter first number:")
    a=float(input())
    print("enter second number:")
    b=float(input())
    
    print('PRODUCT:',(a*b))
  elif ch=="4":
    print("enter first number:")
    a=float(input())
    print("enter second number:")
    b=float(input())
    
    print('DIVISION',(a/b))
  elif ch=="5":
    print('program is terminated')
    break
  else:
    print('invalid choice')
    continue


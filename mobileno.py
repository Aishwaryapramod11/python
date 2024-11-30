'''author:aishwarya
'''
def check_number():
     number=input("enter your number")
     length=len(number)
     if length==10:
         if number[0]=='7' or number[0]=='8 'or number[0]=='9':
           print("valid number")
         else:
          print("invalid number")
check_number()




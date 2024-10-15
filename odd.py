'''author:Aishwarya
date:15-10-24
python code for generating n order numbers'''
limit=int(input("enter the limit"))
odd_number=1
count=0
while count<limit:
    print(odd_number,"\t",end="")
    count+=1
    odd_number+=2

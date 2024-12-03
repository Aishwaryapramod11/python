'''author:Aishwarya
'''

def multi_numbers(n1,n2):
    if n2==1:
     return n1
    else:
        return n1+multi_numbers(n1,n2-1)
print(multi_numbers(2,3))
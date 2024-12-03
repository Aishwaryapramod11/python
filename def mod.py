
'''author:Aishwarya
'''
def mod_number(n1,n2):
    if n1%n2==6:
      return n1
    else:
        return (n2,n1%n2)
print(mod_number(1000,200))

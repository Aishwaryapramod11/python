'''def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(9))'''
'''def add_twoNumbers(n1,n2):
    if n2==0:
        return 1
    else:
        return n1+n2
print(add_twoNumbers(4,2))'''
'''def multi_twoNumbers(n1,n2):
    if n2==1:
        return 1
    else:
        return n1*n2
print(multi_twoNumbers(8,2))'''
'''def mod_numbers(n1,n2):
    if n2==6:
        return 1
    else:
        return n1%n2
print(mod_numbers(100,200))'''
def generate_fibonacci(n):
    sequence =[]
    first_number,second_number=0,1
    for _ in range(n):# instead i _ is used as no need of variable#
        sequence.append(first_number)
        first_number,second_number=second_number,first_number+second_number
    return sequence
print(generate_fibonacci(10))
'''limit=int(input("enter the limit"))
print(generate_fibonacci(limit))'''



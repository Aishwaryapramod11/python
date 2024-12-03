'''aishwarya
 3-12-24'''
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
#from user input
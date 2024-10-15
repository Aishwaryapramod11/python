'''
author:Aishwarya
date:15-10-24
python file to find the purchase amount
'''
purchase_amount=float(input("enter the purchase_amount:"))
if  purchase_amount>500:
    discount=purchase_amount*(20/100)
    Final_amount=purchase_amount-discount
    print("Final amount is:",Final_amount)
elif purchase_amount>=200 and purchase_amount<=500:
    discount=purchase_amount*(10/100)
    Final_amount=purchase_amount-discount
    print("final_amount is:",Final_amount)
else:
    Final_amount=purchase_amount
    print("final amount is:",Final_amount)




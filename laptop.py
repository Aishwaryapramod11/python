'''author:Aishwarya
date:19-11-24'''
inventory=[
    ("laptop",5,30000.00),
    ("headphones",3,8000.00),
    ("mouse",50,150),
    ("keyboard",20,100),
    ("monitor",10,1000)
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,unit_price=item
    stock_value=quantity*unit_price
    print(F"total value of item is:{stock_value}")
    print(item_name ,quantity,unit_price)
    if stock_value>highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_stock_value=item_name
print(f"highest stock value is:{highest_stock_value}")
print(f"item with higheststock value is {item_with_highest_stock_value}")


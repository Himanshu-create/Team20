"""
Imagine you have started up a small restaurant and are trying to make it easier to take and calculate orders. Since your restaurant only sells 9 different items, you assign each one to a number, as shown below.

i) Chicken Strips - $3.50
ii) French Fries - $2.50
iii) Hamburger - $4.00
iv) Hotdog - $3.50
v) Large Drink - $1.75
vi) Medium Drink - $1.50
vii) Milk Shake - $2.25
viii) Salad - $3.75
ix) Small Drink - $1.25

To quickly take orders, your program should allow the user to type in a string of numbers and then it should calculate the cost of the order. For example, if one large drink, two small drinks, two hamburgers, one hotdog, and a salad are ordered, the user should type in 5993348, and the program should say that it costs $19.50. Also, make sure that the program loops so the user can take multiple orders without having to restart the program each time.
"""
items = {1:3.50,2:2.50,3:4.00,4:3.50,5:1.75,6:1.50,7:2.25,8:3.75,9:1.25}
order = True
while(order):
    
    price = 0
    item = input()
    for i in item:
        price = price + items[int(i)]
    print(price)
    print("enter 1 for order or 0 to exist")
    n = int(input())
    if n ==0:
        order = False


    


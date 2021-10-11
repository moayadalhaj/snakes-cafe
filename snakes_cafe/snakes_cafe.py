print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
   """)

menu = {
    'Wings':0,
    'Cookies':0,
    'Spring_Rolls':0,
    'Salmon':0,
    'Steak':0,
    'Meat_Tornado':0,
    'A_Literal_Garden':0,
    'Ice_Cream':0,
    'Cake':0,
    'Pie':0,
    'Coffee':0,
    'Tea':0,
    'Unicorn_Tears':0
}

while True:
    order=input('> ')
    if order=='quit':
        break
    order=order.replace(" ","_")
    if order in menu:
        menu[order]+=1
        print(f'** {menu[order]} orders of {order} have been added to your meal **')
    else:
        print('This order not in our menu!')
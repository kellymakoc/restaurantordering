menu = [
    'Welcome to Mackey Cat restuarant.',
    '         Meun',
    'a. Fried Rice ---- $6.99',
    'b. Beef Noodles ---- $8.46',
    'c. Salad ---- $3.56',
    'd. PIZZA!! --- $1.99 per slice',
    'e. Pop --- $0.99 per can',
    'f. Soup ---- $5.49',
    'g. PASTA ---- #8.69',
    'h. Burger with fries ---- $7.89',
    ]

print(menu)
order_list = []
order = input("Please enter the food you want to order for your meal(Press done when you ordered all you want for your meal): ")
order_list.append(order)
print(order_list)
done = "done"
count = 0

while order != done:
    if order != done:
        order = input("Please enter the food you want to order for your meal(Press done when you ordered all you want for your meal): ")
        order_list.append(order)
        print(order_list)

    if order == done:
        order_list.remove(order)
        print(order_list)
        
final = input("Is there any changes you would like to make?")

if final == "yes":
    n = input("What is the change you would like to make? (add or remove) ")
    if n == "add":
        m = input("What do you want to add in your meal today?")
        order_list.append(m)
        print(order_list)
              
    elif n == "remove":
        m = input("What do you want to remove from your order in your meal today?")
        order_list.remove(m)
        print(order_list)

if final == "no":
    print(order_list)
    

#total_price = price_rice + price_beef + price_salad + price_pizza + price_pop
#tax = total_price*1.13
final_price = total_price + tax

num_rice = 3
price_rice = 5 
print("You ordered: ",order_list)
receipt = [
    ('---------------------------------------'), 
    ('|   Macket Cat Restuarant              |'),
    ('|   201 Town Centre Blvd               |'),
    ('|   Unionville                         |'),
    ('|   905- 493-8862                      |'),
    ('|   Server: Kelly                      |'),
    ('|                                      |'),
    ('|   Your Order:                        |'),
    ('| Item         Quantity      Sub-Total |'),       
    ]
for row in receipt:
    print(row)
#if doesnt work, change to print 
q = [
     ('|',' Fried Rice      ',num_rice,'       ',price_rice,'       |'),
     ('|',' Beef Noodles    ',num_beef,'       ',price_beef,'       |'),
     ('|',' Salad           ',num_salad,'      ',price_salad,'      |'),
     ('|',' Pizza           ',num_pizza,'      ',price_pizza,'      |'),
     ('|',' Pop             ',num_pop,'        ',price_pop,'        |'),
     ('|',' Total                              ',total_price,'      |'),
     ('|',' Tax(13%HST)                        ',tax,'              |'),
     ('|',' Final Total Price                  ',final_price,'      |'),
     ('|','                                                         |'),
     ('| Thank you for ordering! Have a nice day!                   |'),
     ('|Please enjoy the meal!                                      |'),
     ('|Where there is food, there is love <333 !!!                 |'),
     ('|------------------------------------------------------------|'),
     ]
for row in q:
    print(row)
tip = int(input("tip for 10%, 15%, 20% or 0%: "))
a = 1.1*(total_price +tax)
b = 1.15*(total_price +tax))
c = 1.2*(total_price +tax))
if tip == "10":
    print(a) 
elif tip == "15":
    print(b)
elif tip == "20":
    print (c)
else:
    print(final_price)
    
payment = int(input("\nHow would you like to pay? Press: \n 1.Cash \n 2. Credit card"))
if payment == 1:
    change = int(input("Enter the amount of cash you are giving: "))
    print("the change is: ",(change- final_price))
elif payment == 2:
    card = input("paying by Visa, Mastercard or American Express? ")
    code = input("Please enter pin: ")
    print("Transaction approved. no change is given when a credit card is used.")

 

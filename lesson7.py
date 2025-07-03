# Create a shopping chart programe that will continuously ask the user for a food-
# product and the price of that product
# Have an exit clause if the user wishes to stop adding more things to their cart
# At the end show the food iteams and the total cost to the user

food = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    
else:
    price = float(input(f"Enter the price of the{food}: R"))
    foods.append(food)
    prices.append(price)
    
    print("----- YOUR CART -----")
    
    for food in foods:
        print(food, end= "")
        
    for price in prices:
        total = total + prices
        
    print("\n")        
    print(f"Your total is: R(total)")        

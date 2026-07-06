foods=[]
prices=[]
while True:
    food=input("ENTER YOUR FOOD TO CART :( Q to quit ) :  ")
    if food.lower()=="q":
        break
    else:
        price=float(input("ENTER THE PRICE OF GIVEN FOOD : "))
        foods.append(food)
        prices.append(price)
print(foods)
print(f'{sum(prices)} total bill' )
        

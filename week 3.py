#Question 1


def calculate_discount(price, discount_percent):
    if discount_percent >= 20 and discount_percent < 100 :
        price=price - ((discount_percent / 100 )* price)
        return price
    else:
        return price

#question 2


def calculate_discount(price, discount_percent):
    if discount_percent >= 20 and discount_percent < 100 :
        price=price - ((discount_percent / 100 )* price)
        return price
    else:
        return price
    
price = int(input("Enter the original price: "))
discount_percent = int(input("Enter the discount percent: "))

print(calculate_discount(price, discount_percent))

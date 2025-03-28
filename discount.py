def calculate_discount(price, discount_percent):
    if (discount_percent >= 20):
        discounted_price = price - (price * discount_percent/100)
        return f"Your discounted price is Ksh {discounted_price}"
    else:
        return f"Your original price is Ksh {price}"
    
discount = int(input("What is your discount percentage? "))
value = int(input("What is the value of the good you are purchasing? Ksh "))

result = calculate_discount(value, discount)
print(result)

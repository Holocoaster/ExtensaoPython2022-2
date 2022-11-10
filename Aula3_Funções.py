   #Functions

#A segment to calculate 5% of the tax; keep it stored in the variable "tax", and display the result
price = 2999.90
tax = price *0.05
print(tax)


price2 = 100
tax2 = price2 *0.05
print(tax2)

#Function creation that is supposed to calculate a 5% tax

def calculate_tax(product_price):
  tax = product_price * 0.05
  return tax

  #Data used to apply and start the function above, which will be displayed in the console

  price = 299
  tax = calculate_tax(price)
  print(tax)
  
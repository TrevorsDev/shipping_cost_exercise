# shipping = input("Are you using Ground Shipping, Ground Shipping Premium, or Drone Shipping?")
# weight = float(input("Enter the weight of your item to find out the price of shipping your item."))

shipping = "drone"
weight = 5.5
shipping = shipping.lower().replace(" ", "")
price = float


# Ground shipping price based on weight
def ground_shipping_price(weight):

  match weight:
    case w if (w <= 2):
      price = w * 1.50 + 20.00
    case w if (2 < w <= 6):
      price = w * 3.00 + 20.00
    case w if (6 < w <= 10):
      price = w * 4.00 + 20.00
    case w if (10 < w):
      price = w * 4.75 + 20.00

  return "${:.2f}".format(price)


# Premium shipping
def premium_shipping_price(shipping):

  if shipping in ["groundshippingpremium", "groundpremium", "premium"]:
    price = 125.00

    return "${:.2f}".format(price) 


# Drone shipping
def drone_shipping_price(weight):

  match weight:
    case w if ( w <= 2 ):
      price = w * 4.50
    case w if ( 2 < w <= 6 ):
      price = w * 9.00
    case w if ( 6 < w <= 10 ):
      price = w * 12.00
    case w if ( w > 10 ):
      price = w * 14.25

  return "${:.2f}".format(price)


# Returns users choice of shipping based on shipping answer
def user_shipping_choice(shipping):

  shipping_message = ""

  if shipping in ["groundshipping", "ground"]:
    shipping_message = "The price of shipping your item is: " + str(ground_shipping_price(weight))
    print(shipping_message)
    return shipping_message 

  elif shipping in ["groundshippingpremium", "groundpremium", "premium"]:
    shipping_message = "The price of shipping your item is a flat rate charge of: " str(premium_shipping_price(shipping))
    print(shipping_message)
    return shipping_message

  elif shipping in ["droneshipping", "drone"]:
    shipping_message = "You chose the new delivery by drone! Your shipping rate by weight is: " + drone_shipping_price(weight)
    print(shipping_message)
    return shipping_message
  else:
    print("Please enter only one of the three options for shipping")
    return "Please enter only one of the three options for shipping"

user_shipping_choice(shipping)




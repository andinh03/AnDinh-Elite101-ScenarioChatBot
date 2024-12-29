from datetime import date
import datetime
today = date.today()
max_day = 60


print("Welcome to Austin Boutique ChatBot")
itemName = input("Please enter the item that you want to return (shirt, pants, dress, or shoes): ")
itemReceipt = input(f"Do you have the receipt for the {itemName}? (yes/no): ")

print(" ")

def returnQuestion():
  if itemReceipt == "yes":
    print("We will go ahead and check your purchase date \n")
    print("")

  elif itemReceipt == "no":
    print("Sorry, we can't return or exchange your item(s) without a receipt")
    exit()

def day_Allow():  
  purchaseDate = input("Please enter the date of purchase (mm/dd/yyyy): ")
  dateBuy = datetime.datetime.strptime(purchaseDate, "%m/%d/%Y").date()

  todayDate = today

#Calculate date difference
  dateDiff = int((todayDate - dateBuy).days)

  if dateDiff <= max_day:
      return ("We will go ahead and return or exchange the item.")
  else:
      return ("Sorry, We cannot return or exchange the item at the moment.")


def user_selection():  
  print("Please choose from the following options:")
  print("1. Return the item")
  print("2. Exchange the item")
  number = int(input("Enter the number of your choice: "))

  if number == 1:
      print("What is the reason for your return? ")
      reason_return = input("1. The item is damaged\n2. Wrong order item\n3. Wrong size\n")
      if reason_return == "1":
        print("Did the item get damaged after used?")
        damaged = input("1. Yes\n2. No\n")
        if damaged == "1":
          print("We will issue you the shop card")
        if damaged == "2":
          print("We will fully refund based on your order payment method!")
      elif reason_return == "2" or reason_return == "3":
        print("Did you paid by cash, card, or shop card?")
        payment = input("Cash\nCard\nShop Card\n\n")
        print(f"We will fully refund to your money as {payment}!")

  elif number == 2:
    print("What item that you need to exchange? ")
    item_exchange = input("1. Shirt\n2. Pants\n3. Dress\n\n")
    reason_exchange = input("1. The item is damaged\n2. Wrong order item\n3. Wrong size\n")
    if reason_exchange == "1":
        print(f"We will go ahead and exchange the new {itemName} for you")
    if reason_exchange == "2":
        print(f"We will go ahead and exchange the correct {itemName} for you")
    if reason_exchange == "3":
        print(f"We will go ahead and exchange the correct size of {itemName} for you")


returnQuestion()
day_Allow()
user_selection()
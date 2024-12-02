price_input = input("Enter your budget: ")
price = int(price_input)

if (price < 500):
  print("You can buy only a atar")
elif (price < 1999):
  print("You can buy thobe but can't buy pajama")
else:
  print("You can buy both")


if (price > 1000):
  print("You can go co'x bazar")
  if (price > 2000):
    print("You have money. If You wish, you can go seint martin")
  else:
    print("You have not enogh money. You should back to your home")
else: 
  print("You can't go co'x bazar")
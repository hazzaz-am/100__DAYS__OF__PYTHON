x = 20
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)



num = int(input("Enter match case: "))

match num:
  case 0:
    print("Num is Zero")
  case 1:
    print("Num is One")
  case _ if (num < 10):
    print("Num is less then 10")
  case _ if(num == 10):
    print("Num is equal to 10")
  case _ if(num < 20):
    print("Num is greater then 10 and less then 20")
  case _:
    print("Beyond 20")
ex = "Mango"

print(len(ex)) # 5

print(ex[0:5]) # Mango
print(ex[0:-5]) # nothing will be shown because length - 5 is 0

print(ex[:5]) # Mango. Because python automatic start slicing with 0

print(ex[0:]) # Mango. Becase python automatic end slicing to the end of the length of the word

print(ex[-1:5]) # o. Becase python minus the negative number from the length of the word then slice the word

print(ex[-4:-2]) # an

for i in ex:
  print(i)
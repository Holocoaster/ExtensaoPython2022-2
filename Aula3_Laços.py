#Laços

'''contador = 1
print(contador)
contador = contador+1 
print(contador)
contador += 1
print(contador)'''

#The variable counter (which equals to 1), will get +1 added to it, until it becomes <= 100, and that's when it stops

counter = 1

while counter <= 100:
  print(counter)
  counter = counter +1

  animals = ["Raccoon", "Elephant", "Mammoth"]

print(animals)

#print(animals[index number]) for selecting and printing an specific order from the list of animals

print(len(animals)) #Will literally print the number of the list's length, which is currently 3

#Adding a new item/animal that isn't in the list
animals.append("Frog")

print(animals)

print(len(animals)) #After adding Frog into the list, the new list length should be 4

i=0 #(i for index)
while(i<len(animals)):
  print(animals[i])
  i = i + 1


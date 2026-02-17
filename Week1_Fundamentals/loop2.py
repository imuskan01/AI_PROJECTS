# store names in a list
n = int(input('How many students are there in the class? '))
names = [0] * n # list initialise
print(names)

for i in range(n):
  print(i)
  names[i] = input("Enter your name: ")
print(names)
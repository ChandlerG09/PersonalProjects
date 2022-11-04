#Lists
groceries = ['apple', 'bread', 'cheese', 'milk']
#print all
print(groceries)
#print starting at index 2
print(groceries[2:])
#print first 3 items
print(groceries[:3])

#Loops
for x,y in enumerate(groceries):
    print('x value is: ' + str(x) + ' y value is: ' + str(y))
    if(x%2 == 0):
        print('Even indexed element = ' + y)
num = 0
while num != 10:
    if num%2 == 1:
        print(str(num))
    num = num+1

#Strings
myString = "Hello World"
print(myString[:4])
print(myString[4:])
print(myString[4:6])


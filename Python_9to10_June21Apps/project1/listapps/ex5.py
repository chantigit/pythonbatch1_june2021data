#II.Reading list elements from console
list1=list()
size=int(input('Enter size of list:'))
for i in range(size):
    list1.append(int(input('Enter an element:')))

print('List elements are:',list1)
print('Iterating elements using for loop (index based accessing)')
for i in range(size):
    print(list1[i])
print('Iterating elements using foreach loop(element based accessing)')
for i in list1:
    print(i)
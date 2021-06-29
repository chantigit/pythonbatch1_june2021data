#append(),insert() and 	extend()
myList1=list()
myList1.append(10)
myList1.append(9)
myList1.append(10)
myList1.append(15)
myList1.append(12)
print(myList1)
#  [10 9 10 15 12]
#   0  1  2 3  4
myList1.insert(1,100)
print(myList1)
myList2=[11,22,33]
myList1.extend(myList2)
print(myList1)
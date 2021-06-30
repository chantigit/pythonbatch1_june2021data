#items={'chicken biryani' :350, 'mutton biryani':450, 'veg Manchuria':200, 'chicken kebab':350,'chilli chicken':270, 'gobi munchuria':350,'chicken lollipop':380 }
n=int(input('enter number of items:'))
items=list()
for i in range(n) :
    items.append(int(input('enter item cost:')))

total=sum(items)

print(total)
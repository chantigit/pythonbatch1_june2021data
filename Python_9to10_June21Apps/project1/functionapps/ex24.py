#Zomato application

def itemsTotalPrice(*items):
    s=0
    for i in items:
        s=s+i
    return s

print(itemsTotalPrice(100,400,500))

#1.Coupons  2.Delivery chargers 3.Packing Charges 4.Discounts 5.Gst
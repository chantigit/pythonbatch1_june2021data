#Zomato application
def coupon10(dummyTotal):
    def inner(*items):
        res=dummyTotal(*items)-10
        return res
    return inner
def discountof5(dummyTotal):
    def inner(*items):
        total = dummyTotal(*items)
        discount=total-(total*5/100)
        return discount
    return inner

@discountof5
@coupon10
def itemsTotalPrice(*items):
    s=0
    for i in items:
        s=s+i
    return s

print(itemsTotalPrice(100,400,500))

# 1.Coupons ->10/-
# 2.Delivery chargers->15/-
# 3.Packing Charges -> 10/-
# 4.Discount  -> 5%
# 5.Gst  -> 18%
s1,s2,s3=80,90,75
total=s1+s2+s3
percentage=total/300*100
print(percentage)
if percentage > 70:
    print('A')
elif percentage < 70 and percentage > 60:
    print('B')
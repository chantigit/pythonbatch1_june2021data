#5.Bitwise operators (&, | , ^, ~, <<,>> )
a,b=12,14
'''      8 4 2 1
a=12  =  1 1 0 0
b=14  =  1 1 1 0
________________
a&b   =  1 1 0 0   = 12
a|b   =  1 1 1 0   = 14
a^b   =  0 0 1 0   =  2
'''
print(a&b) #12
print(a|b) #14
print(a^b) #2
print(~a)  #~n = +/- (n+1)  = -(12+1) =-13
print(~b)  #-15
print(a<<2)#n<<s = n * 2^s = 12 * 4   = 48
print(b>>3)#n>>s = n // 2^s = 14 // 8 = 1


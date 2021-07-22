from re import search,match,findall
s1=r'python has two parts core python and adv python'
res1=search('python',s1)
print(res1.group())    #If word found any where it retunrs first occurance

res2=match('python',s1)#If word found in the begining it retunrs that word
print(res2.group())

res3=findall('python',s1)
print(res3)

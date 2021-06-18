#balenq(),diposit(),withdraw()
accountNumber,amount=501,1000
def balenq():
    print(accountNumber,' account having ',amount ,'/- Amount')
def diposit(amt):
    global amount
    amount=amount+amt
    balenq()

diposit(4000)

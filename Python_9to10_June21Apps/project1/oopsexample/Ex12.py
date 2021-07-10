import abc
class Rbi(abc.ABC):
    def timings(self):
        print('Open@10am , Colsed@4pm')
    def holyDaysList(self):
        print('Weekly 5,All public,1 month vacc')
    @abc.abstractmethod
    def rateOfInterest(self):
        pass
class Sbi(Rbi):
    def rateOfInterest(self):
        print('Sbi decides roi=12%')
class Hdfc(Rbi):
    def rateOfInterest(self):
        print('Hdfc decides roi=10%')
class Axis(Rbi):
    def rateOfInterest(self):
        print('Sbi decides roi=8%')

bank1,bank2,bank3=Sbi(),Hdfc(),Axis()
print('---------------BANK1 Methods-----------------')
bank1.timings()
bank1.holyDaysList()
bank1.rateOfInterest()
print('---------------BANK2 Methods-----------------')
bank2.timings()
bank2.holyDaysList()
bank2.rateOfInterest()
print('---------------BANK3 Methods-----------------')
bank3.timings()
bank3.holyDaysList()
bank3.rateOfInterest()
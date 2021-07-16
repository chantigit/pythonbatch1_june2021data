class AgeBelowError(Exception):
    def __str__(self):
        return "Age Should be greater than 18"
class NegativeAgeError(Exception):
    def __str__(self):
        return "Age should be in positive"
class AgeAboveError(Exception):
    def __str__(self):
        return "Age should be less than 100"

def agecheckingforvoting(age):
    try:
        if age<0:
            raise NegativeAgeError()
        elif age>0 and age < 18:
            raise AgeBelowError()
        elif age>100:
            raise AgeAboveError()
        else:
            print(age, ' Age is valid for voting')
    except AgeBelowError as e:
        print(e)
    except NegativeAgeError as e:
        print(e)
    except AgeAboveError as e:
        print(e)
agecheckingforvoting(25)
agecheckingforvoting(16)
agecheckingforvoting(-16)
agecheckingforvoting(200)
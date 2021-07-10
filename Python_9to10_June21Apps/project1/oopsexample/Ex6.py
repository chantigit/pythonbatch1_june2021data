#PS1: Addition of 2 numbers using Static methods (2 Steps of code)
class Addition:
    #Preparing static method
    @staticmethod
    def doSum(n1,n2):
        res=n1+n2
        print('Sum is:',res)

#Calling method
Addition.doSum(120,23)
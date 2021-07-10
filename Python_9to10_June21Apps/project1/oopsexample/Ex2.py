class AmazonUser:
    def __init__(self,name,phone,email,pswd):  #SET DATA to OBJECT
        print('---CONSTRUCTOR---')
        self.name,self.phone,self.email,self.pswd=name,phone,email,pswd
    def __str__(self):                         #GET DATA from OBJECT in string format
        print('---STR---')
        return self.name+','+str(self.phone)+','+self.email+','+self.pswd
    def __del__(self):                         #REMOVE DATA with in OBJECT
        print('---DESTRUCTOR---')
        del self.name, self.phone, self.email, self.pswd

#Object creation
user1=AmazonUser('depak',9849098491,'deepu@gmail.com','Apple')
print(user1)  #user1.__str__()
user2=AmazonUser('sanju',9849098492,'sanjay@gmail.com','1234')
print(user2)  #user2.__str__()
user3=AmazonUser('ramkumar',9849098493,'ram@gmail.com','3443')
print(user3)  #user3.__str__()
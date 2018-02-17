'''
- there is a bank class with name address,zipcode and has a private data member
- there is a customer class too which inherits from bank class. has balance, withdraw and deposit fuctions
- there is a joint account class which inherits from both bank and customer class which has names of both the holders
   and also all other functions
- there is a complaint filing machine for filing complaints regarding displutes and gives an reuest number
- there is  a credit card class which inherits from customer class and has credit limit. there is also method averrding
   here
'''
class Bank(object):
    __name_of_bank = "Bank of xyz"  # Private Data Member


    def __init__(self,name,address,zip):            #construcor
        self.name=name
        self.address=address
        self.zip=zip
        print "Bank name: ", Bank.__name_of_bank  # displays school members

    # getters
    def getname(self):
        return self.name

    def getaddress(self):
        print self.name + " and is located at: " +self.address +" ,"+ str(self.zip)

class Customer(Bank):                                    # Inheriting from bank class
    c_count=0
    def __init__(self,name,address,zip,balance):
        Bank.__init__(self,name,address,zip)
        self.balance=balance
        Customer.c_count += 1

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.amount>self.balance:
            print "Your balance is not sufficient"
        else:
            self.balance -= amount

    def getbalance(self):
        return self.balance

    def no_customers(self):
        print "the number of customers are: "+Customer.c_count

    def c_display(self):
        print "the name of customer is" +self.getname()

class Joint_account(Customer,Bank):                            #multiple inheritance
    def __init__(self,first_person,second_person):
        super(Joint_account,self).__init__()                   # Using super class
        self.first_person=first_person
        self.second_person=second_person

    def get_names(self):
        print "the account names are: " +self.first_person + " and " +self.second_person

class Credit_Card:                                    # inheriting from customer class
    def __init__(self,credit_limit,name,address,zip):
        self.credit_limit=credit_limit

    def withdraw(self,amount):                                  # method overriding
        if amount>self.credit_limit:
            print "your credit limit exceeded"
        else:
            self.credit_limit -= amount

    def deposit(self,amount):
        self.credit_limit += amount

    def get_credit_limit(self):
        return self.credit_limit

class Complaint:
    complaint_id=0
    def __init__(self,name,id_type,acc_no):        # cid is complaint id type and acc_no is account number
        self.name=name
        self.id_type=id_type
        self.acc_no=acc_no

    def get_cmp(self):
        print "Hello " + self.name +" your complaint of id-type: " + str(self.id_type) +\
              " ,with account number: "+ \
              str(self.acc_no) + " is registered"

# instance for bank
b=Bank("bank of xyz","abc,Kansas City, Missouri",11111)
b.getname()
b.getaddress()

#creating instance for cutomer and showing 2000 deposit + intial balance 200 =2200
c=Customer("mani",4511,64110,200)
c.deposit(2000)
print c.getbalance()

# isntance for complaint
comp=Complaint("mani",15,"200123")
comp.get_cmp()

#instance for credit card
c=Credit_Card(3000,"mani","xxx,Kansas City,MO",64110)
c.withdraw(3100)




        







class Account:
    def __init__(self, balance, account):
        self.balance=balance
        self.account=account
    

    def Debit(self, ammount):
        self.balance -=ammount
        print("Rs",ammount,"was debited")
        print("Total balance", self.get_balance())


    def Creadit(self, ammount):
        self.balance += ammount
        print("Rs",ammount,"was creadited")
        print("Total balance", self.get_balance())

    def get_balance(self):
        return self.balance
    

acc1 =Account(10000, 432602120003758)

acc1.Creadit(40000)
acc1.Debit(5000)

class bank_account:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance
    def withdraw_money(self,money):
        if money<=0:
            print("You can not withdraw less than 0")
        elif money>self.__balance:
            print("You can not withdraw more than balance")
        else:
            self.__balance -= money   
            print("Please collect your cash!")

    def deposit_money(self,money):
        if money<0:
            print("You can not deposit negative amount")
        elif money==0:
            print("You can not deposit zero")
        else:
            self.__balance += money
            print("Amount deposited successfully!")

    def display_balance(self):
        return self.__balance

acc1=bank_account(23,70000)
acc1.withdraw_money(35000)
acc1.deposit_money(40000)
print (acc1.display_balance())     

class CurrentAccount:
    def __init__(self, owner_firstname, owner_lastname, balance=0):
        self.owner_firstname = owner_firstname
        self.owner_lastname = owner_lastname
        self.balance= balance
        self.transactions=[]
    
    def deposit(self, amount):
        self.balance= self.balance + amount
        Deposited = 'Deposit: ' + str(amount)
        self.transactions.append(Deposited)
        print(str(amount) + ' has been deposited in your account, your current balance is ' + str(self.balance))
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            Withdrawn = 'Withdraw: ' + str(amount)
            self.transactions.append(Withdrawn)
            print(str(amount) + ' has been credited from your account and the remaining balance is ' + str(self.balance))
            return True
        else:
            print('You do not have enough balance in your account') 
            return False


    def get_balance(self):
        return self.balance
    
    def transaction_history(self):
            for transaction in self.transactions:
                print(transaction)    
            return self.transactions
    
    @property
    def owner_fullname(self):
        return '{} {}'.format(self.owner_firstname, self.owner_lastname)
    
    def __str__(self):
        return '{} {}'.format(self.owner_fullname, self.balance)
    
class SavingsAccount(CurrentAccount):
    interest_rate = 0.05
    def __init__(self, owner_firstname, owner_lastname, balance=0 ):
        super().__init__(owner_firstname, owner_lastname, balance)
    
    def apply_interest(self):
        self.interestearned = self.balance * self.interest_rate
        self.balance = self.interestearned + self.balance
        interestbalance = 'Interest paid: ' + str(self.interestearned)
        self.transactions.append(interestbalance)
        print('You have been paid an interest of ' +  str(self.interest_rate) + ' your new balance is ' + str(self.balance))

class Bank():
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
    
    def find_account(self, owner_fullname):
        for account in self.accounts:
            if owner_fullname == account.owner_fullname:
                return account
        return 'Account not found'
    
    def transfer(self, from_name, to_name, amount):
        from_account = self.find_account(from_name)
        to_account = self.find_account(to_name)
        
        if from_account != 'Account not found':    
            success = from_account.withdraw(amount)
            if success == True:
                pass
            else: 
                return 'Insufficient Funds'
        else:
            return 'Sender account not found'
        
        if to_account != 'Account not found':
            to_account.deposit(amount)
        else:
            from_account.deposit(amount)
            return 'Recipient account not found'
        
        return 'Transfer Successful'

    def __str__(self):
        result = ''
        for account in self.accounts:
            result = result + str(account) + '\n'
        return result
             
        
    
        
currentaccountowner1 = CurrentAccount('Mike', 'Josh', balance= 3000)
currentaccountowner2 = CurrentAccount('Palina', 'Dekot')
savingsaccountowner1 = SavingsAccount('Michael', 'Jakeson', balance= 50000)
savingsaccountowner2 = SavingsAccount('Bob', 'Wither')
BankManagement = Bank()

BankManagement.add_account(currentaccountowner1)
BankManagement.add_account(currentaccountowner2)
BankManagement.add_account(savingsaccountowner1)
BankManagement.add_account(savingsaccountowner2)

currentaccountowner2.deposit(2500)
currentaccountowner2.withdraw(300)
savingsaccountowner1.apply_interest()

#print(BankManagement.find_account("Mike Josh"))
#print(BankManagement.find_account("Pike Nosh"))

#print(BankManagement.transfer('Mike Josh', 'Bob Wither', 10000))

#currentaccountowner2.transaction_history()
#savingsaccountowner1.transaction_history()

#print(currentaccountowner1.owner)
#print(currentaccountowner1.balance)
#print(currentaccountowner1)
#print(currentaccountowner2)
#print(savingsaccountowner1)
#print(savingsaccountowner2)
print(BankManagement)

#print(currentaccountowner2.owner)
#print(currentaccountowner2.balance)
#print(currentaccountowner2.transactions)
#print(currentaccountowner2.get_balance())

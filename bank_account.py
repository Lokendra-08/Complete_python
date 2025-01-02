class BankAccount:
    def __init__(self):
        self.customers= {}

    def add_account(self, acc_no, initial_balance=0):
        if acc_no in self.customers:
            print("-----------------------")
            print('Account already exists')
            print("-----------------------")

        else:
            self.customers[acc_no] = initial_balance
            print("-----------------------------")
            print("Account created successfully")
            print("-----------------------------")


    def deposit(self, acc_no, amount):
        if acc_no in self.customers:
            self.customers[acc_no] += amount
            print("------------------------------")
            print("Amount deposited successfully")
            print("------------------------------")
        else:
            print("----------------------")
            print("Account does not exist")
            print("----------------------")


    def withdraw(self, acc_no, amount):
        if acc_no in self.customers:
            if self.customers[acc_no] >= amount:
                self.customers[acc_no] -= amount
                print("------------------------------")
                print("Amount withdrawn successfully")
                print("------------------------------")
            else:
                print("--------------------")
                print("Insufficient balance")
                print("--------------------")

        else:
            print("----------------------")
            print("Account does not exist")
            print("----------------------")


    def check_balance(self, acc_no):
        if acc_no in self.customers:
            print("-----------------------")
            print(f"Balance: {self.customers[acc_no]}")
            print("-----------------------")

        else:
            print("-----------------------")
            print("Account does not exist")
            print("-----------------------")

bankaccount= BankAccount()
while True:
    answer = input("Press \nO to open new account\nD to deposit account \nW to withraw amount \nB to print balance \nQ to quit :\n")
    if answer.upper() == 'O':
        acc_no = input("Enter account number: ")
        initial_balance = int(input("Enter initial balance: "))
        bankaccount.add_account(acc_no, initial_balance)
    
    elif answer.upper() == 'D':
        acc_no = input("Enter account number: ")
        amount = int(input("Enter amount to deposit: "))
        bankaccount.deposit(acc_no, amount)

    elif answer.upper() == 'W':
        acc_no = input("Enter account number: ")
        amount = int(input("Enter amount to withdraw: "))
        bankaccount.withdraw(acc_no, amount)

    elif answer.upper() == 'B':
        acc_no = input("Enter account number: ")
        bankaccount.check_balance(acc_no)

    else:
        break
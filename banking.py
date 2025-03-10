import csv
import os

customer_accounts = [
    { 'account_id': 10001 ,  'first_name': 'suresh',   'last_name': 'sigera','password': '1234', 'balance_checking' : 1000, 'balance_savings': 10000 },
    { 'account_id': 10002 , 'first_name': 'james',  'last_name': 'taylor','password': 'idh36%@#FGd', 'balance_checking' : 10000, 'balance_savings': 10000 },
    ]

fieldnames = ["account_id", "first_name", "last_name", "password", "balance_checking", "balance_savings"]

if not os.path.exists("./banck.csv"):
    with open("./banck.csv", 'w', newline='') as csvfile:
        try:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in customer_accounts:
                writer.writerow(row)
        except csv.Error as e:
            print(e)

# 4.0 If Exists - ReadFile / Rows:
try: 
    with open("banck.csv", "r") as file:
        contents = csv.DictReader(file)
        # for row in contents:
        #     print(row) #will print: {'Name': 'The First Doctor', 'Actor': 'William Hartnell', 'Number of Episodes': '134'}
        #     for prop in fieldnames:
        #         print(row[prop]) # will print the value of each individual property
except csv.Error as e:
    print(e)



class Customer():

    def __init__(self,account_type, first_name, last_name, password):
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance_checking = None
        self.balance_savings = None
        self.account_id = 10002 #try use random and chech if it exist for the id
        self.logged_in = False
        self.current_useer = None

    def add_customer(self,new_account, fname, lname, password):

        if new_account == 1:
            self.balance_checking = 0
        elif new_account == 2:
            self.balance_savings = 0
        else:
            self.balance_checking = 0
            self.balance_savings = 0
        
        try:
            self.account_id += 1
            new_row = {'account_id': self.account_id, 'first_name': self.first_name, 'last_name': self.last_name, 'password': self.password,  'balance_checking': self.balance_checking, 'balance_savings': self.balance_savings}
            customer_accounts.append(new_row)
            with open("banck.csv", "a+") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(new_row)

        except csv.Error as e:
            print(e)
    
    @classmethod
    def log_in(self):
        user_name = input('enter your usre name: ')
        user_password = input('enter your paswword: ')

        for user in customer_accounts:
            if user['first_name'] == user_name and user['password'] == user_password:
                print(user['first_name'], user['password'])
                self.current_useer = user['account_id']
                self.logged_in = True
                return
        
        print("Invalid username or password. Please try again.")

# class checking_account(Customer):
# class savings_account(Customer):
# class checking_and_savings_account(Customer):


class Deposit(Customer):
    @classmethod
    def check_account(self):
        if not self.logged_in:
            print("You need to log in first!")
            return

        deposit_amount = float(input("Enter the amount of mony to be add: "))

        for user in customer_accounts:
            if user['account_id'] == self.current_useer:

                Deposit_type = int(input("Deposit into (1) Checking or (2) Savings? "))
                
                if Deposit_type == 1:
                    user['balance_checking'] += deposit_amount

                elif Deposit_type == 2:
                    user['balance_savings'] += deposit_amount

                else:
                    print("Invalid selection!")
                    return
                
                print("Deposit successful! Updated balance:", user)
                return
    


class Withdraw(Customer):

    def Withdraw_operation(self):
        if not self.logged_in:
            print("You need to log in first!")
            return

        if self.balance_checking != 0 and self.logged_in:
            Withdraw_amount = input("ente the amount of mony to be draw: ")
            for user in customer_accounts:
                if user['account_id'] == self.current_useer:
                    
                    Deposit_type = int(input("Deposit into (1) Checking or (2) Savings? "))
                if Deposit_type == 1:
                    user['balance_checking'] -= Withdraw_amount
                elif Deposit_type == 2:
                    user['balance_savings'] -= Withdraw_amount
                else:
                    print("Invalid selection!")
                    return
                

class Transfer():
    pass



# new_account = input('what kind of account you want to create? \n1: checking account\n2: savings account\n3: checking and a savings account\n')

# fname = input('please enter usre fist  name: ')
# lname = input('please enter usre last  name: ')
# password = input('please enter usre password: ')
# user = Customer(new_account, fname, lname, password)
# user.add_customer(user.account_type ,user.first_name,user.last_name,user.password)


# user = Customer(1, "noura", "almutairi", "12345")
account = input("do you have account? y/n")

Customer.log_in()
# print(user.logged_in)
Deposit.check_account()





















# if not os.path.exists("./banck.csv"):
#     with open("./banck.csv", 'w', newline='') as csvfile:
#         try:
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#             writer.writeheader()
#             for row in users_accounts:
#                 writer.writerow(row)
#         except csv.Error as e:
#             print(e)

# # 4.0 If Exists - ReadFile / Rows:
# try: 
#     with open("banck.csv", "r") as file:
#         contents = csv.DictReader(file)
#         for row in contents:
#             print(row) #will print: {'Name': 'The First Doctor', 'Actor': 'William Hartnell', 'Number of Episodes': '134'}
#             for prop in fieldnames:
#                 print(row[prop]) # will print the value of each individual property
# except csv.Error as e:
#     print(e)

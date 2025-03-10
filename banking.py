import csv
import os

customer_accounts = [
    { 'account_id': 10001 ,  'first_name': 'suresh',   'last_name': 'sigera','password': '1234', 'checking' : 20, 'savings': 10000 },
    { 'account_id': 10002 , 'first_name': 'james',  'last_name': 'taylor','password': 'idh', 'checking' : 10000, 'savings': 10000 },
    ]

fieldnames = ["account_id", "first_name", "last_name", "password", "checking", "savings"]

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

class Error(Exception):
    """Base class for other exceptions"""
    pass

class LoggedInError(Error):
    pass

class Customer:

    def __init__(self, first_name, last_name, password):
        self.account_type = None
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.checking = None
        self.savings = None
        self.account_id = 10002 #try use random and check if it exist for the id
        self.is_logged_in = False
        self.current_useer = None
    
    def check_logged_in(self):
        print("checkin logged in")
        return True if not self.is_logged_in else False

    def add_customer(self,obj):
        if check_logged_in():
            raise LoggedInError

        if new_account == 1:
            self.checking = 0
        elif new_account == 2:
            self.savings = 0
        else:
            self.checking = 0
            self.savings = 0
        
        try:
            self.account_id += 1
            new_row = {'account_id': self.account_id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'password': self.password,
                'checking': self.checking,
                'savings': self.savings
                }

            customer_accounts.append(new_row)
            with open("banck.csv", "a+") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(new_row)

        except csv.Error as e:
            print(e)

    def add_money(self):
        Bank.add_money()
    
    def log_out(self):
        pass

    def log_in(self):
        while True:
            user_name = input('enter your usre name: ')
            user_password = input('enter your paswword: ')
            for user in customer_accounts:
                if user['first_name'] == user_name and user['password'] == user_password:
                    self.current_useer = user['account_id']
                    self.is_logged_in = True
                    return
            print("Invalid username or password. Please try again.\n")

# class checking_account(Customer):
# class savings_account(Customer):
# class checking_and_savings_account(Customer):


class Deposit(Customer):
    # def__init__():
    #     self.

    def deposit(self):
        # print(customer.is_logged_in)

        if self.check_logged_in():
            raise LoggedInError

        for user in customer_accounts:
            if user['account_id'] == self.current_useer:
                deposit_types = { "1": "checking", "2": "savings" }
                deposit_to = input(f"Deposit into (1) {deposit_types['1']} or (2) {deposit_types['2']} ? ")
                deposit_amt = float(input("Enter the amount of mony to be deposit: "))
                while True:
                    if deposit_to == '1' or deposit_to == '2':
                        # print('it work')
                        user[deposit_types[deposit_to]] += deposit_amt
                        break
                    else:
                        print("Invalid selection! try again")
                        continue 
                
                print("Deposit successful! Updated balance:", user)
                return
    
class Withdraw(Customer):

    def Withdraw_operation(self):

        if check_logged_in():
            raise LoggedInError
        for user in customer_accounts:
            # print(self.current_useer)
            if user['account_id'] == self.current_useer:
                Withdraw_type = int(input("Withdraw into (1) Checking or (2) Savings? "))
                Withdraw_amount = float(input("Ente the amount of mony to be deposit: "))
                if Withdraw_type == 1:
                    if user['checking'] < 0 and Withdraw_amount >100: 
                        print ("invalid operation! your account balance is negative, you can not draw more than 100$!")
                    
                    elif user['checking'] < Withdraw_amount:
                        user['checking'] -= Withdraw_amount
                        user['checking'] -= 35
                        print("Overdraft! 35 has been charge from your account")  
                    else:
                        user['checking'] -= Withdraw_amount

                    print("Deposit successful! Updated balance:", user)
                    return
                elif Withdraw_type == 2:
                    if self.checking < 0 and Withdraw_amount <= 100: 
                        user['savings'] -= Withdraw_amount
                    else:
                        print ("invalid operation! your account balance is negative, you can not draw more than 100$!")
                else:
                    print("Invalid selection!")
                    return
                
class Transfer(Customer):
    def Transfer_operation(self):
        if check_logged_in():
            raise LoggedInError
        
        for user in customer_accounts:
            if user['account_id'] == self.current_useer:
                acct_types = { "1": "checking", "2": "savings", "3": "Other Account" }

                trans_from = int(input(f"Would you like to transfer from (1) {acct_types["1"]}, (2) {acct_types["2"]}?"))
                trans_to = int(input(f"Would you like to transfer from (1) {acct_types["1"]}, (2) {acct_types["2"]}, or (3) {acct_types["3"]}?"))
                trans_amt = float(input("Ente the amount of mony to be transfer: "))
                # if trans_to == "3":
                #     # check the account number

                if trans_to == "3":
                    # run code for transfer to external account
                    for account in customer_accounts:
                        if account['account_id'] == other_account:
                            user[acct_types[trans_from]]-= trans_amt
                            account["checking"] += trans_amt
                            print("Transfer successful! Updated balance:", account)
                            return
                        else:
                            print("Acconut are not found pleas try again")

                else:
                    user[acct_types[trans_from]] -= trans_amt
                    user[acct_types[trans_to]] += trans_amt
                    print("Transfer successful! Updated balance:", user)
                    return

                

                    
                        

       
                



# new_account = input('what kind of account you want to create? \n1: checking account\n2: savings account\n3: checking and a savings account\n')

# fname = input('please enter usre fist  name: ')
# lname = input('please enter usre last  name: ')
# password = input('please enter usre password: ')
# user = Customer(new_account, fname, lname, password)
# user.add_customer(user.account_type ,user.first_name,user.last_name,user.password)


# user = Customer(1, "noura", "almutairi", "12345")
# account = input("do you have account? y/n")

try:

    d = Deposit('james', 'taylor', 'idh')
    d.log_in()
    # print(d.is_logged_in)
    d.deposit()

except LoggedInError:
    print("you need to log in first!")

# first_name': 'james',  'last_name': 'taylor','password': 'id















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



# if transfer_type == 1:
                #     user['savings'] -= trans_amt
                #     user['checking'] += trans_amt
        
                # if transfer_type == 2:
                #     user['checking'] -= trans_amt
                #     user['savings'] += trans_amt

                # if transfer_type == 3:
                #     other_account = int(input("Enter the account Id of the account to be transf: "))

                    # for account in customer_accounts:

                    #     if account['account_id'] == other_account:
                    #         user['checking'] -= trans_amt

                    #         account['checking'] += trans_amt
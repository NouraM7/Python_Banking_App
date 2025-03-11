import csv
import os
import random

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

class ActivationError(Error):
    pass

class Customer:

    def __init__(self, first_name, last_name, password):
        # self.account_type = None
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        # self.checking = None
        # self.savings = None
        self.account_id = random.randrange(10002, 99999) #try use random and check if it exist for the id
        self.is_logged_in = False
        self.current_useer = None
        self.is_active = False
    
    def check_logged_in(self):
        print("checkin logged in")
        return True if not self.is_logged_in else False

    def check_activation_in(self):
        print("checkin activation ")
        return True if not self.is_active else False

    def add_customer(self,obj):
        # if check_logged_in():
        #     raise LoggedInError

        try:
            new_row = {'account_id': self.account_id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'password': self.password,
                }

            # self.account_id = random.randrange(10002, 99999)# check if the number exist

            new_acc = input("choose your account type (1) checking (2) saving (3) checking and saving : ")

            if new_acc == '1':
                new_row['checking'] = 0
            elif new_acc == '2':
                new_row['savings'] = 0
            else:
                new_row['checking'] = 0
                new_row['savings'] = 0

            customer_accounts.append(new_row)
            self.is_active = True

            with open("banck.csv", "a+") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(new_row)

        except csv.Error as e:
            print(e)

    # def add_money(self):
    #     Bank.add_money()
    
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

        if self.check_logged_in():
            raise LoggedInError
        if self.is_active():
            raise ActivationError
        for user in customer_accounts:
            # print(self.current_useer)
            if user['account_id'] == self.current_useer:

                Withdraw_type = { "1": "checking", "2": "savings" }
                overdraft = 0

                while True:
                    Withdraw_from = input(f"Withdraw from (1) {Withdraw_type["1"]} or (2) {Withdraw_type["2"]}? ")
                    Withdraw_amt = float(input("Ente the amount of mony to be deposit: "))
                    if Withdraw_from == '1' or Withdraw_from == '2':
                        if user[Withdraw_type[Withdraw_from]] > 0 or  Withdraw_amt <=  100: 
                            if Withdraw_amt <= 100:
                                if overdraft < 2:
                                    if user[Withdraw_type[Withdraw_from]] < Withdraw_amt:
                                        user[Withdraw_type[Withdraw_from]] -= (Withdraw_amt + 35)
                                        overdraft += 1
                                        print("Overdraft occurs! 35 has been charge from your account", user, "the overdraft is : ", overdraft) 
                                        # return 
                                        continue
                                    else: 
                                        user[Withdraw_type[Withdraw_from]] -= Withdraw_amt
                                        print("Deposit successful! Updated balance:", user)
                                        #return
                                        continue
                                else:
                                    print("Two overdraft occurs, your account has ben deactivated!")
                                    self.is_active = False
                                    return
                                    # continue
                            else:
                                print("invalid operation! you can not Withdraw more than 100$ in one transaction")
                                continue
                        else:
                            print ("invalid operation! your account balance is negative, you can not draw more than 100$!")
                            return
                    else:
                        print("Invalid selection! try again")
                        continue
                           
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

                

                    
                        

       
                





try:
    # new_acc = input('what kind of account you want to create? \n1: checking account\n2: savings account\n3: checking and a savings account\n')

    # fname = input('please enter usre fist  name: ')
    # lname = input('please enter usre last  name: ')
    # password = input('please enter usre password: ')
    # user = Customer(fname, lname, password)
    # user.add_customer(user)


    # user = Customer(1, "noura", "almutairi", "12345")
    # account = input("do you have account? y/n")


    d = Withdraw('james', 'taylor', 'idh')
    d.log_in()

    while True:
        # print(d.is_logged_in)
        d.Withdraw_operation()

except LoggedInError:
    print("you need to log in first!")

except ActivationError:
    print("you account is deactivate!")

















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
import csv
import os

customer_accounts = [
    { 'account_id': 10001 ,  'frst_name': 'suresh',   'last_name': 'sigera','password': 'juagw362', 'balance_checking' : 1000, 'balance_savings': 10000 },
    { 'account_id': 10002 , 'frst_name': 'james',  'last_name': 'taylor','password': 'idh36%@#FGd', 'balance_checking' : 10000, 'balance_savings': 10000 },
    ]

fieldnames = ["account_id", "frst_name", "last_name", "password", "balance_checking", "balance_savings"]

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
        self.loged_in = False
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
            new_row = {'account_id': self.account_id, 'frst_name': self.first_name, 'last_name': self.last_name, 'password': self.password,  'balance_checking': self.balance_checking, 'balance_savings': self.balance_savings}
            customer_accounts.append(new_row)
            with open("banck.csv", "a+") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(new_row)

        except csv.Error as e:
            print(e)
    
    def log_in(self):
        user_name = input('enter your usre name: ')
        user_password = input('enter your paswword: ')

        for user in customer_accounts:
            print(user['frst_name'], user['password'])
            if user['frst_name'] == user_name and user['password'] == user_password:
                self.current_useer = user['account_id']
                self.loged_in = True

class Withdraw(Customer):

    def check_account(self):

        if self.balance_checking != 0 and self.loged_in:
            Withdraw_amount = input("ente the amount of mony to be draw: ")
            for user in customer_accounts:
                




class Deposit():
    pass

class Transfer():
    pass



# new_account = input('what kind of account you want to create? \n1: checking account\n2: savings account\n3: checking and a savings account\n')

# fname = input('please enter usre fist  name: ')
# lname = input('please enter usre last  name: ')
# password = input('please enter usre password: ')
# user = Customer(new_account, fname, lname, password)
# user.add_customer(user.account_type ,user.first_name,user.last_name,user.password)

user = Customer(1, "noura", "almutairi", "12345")
account = input("do you have account? y/n")
if account == 'y':
    user.log_in()
    print(user.loged_in)





















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

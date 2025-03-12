# from tempfile import NamedTemporaryFile
# import shutil
import pandas as pd
import csv
import os
import random


customer_accounts = [
    { 'account_id': 10001 ,  'first_name': 'suresh',   'last_name': 'sigera','password': '1234', 'checking' : 60.0, 'savings': 10000.0 },
    { 'account_id': 10002 , 'first_name': 'james',  'last_name': 'taylor','password': 'idh', 'checking' : 10000.0, 'savings': 10000.0 },
    { 'account_id': 10003 , 'first_name': 'melvin',  'last_name': 'gordon','password': 'uYWE732g4ga1', 'checking' : 2000.0, 'savings': 20000.0 },
    { 'account_id': 10004 ,  'first_name': 'stacey',   'last_name': 'abrams','password': 'DEU8_qw3y72$', 'checking' : 2000.0, 'savings': 20000.0 },
    { 'account_id': 10005 , 'first_name': 'jake',  'last_name': 'paul','password': 'd^dg23g)@', 'checking' : 100000.0, 'savings': 100000.0 }
]

fieldnames = ["account_id", "first_name", "last_name", "password", "checking", "savings"]



if not os.path.exists("./banck.csv"):
    with open("./banck.csv", 'w', newline='') as csvfile:
        try:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        except csv.Error as e:
            print(e)
# else:
#     #change customer data to the values in the csv
    #You can turn the CSV into a dictionary, and then assign that dictionary to data

df = pd.read_csv("banck.csv")
print(df,  "32")
# 4.0 If Exists - ReadFile / Rows:
try: 
    with open("banck.csv", "r") as file:
        contents = csv.DictReader(file)
        data = [row for row in contents]

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

    def __init__(self):
        self.account_id = random.randrange(10002, 99999) #try use random and check if it exist for the id
        self.is_logged_in = False
        self.current_useer = None
        self.is_active = True
    
    def check_logged_in(self):
        print("checkin logged in")
        return True if not self.is_logged_in else False

    def check_activation_in(self):
        print("checkin activation ")
        return True if not self.is_active else False

    def add_customer(self):
        # if check_logged_in():
        #     raise LoggedInError

        try:

            # self.account_id = random.randrange(10002, 99999)# check if the number exist
            print("plear enter your:")
            fname = input('fist  name: ')
            lname = input('last  name: ')
            password = input('usre password: ')

            new_row = {'account_id': self.account_id,
                'first_name': fname,
                'last_name': lname,
                'password': password,
                }

            new_acc = input("choose your account type (1) checking (2) saving (3) checking and saving : ")

            if new_acc == '1':
                new_row['checking'] = 0
            elif new_acc == '2':
                new_row['savings'] = 0
            else:
                new_row['checking'] = 0
                new_row['savings'] = 0

            data.append(new_row)
            self.is_active = True
            

            with open("banck.csv", "a+") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(new_row)

        except csv.Error as e:
            print(e)

    # def add_money(self):
    #     Bank.add_money()
    
    def log_out(self):
        user = input("do you want to log out? yes / no")
        if user == 'yes':
            print('have a good day')
            self.is_logged_in = False
            return

    def log_in(self):
        while True:
            user_name = input('enter your usre name: ')
            user_password = input('enter your paswword: ')
            for user in data:
                if user['first_name'] == user_name and user['password'] == user_password:
                    self.current_useer = user['account_id']
                    self.is_logged_in = True
                    return
            print("Invalid username or password. Please try again.\n")

    def write_csv(self):
        print(data)
        # print(data)

        try: 
            with open("banck.csv", "r") as file:
                contents = csv.DictReader(file)

            with open("./banck.csv", 'w', newline='') as csvfile:
                print("we are changing the csv 140")
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
        except csv.Error as e:
            print(e)


class Bank(Customer):


    def Transfer_operation(self):
        if self.check_logged_in():
            raise LoggedInError
        
        for user in data:
            if user['account_id'] == self.current_useer:
                acct_types = { "1": "checking", "2": "savings", "3": "Other Account" }

                trans_from = input(f"Would you like to transfer from (1) {acct_types["1"]}, (2) {acct_types["2"]}?")
                trans_to = input(f"Would you like to transfer from (1) {acct_types["1"]}, (2) {acct_types["2"]}, or (3) {acct_types["3"]}?")
                trans_amt = float(input("Ente the amount of mony to be transfer: "))
                # if trans_to == "3":
                #     # check the account number

                if trans_to == "3":
                    other_account = int(input("Ente the id of the account: "))
                    # run code for transfer to external account
                    for account in data:
                        if account['account_id'] == other_account:
                            user[acct_types[trans_from]]-= trans_amt
                            account["checking"] += trans_amt

                            new_tras = user[acct_types[trans_from]]
                            new_trans2 = account["checking"]


                            # for row in data.index:
                            #     if data.loc[row, "account_id"] == self.current_useer:
                            #         data.loc[row, acct_types[trans_from]] = new_tras #update

                            #     if data.loc[row, "account_id"] == other_account:
                            #         data.loc[row, "checking"] = new_trans2 #update
                            
                            self.write_csv()
                            print("Transfer successful! Updated balance:", account)
                            return
                        else:
                            print("Acconut are not found pleas try again")

                else:
                    user[acct_types[trans_from]] -= trans_amt
                    user[acct_types[trans_to]] += trans_amt
                    print("Transfer successful! Updated balance:", user)
                    return    
    def deposit(self):
        # print(customer.is_logged_in)

        if self.check_logged_in():
            raise LoggedInError

        # if self.check_activation_in():
        #     raise ActivationError

        def is_float(val): 
            try:
                float(val)
                return True
            except ValueError:
                return False

        for user in data:
            if user['account_id'] == self.current_useer:
                deposit_types = { "1": "checking", "2": "savings" }
                deposit_to = None
                while deposit_to != '1' and deposit_to != '2':
                    deposit_to = input(f"Deposit into (1) {deposit_types['1']} or (2) {deposit_types['2']} ? ")
                    if deposit_to != '1'and deposit_to != '2':
                        print("Invalid selection! try again")
                        print (type(deposit_to))

                deposit_amt = None
                while type(deposit_amt): 
                    deposit_amt = float(input("Enter the amount of mony to be deposit: "))
                    # if is_float(deposit_amt):
                        # curr_balece = user[deposit_types[deposit_to]]
                    user[deposit_types[deposit_to]] =  str(float(user[deposit_types[deposit_to]]) + deposit_amt)
                        # data.loc[row, deposit_types[deposit_to]] = new_data #update
                        # data_top = data.head()

                        # for row in data.index:
                        #     if data.loc[row, "account_id"] == self.current_useer:
                        #         # print(row,data.loc[row, "account_id"])
                        #         data.loc[row, deposit_types[deposit_to]] += deposit_amt #update
                        #         # print(data)

                    self.write_csv()
                        
                    print("Deposit successful! Updated balance:", user)
                    return

try:

    d = Bank()

    d.log_in()
    d.deposit()
    # print("welcome to the bank system!")
    # choise = input("(1) Log in\n(2) creat account")

    # if choise == '1':
    #     d.log_in()
    #     if d.check_logged_in():
    #         raise LoggedInError
    #     print("choos operation:\n")
    #     user_input = input("(1) deposit\n(2)transfar\n(3)log out")
    #     if user_input == '1':
    #         d.deposit()
    #     elif user_input == '2':
    #         d.Transfer_operation()
    #     elif user_input == '3':
    #         d.log_out()
    # else:
    #     d.add_customer()

except LoggedInError:
    print("you need to log in first!")

except ActivationError:
    print("you account is deactivate!")


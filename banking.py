# from tempfile import NamedTemporaryFile
# import shutil
import pandas as pd
import csv
import os
import random
import datetime

from errors import LoggedInError, ActivationError


customer_accounts = [
    { 'account_id': 10001 , 'active' : True,   'first_name': 'suresh', 'last_name': 'sigera',  'password': '1234',         'checking' : 60.0,      'savings': 10000.0,     'overdraft': 0 },
    { 'account_id': 10002 , 'active' : True,   'first_name': 'james',  'last_name': 'taylor',  'password': 'idh',          'checking' : 10000.0,   'savings': 10000.0,     'overdraft': 0 },
    { 'account_id': 10003 , 'active' : True,   'first_name': 'melvin', 'last_name': 'gordon',  'password': 'uYWE732g4ga1', 'checking' : 2000.0,    'savings': 20000.0,     'overdraft': 0 },
    { 'account_id': 10004 , 'active' : True,   'first_name': 'stacey', 'last_name': 'abrams',  'password': 'DEU8_qw3y72$', 'checking' : 2000.0,    'savings': 20000.0,     'overdraft': 0 },
    { 'account_id': 10005 , 'active' : True,   'first_name': 'jake',   'last_name': 'paul',    'password': 'd^dg23g)@',    'checking' : 100000.0,  'savings': 100000.0,    'overdraft': 0 }
]

fieldnames = ["account_id", "active", "first_name", "last_name", "password", "checking", "savings", "overdraft"]

fieldnames_trans = ["transaction_id", "transaction_type", "amount", "date", "balance"]




if not os.path.exists("./banck.csv"):
    with open("./banck.csv", 'w', newline='') as csvfile:
        try:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in customer_accounts:
                writer.writerow(row)
        except csv.Error as e:
            print(e)

# 4.0 If Exists - ReadFile Banck / Rows:
try: 
    with open("banck.csv", "r") as file:
        contents = csv.DictReader(file)
        data = [row for row in contents]

except csv.Error as e:
        print(e)

if not os.path.exists("./transaction_history.csv"):
    with open("./transaction_history.csv", 'w', newline='') as csvfile:
        try:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames_trans)
            writer.writeheader()
                # writer.writerow(row)
        except csv.Error as e:
            print(e)
try: 
    with open("transaction_history.csv", "r") as file:
        contents = csv.DictReader(file)
        trans_data = [row for row in contents]

except csv.Error as e:
    print(e)

class Customer:

    def __init__(self):
        self.account_id = int(data[len(data)-1]['account_id'] )+1 #try use random and check if it exist for the id
        self.is_logged_in = False
        self.current_useer = None
        # self.is_active = True
    
    def check_logged_in(self):
        # print("checkin logged in")
        return True if not self.is_logged_in else False

    def check_activation(self, val):
        if val == "False":
            print("checkin activation ", (val))
            return True
        else:
            print("checkin activation ", (val))
            return False
        # return True if not val else False

    def is_float(self,  val): 
            try:
                float(val)
                return True
            except ValueError:
                return False

    def add_customer(self):

        print("plear enter your:")
        fname = input('fist  name: ')
        lname = input('last  name: ')
        password = input('usre password: ')
        new_row = {'account_id': str (self.account_id),
            'active' : True,
            'first_name': fname,
            'last_name': lname,
            'password': password,
            }
        new_acc = input("choose your account type (1) checking (2) saving (3) checking and saving : ")
        if new_acc == '1':
            new_row['checking'] = 0
            new_row['savings'] = ""
            new_row['overdraft'] = 0
        elif new_acc == '2':
            new_row['checking'] = ""
            new_row['savings'] = 0
            new_row['overdraft'] = 0
        else:
            new_row['checking'] = 0
            new_row['savings'] = 0
            new_row['overdraft'] = 0
        data.append(new_row)
        self.update_csv()
        return print("Your account has been created successfully.")
    
    def log_out(self):
        user = input("do you want to log out? yes / no : ")
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
   
    def update_csv(self):

        try: 
            with open("./banck.csv", 'w', newline='') as csvfile:
                # print("we are changing the csv 140")
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
        except csv.Error as e:
            print(e)


class Bank(Customer):

    def transfer(self):

        #chechk log in
        if self.check_logged_in():
            raise LoggedInError
        
        for user in data:
            if user['account_id'] == self.current_useer:
                acct_types = { "1": "checking", "2": "savings", "3": "Other Account" }

                try: 
                    #check account activation
                    if user['active'] == 'False':
                        raise ActivationError
                except ActivationError:
                    print("You account is deactivate!")
                    return

                while True:
                    trans_from = input(f"Would you like to transfer from (1) {acct_types["1"]}, (2) {acct_types["2"]}?")
                    if trans_from not in ["1","2"]:
                        print("Invalid selection! try again")
                        continue

                    #check if the user have the account
                    if user.get(acct_types[trans_from]) == '':
                        print ("There is no account, try again")
                        continue
                    break

                while True:
                    trans_to = input(f"Would you like to transfer to (1) {acct_types["1"]}, (2) {acct_types["2"]}, or (3) {acct_types["3"]}?")
                    if trans_to not in ["1","2","3"]:
                        print("Invalid selection! try again")
                        continue

                    #check if the user have the account
                    if user.get(acct_types[trans_to]) == '':
                        print ("There is no account, try again")
                        continue 
                    break

                trans_amt = None
                while type(trans_amt): 
                    trans_amt = float(input("Enter the amount of mony to be deposit: "))
                    if not self.is_float(trans_amt):
                        print("Please enter an actual number.")
                        continue
                    break

                # check if external account exist
                not_found = True
                if trans_to == "3":
                    while True:
                        other_account = input("Ente the id of the account: ")
                        for account in data:
                            if account['account_id'] == other_account:
                                not_found = False
                                break
                        if not_found:
                            print("there is no account with this id, please try again")
                            continue
                        break


                # transfer to external account
                if trans_to == "3":
                    for account in data:
                        if account['account_id'] == other_account:
                            user[acct_types[trans_from]] = str(float(user[acct_types[trans_from]]) - trans_amt) 
                            account["checking"] = str(float(account["checking"]) + trans_amt)
                            self.update_csv()
                            print("Transfer successful! Updated balance:", account)
                            return
                
                # transfer to checking or savings account
                else:
                    user[acct_types[trans_from]] = str(float(user[acct_types[trans_from]]) - trans_amt) 
                    user[acct_types[trans_to]] = str(float(user[acct_types[trans_to]]) + trans_amt) 
                    self.update_csv()
                    print("Transfer successful! Updated balance:", user)
                    return 

    def deposit(self):

        #chechk log in
        if self.check_logged_in():
            raise LoggedInError

        for user in data:
            if user['account_id'] == self.current_useer:
                
                deposit_types = { "1": "checking", "2": "savings" }

                while True:
                    deposit_to = input(f"Deposit into (1) {deposit_types['1']} or (2) {deposit_types['2']} ? ")
                    if deposit_to not in ['1','2']: #check user selection
                        print("Invalid selection! try again")
                        continue
                    if user.get(deposit_types[deposit_to]) == '':#check if the user have the account
                        print ("There is no account, try again")
                        continue
                    break
                
                deposit_amt = None
                while type(deposit_amt): 
                    deposit_amt = float(input("Enter the amount of mony to be deposit: "))
                    if self.is_float(deposit_amt):
                        curr_amt = float(user[deposit_types[deposit_to]]) + deposit_amt
                        user[deposit_types[deposit_to]] =  str(float(user[deposit_types[deposit_to]]) + deposit_amt)
                        print(curr_amt, type(curr_amt), type(0), "line 254")
                        if curr_amt >= 0:
                            print('line 256')
                            user['active'] = 'True'
                            user['overdraft'] = '0'
                        self.update_csv() 
                        print("Deposit successful!")
                        return
                    else:
                        print("Please enter an actual number.")

    def withdraw(self):

        #chechk log in
        if self.check_logged_in():
            raise LoggedInError
        
        for user in data:
            if user['account_id'] == self.current_useer:

                try: #check account activation
                    if user['active'] == 'False':
                        raise ActivationError
                except ActivationError:
                    print("you account is deactivate!")
                    return

                withdraw_type = { "1": "checking", "2": "savings" }

                # withdraw from functionality
                withdraw_from = None
                while True:
                    withdraw_from = input(f"Withdraw from (1) {withdraw_type["1"]} or (2) {withdraw_type["2"]}? ")
                    if withdraw_from != "1" and withdraw_from != "2":
                        print("Please choose '1' or '2'")
                        continue
                        #check if the user have the account
                    if user.get(withdraw_type[withdraw_from]) == '':
                        print ("There is no account, try again")
                        continue
                    break

                # withdraw amt functionality
                withdraw_amt = None
                while withdraw_amt is None :
                    withdraw_amt = float(input("Enter the amount of money to be deposited: "))
                    #check if the value is float
                    if not self.is_float(withdraw_amt): 
                        print("Please enter an actual number.")
                    
                    #prevint withdraw more than 100$ in one transaction
                    if withdraw_amt > 100:
                        print('you can not transfare more than 100$ in one transaction')
                        withdraw_amt = None
                        continue
                
                can_withdraw = True
                # can_overdraft = True
                # overdraft_countir = user['overdraft']
                # # max_withdraw_amt = 100
                curr_balance = user[withdraw_type[withdraw_from]]
                print("balance", curr_balance)
                curr_balance_float = float(curr_balance)
                
                # balance cannot be less than 100 -> (-65 -35 = -100)
                # if curr_balance <= -65:
                #     can_withdraw = False
                
                # if (curr_balance - withdraw_amt) < -65:
                #     can_withdraw = False
                if float(user[withdraw_type[withdraw_from]]) < 0:
                    if (float(user[withdraw_type[withdraw_from]]) - withdraw_amt) < -100:
                        can_withdraw = False
                        print('you can not withdraw! you account reach the limit')

                if can_withdraw:
                    if float(user[withdraw_type[withdraw_from]]) < withdraw_amt:
                        if user['overdraft'] >= "2":
                            user['active'] = False
                            print("your account hase be deactivate if you want to active the account pleas deposit")
                            return
                            
                        user[withdraw_type[withdraw_from]] = str(float(user[withdraw_type[withdraw_from]]) - (withdraw_amt + 35))
                        # curr_balance = str(curr_balance_float - (withdraw_amt + 35))
                        user['overdraft'] = str( int(user['overdraft']) + 1)
                        print("Overdraft occurs! 35 has been charge from your account", user) 
                        self.update_csv()
                        return 
                    else:
                        # user[acct_types[trans_from]] = str(float(user[acct_types[trans_from]]) - trans_amt) 
                        user[withdraw_type[withdraw_from]] = str(float(user[withdraw_type[withdraw_from]]) - withdraw_amt)
                        self.update_csv()
                        print("Deposit successful! Updated balance:", user)
                        return

    def display_transaction_data(self):
        # chechk log in
        if self.check_logged_in():
            raise LoggedInError
        
        for user in data:
            if user['account_id'] == self.current_useer:
                date = datetime.datetime.now()

                new_row = {'transaction_id': random.randint(1000, 9999),
                    'transaction_type' : "dd",
                    'amount': 'fname',
                    'date': date,
                    'balance': user['account_id'],
                }
                trans_data.append(new_row)

try:


    d = Bank()
    while True:
        print("Welcome to the Saudi Bank!")
        choise = input("(1) Log in\n(2) Creat account\n(3) Quit your\nYour chooise is: ")

        if choise == '1':
            d.log_in()
            while True:
                print("\nchoos operation:\n")
                user_input = input("(1) Deposit\n(2) Withdraw\n(3) Transfer\n(4) Log out\n Your chooise is: ")
                if user_input == '1':
                    d.deposit()
                    continue
                elif  user_input == '2':
                    d.withdraw()
                    continue
                elif user_input == '3':
                    d.transfer()
                    continue
                elif user_input == '4':
                    d.log_out()
                    break
        elif choise == '2':
            d.add_customer()
            continue
        elif choise == '3':
            print("Have a good day")
            break
        else:
            print("Invaled secection try again!")
            continue

except LoggedInError:
    print("you need to log in first!")

except ActivationError:
    print("you account is deactivate!")


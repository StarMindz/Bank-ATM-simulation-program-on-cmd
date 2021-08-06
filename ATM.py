# THIS IS AN ATM MACHINE. YOU CAN WITHDRAW, DEPOSIT, CHANGE PIN, CHECK ACCOUNT DETAILS,CREATE A NEW ACCOUNT, CAN TRANSFER FROM
# ONE ACCOUNT TO ANOTHER, YOU CAN ALSO CHANGE PHONE NUMBER,

#CLASS
class Account:
    pin = ""
    balance = 0
    phone_number = ""
    account_name = ""
    account_number = ""
    account_type=""

    def __init__(self, name, phone, pin, no, balance):
        self.account_name = name
        self.phone_number = phone
        self.pin = pin
        self.balance = balance
        self.account_number = no

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


#GLOBAL VARIABLES
accountno_list = []
global account
global data

#SUB FUNCTIONS
def cls():
    print(100*"\n")

def strings():
    return str(account.account_name) + str(account.phone_number) +'\n' + str(account.pin) + "\n" + str(account.balance) + "\n" + str(account.account_number) + str(account.account_type)

def Account_list():  # opens list of all the account numbers in the database
    global accountno_list
    with open("ATM DATABASE\\ACCOUNT NO'S.txt", 'a+') as accountno:
        accountno.seek(0)
        accountno_list = [string for string in accountno]

def authenticate(pin):
    while True:
        try:
            pin2 = input("\nInput your ATM pin")
            if int(pin2) == pin:
                break
            else:
                print("\nWrong pin. Try again")
        except:
            print("\nWrong input.")



#MAJOR FUNCTIONS
def Create_Account():
    from random import randint
    typo = ""
    while True:
        typo = str(input("What type of account do you want to create?\
         \na, Savings \nb, Current"))
        if typo.lower() == "a" or typo.lower() == "b":
            break
        else:
            print("\nYour input should be either 'a' or 'b'")
    name = input("\n\nWrite in your complete name in this format *first name  *surname")
    phone = input("\nType in your phone number")
    while True:
        pin = str(input("\nType in a four digit ATM pin"))
        if str(pin).isdigit() and len(pin) == 4:
            break
        else:
            print("Wrong input. it should be a four digit number")
    print("\n\nCreating Account............")

    while True:
        account_number = randint(1000000000, 9999999999)
        if account_number not in accountno_list:
            break
    balances = 0
    if typo.lower() == "a":
        account_type = "Savings"
        account = Account(name, phone, pin, account_number, balances)
        print("\n\nCONGRATULATIONS\nYou successfully created a Saving account \nYour new account number is   \
        {}".format(account_number))
        with open("ATM DATABASE\\" + str(account_number) + ".txt",
                  'a+') as data:
            g = str(account.account_name) + "\n" + str(account.phone_number) + "\n" + str(account.pin) + "\n" + str(account.balance) + "\n" + str(account.account_number) + '\n' + str(account_type)
            data.write(g)

        with open("ATM DATABASE\\ACCOUNT NO'S.txt", 'a+') as data2:
            data2.write("\n" + str(account_number))
    else:
        account_type = "Current"
        account = Account(name, phone, pin, account_number, balances)
        print("\n\nCONGRATULATIONS\nYou successfully created a Current account \nYour new account number is   \
        {}".format(account_number))
        with open("ATM DATABASE\\" + str(account_number) + ".txt",
                  'a+') as data:
            g = str(account.account_name) + "\n" + str(account.phone_number) + "\n" + str(account.pin) + "\n" + str(account.balance) + "\n" + str(account.account_number) + '\n' + str(account_type)
            data.write(g)

        with open("ATM DATABASE\\ACCOUNT NO'S.txt", 'a+') as data2:
            data2.write("\n" + str(account_number))


def Open_Account():
    global accountno_list
    global account
    global data
    accountno = str(input("\nGoodday, please slot in your ATM card and type in your account number"))
    while True:
        if '\n' + accountno in accountno_list or accountno in accountno_list or accountno + '\n' in accountno_list:
            break
        else:
            accountno = input("\nThis account does not exist!!!\nInvalid account number. Please try again")
    account_number = accountno
    data = open("ATM DATABASE\\" + str(account_number) + ".txt", 'r+')
    account_name = data.readline()
    phone_number = data.readline()
    pin = int(data.readline())
    balance = int(data.readline())
    account_number = data.readline()
    account_type = data.readline()
    data.seek(0)
    authenticate(pin)
    account = Account(account_name, phone_number, pin, account_number, balance)
    account.account_type=account_type
    Loggedin = True
    while Loggedin:
        while True:
            command = input("\n\n\nWhat would you like to do:\
            \n1.Make a withdrawal\
            \n2.Make a deposit\
            \n3.Change your phone number\
            \n4.Change your ATM pin\
            \n5.Make a transfer to another account")
            if command == '1' or command == '2' or command == '3' or command == '4' or command == '5':
                break
            else:
                print("\nWrong input,please try again")
        if command == '1':
            withdraw()
        elif command == '2':
            deposit()
        elif command == '3':
            change_phone(pin)
        elif command == '4':
            change_pin(pin)
        elif command == '5':
            transfer(pin)
        while True:
            cls()
            log = input("\nDo you want to carry out another transaction?\n1.Yes\n2.No")
            if log == '1' or log == '2':
                break
            else:
                print("\nWrong input. type in either 1 or 2")
        if log == '1':
            Loggedin = True
        else:
            data.close()
            Loggedin = False


def withdraw():
    global data
    while True:
        try:
            amount = int(input("\nHello!!! \nHow much do you want to withdraw..."))
            while True:
                if amount <= int(account.balance):
                    account.withdraw(amount)
                    break
                else:
                    amount =int(input("\nYou do not have sufficient fund to make this withdrawal\nRequest for a lesser amount"))
            break
        except:
            print("\nType in only numbers")
    print("\nYou have sucessfully withdrawn {} from your account\nPrevious balance: {} \nNew balance: {}".format(amount, amount + account.balance , account.balance))
    print("\nTake your cash")
    g = strings()
    data.write(g)
    data.seek(0)


def deposit():
    global data
    amount = int(input("Good day sir,\n\nHow much do you want to deposit..."))
    account.deposit(amount)
    print(
        "\nYou have successfully deposited {} to your account.\nPrevious balance: {} \nNew balance: {} ".format(amount,
                                                                                                                account.balance - amount,
                                                                                                                account.balance))
    g = strings()
    data.write(g)
    data.seek(0)


def change_phone(pin):
    global data
    authenticate(pin)
    phone = input("\nType in your new phone number")
    account.phone_number = phone
    g = strings()
    data.write(g)
    data.seek(0)


def change_pin(pin):
    global data
    authenticate(pin)
    while True:
        pin2 = str(input("\nType in a four digit ATM pin"))
        if pin2.isdigit() and len(pin2)==4:
            break
        else:
            print("Wrong input. it should be a four digit number")

    account.pin = pin2
    g = strings()
    data.write(g)
    data.seek(0)


def transfer(pin):
    amount = input("Type in amount to be transfered")
    while True:
        if amount <= account.balance:
            break
        else:
            amount = input("\nYou do not have sufficient fund to make this transfer. \nType in a lesser amount")
    account_number = input("\nType in the account number to transfer amount to")
    while True:
        if account_number not in accountno_list:
            account_number = ("\nThis account does not exist.\nType in a valid account number")
        else:
            break
    authenticate(pin)
    account.withdraw(amount)


def ATM():
    global accountno_list
    Account_list()
    print(
        "\n\n" + "*" * 125 + "\n" + "-" * 125 + "\n" + "      WELCOME TO THE STAR MINDS ATM" + "\n" + "-" * 125 + "\n" + "*" * 125)
    typo = ""
    while typo.lower() != 'a' and typo.lower() != 'b' and typo.lower() != 'c':
        typo = input(
            "\n\n\nWhat would you love to do: \na, Open a new Account \nb, Open an existing Account\nc,Exit ATM")
        if typo.lower() != 'a' and typo.lower() != 'b' and typo.lower() != 'c':
            print("\nWrong input. Your input should be either 'a' or 'b'")
    if typo.lower() == 'a':
        Create_Account()
    elif typo.lower() == 'b':
        Open_Account()
    else:
        return 0


ATM()















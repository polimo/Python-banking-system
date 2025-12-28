import string
import random
Account = {}
is_account = False
list_Accounts = []
def add_account():
    print("--------------------")
    account_name = input("Enter a name for your account: ").title().strip()
    Account["Account Name"] = account_name
    choices = ["yes", "no"]
    choice = input("Want us to create a Powerful password?[Yes/No]: ").lower().strip()
    while choice not in choices:
        choice = input("Want us to create a Powerful password?[Yes/No]: ").lower().strip()
    if choice == "yes":
        characters = "".join(random.choice(string.ascii_letters + string.digits) for i in range(11))
        account_pwd = characters
        Account["Account Password"] = account_pwd
    else:
        account_pwd = input("Enter your account password: ").strip()
        Account["Account Password"] = account_pwd
    account_id = "".join(random.choice(string.digits) for i in range(6))
    Account["Account ID"] = account_id
    account_Balance = 0
    Account["Account Balance"] = account_Balance
    return Account

def show_accounts():
    counts = 0
    for accounts in list_Accounts:
        print(f"----------------Index({counts})-------------------")
        print(f"Account Name: {accounts['Account Name']} || Account ID: {accounts['Account ID']} || Account Balance: {accounts['Account Balance']}")
        counts += 1
while True:
    print("""
        1. Add account
        2. Remove account
        3. Show account
        4. Withdraw from chosen account
        5. Deposit from chosen account
        6. Exit
    """)
    try:
        choice = int(input("Enter a valid choice: "))
        if choice == 1:
            is_account = True
            returned_pack = add_account()
            list_Accounts.append(returned_pack.copy())
            print("Account added!")
        elif choice == 2:
            if not is_account:
                print("There are no accounts to remove!")
            else:
                show_accounts()
                try:
                    index_choice = int(input("Please enter the index of the account you would like to remove: "))
                    if index_choice > len(list_Accounts):
                        print("The account doesnt exist!")
                    else:
                        del list_Accounts[index_choice]
                        print("Account removed!")
                        if len(list_Accounts) > 0:
                            is_account = True
                        else:
                            is_account = False
                except ValueError:
                    print("Please enter a valid choice.")
        elif choice == 3:
            if is_account:
                show_accounts()
            else:
                print("There are no accounts to show")
        elif choice == 4:
            if not is_account:
                print("There are no accounts")
            else:
                show_accounts()
                print("-------------------------------")
                try:
                    index_choice = int(input("Please enter the index of the account you would like to withdraw from: "))
                    if index_choice > len(list_Accounts):
                        print("The account doesnt exist!")
                    else:
                        with_draw = int(input(f"How much you'd like to withdraw from {list_Accounts[index_choice]["Account Name"]}'s account?: "))
                        if with_draw <= 0:
                            print("You cant withdraw 0 or less")
                        else:
                            if with_draw > list_Accounts[index_choice]["Account Balance"]:
                                print("You dont have this much money!")
                            else:
                                list_Accounts[index_choice]["Account Balance"] -= with_draw
                except ValueError:
                    print("Please enter a valid Number. ")
        elif choice == 5:
            if is_account:
                show_accounts()
                print("-------------------------")
                index_choice = int(input("Enter the index of the account you would like to deposit money to: "))
                if index_choice > len(list_Accounts):
                    print("There is no such account!")
                else:
                    try:
                        deposit_money = int(input(f"How much you would like to deposit money from {list_Accounts[index_choice]['Account Name']}'s account?:"))
                        if deposit_money <= 0:
                            print("You cant deposit 0 or less")
                        else:
                            list_Accounts[index_choice]["Account Balance"] += deposit_money
                    except ValueError:
                        print("Please enter a valid Amount. ")
            else:
                print("There are no accounts!")
        elif choice == 6:
            print("GoodBye!!")
            break
    except ValueError:
        print("Please enter a valid choice. ")
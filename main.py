import hashlib
import os
from time import sleep
from os.path import exists
from bullet import Password


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def create_account():
    passwords_not_same = True
    login = input("Login: ")
    while passwords_not_same:
        cli = Password(prompt='Password: ', hidden="*")
        password = cli.launch()
        cli = Password(prompt="Repeat password: ", hidden="*")
        repeat_password = cli.launch()
        if password == repeat_password:
            print(f"Account {login} created!")
            encrypt = hashlib.md5(password.encode())
            add_account_to_txt(login, encrypt.hexdigest())
            break
        print("The passwords do not match. Try again.")


def add_account_to_txt(login, password):
    with open("accounts.txt", "a", encoding="UTF-8") as f:
        f.write(f"{login}: {password}\n")


def sign_in():
    login = input("Login: ")
    cli = Password(prompt="Password: ", hidden="*")
    password = cli.launch()
    encrypt = hashlib.md5(password.encode())
    logged_in = check_if_account_exist(login, encrypt.hexdigest())
    if logged_in:
        print("You are logged.")
        return login
    print("You have entered the wrong username or password.")
    sleep(2)


def check_if_account_exist(login, password):
    with open("accounts.txt", encoding="utf-8") as f:
        for line in f.readlines():
            if login == line[:line.index(":")].strip() and password == line[line.index(":") + 1:].strip():
                return True
    return False


def application_driver_license(login):
    with open(f"application_{login}.txt", "w", encoding="UTF-8") as f:
        f.write("\t\t\t\t\tAPPLICATION DRIVER LICENSE\n")
        print("First name: ", end="")
        f.write(f"First name: {input()}\n")
        print("Last name: ", end="")
        f.write(f"Last name: {input()}\n")
        print("Candidate number on the driver: ", end="")
        f.write(f"Candidate number on the driver: {input()}\n")
        print("Signature: ")
        f.write(f"Signature: {input()}")
    print("Please wait to be contacted regarding the exam.\nThank you.")


running_system_driver = True
while running_system_driver:
    if not exists("accounts.txt"):
        f = open("accounts.txt", "x")
        f.close()
        print("Stworzono plik")
    while True:
        clear()
        print("Hello what do you want to do (Enter number)?")
        print("1. Create account\n2. Sign in\n9. Close program")
        try:
            system_choice = int(input("Option: "))
            break
        except:
            print("Please enter a number")
            sleep(1)
            clear()

    sleep(0.5)
    clear()
    if system_choice == 1:
        create_account()
        sleep(2)
    elif system_choice == 2:
        login = sign_in()
        if login:
            while True:
                sleep(1)
                clear()
                print("Do you want to apply for a driving license(yes/no): ", end="")
                want_apply_license = input()
                if want_apply_license.lower() == "yes" or want_apply_license.lower() == "no":
                    break
                print("Please choose between yes or no.")
                clear()
            sleep(2)
            clear()
            if want_apply_license == "yes":
                application_driver_license(login)
    elif system_choice == 9:
        print("Thank you for using our system.")
        running_system_driver = False
    else:
        clear()

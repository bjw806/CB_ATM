import sqlite3
import datetime
import time as TIME


def database():
    conn = sqlite3.connect("bankdata.db", isolation_level=None)
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS bankdata \
            (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATETIME DEFAULT (DATETIME('now', 'localtime')), card number, account name, pin number, balance real)")


def search_account(card, account):
    conn = sqlite3.connect("bankdata.db", isolation_level=None)
    c = conn.cursor()

    if (account == None):
        c.execute("SELECT * FROM 'bankdata' WHERE card=:idn1", {"idn1": card})
    else:
        c.execute("SELECT * FROM 'bankdata' WHERE card=:idn1 AND account=:idn2", {"idn1": card, "idn2": account})
    found = c.fetchall()
    conn.close()

    if (found == []):
        print("*not found")
        return -1
    return found


def check_pin(card, pin):
    db = search_account(card, None)[0]
    dbpin = int(db[4])
    if (pin == dbpin):
        return db
    else:
        print("*wrong pin")
        return False


def withdraw_deposit(str1, card, account, pin, amount):
    conn = sqlite3.connect("bankdata.db", isolation_level=None)
    c = conn.cursor()
    c.execute("SELECT * FROM 'bankdata' WHERE card=:idn1 AND account=:idn2 AND pin=:idn3",
              {"idn1": card, "idn2": account, "idn3": pin})
    found = c.fetchone()

    if (str1 == "deposit"):
        balance = found[5] + amount
    elif (str1 == "withdraw"):
        balance = found[5] - amount
        if (balance < 0):
            print("*Not enough balance")
            return
    else:
        return
    c.execute("UPDATE bankdata SET balance = ? WHERE id = ?", (balance, found[0]))
    conn.close()


def account_balance(card, pin):

    conn = sqlite3.connect("bankdata.db", isolation_level=None)
    c = conn.cursor()
    c.execute("SELECT * FROM 'bankdata' WHERE card=:idn1 AND pin=:idn2",
              {"idn1": card, "idn2": pin})
    found = c.fetchall()
    conn.close()
    return found


if __name__ == "__main__":
    database()

    # insert card
    while (1):
        card_num = input("\nInsert Card: ")
        if (card_num == "exit"):
            exit()
        elif (search_account(int(card_num), None) != -1):
            break
        else:
            pass
    # enter pin
    while (1):
        pin_num = input("\nEnter PIN number: ")
        if (pin_num == "exit"):
            exit()
        elif (check_pin(int(card_num), int(pin_num)) != False):
            break
        else:
            pass

    # show accounts and balances
    account = account_balance(card_num, pin_num)
    for i in range(len(account)):
        print("NUM:", i + 1, "Account:", account[i][3], "| Balance:", account[i][5])

    # select action
    select_account = input("\nSelect Account: ")
    if (select_account == "exit"):
        exit()

    while (1):
        print("\n1. Deposit Balance")
        print("2. Withdraw Balance")
        print("3. Exit")
        select_action = input("Select Action: ")
        if (int(select_action) == 3):
            break
        elif (int(select_action) == 1):
            amount = int(input("Amount of deposit balance: "))
            withdraw_deposit("deposit", card_num, account[int(select_account) - 1][3], pin_num, amount)
        elif (int(select_action) == 2):
            amount = int(input("Amount of withdraw balance: "))
            withdraw_deposit("withdraw", card_num, account[int(select_account) - 1][3], pin_num, amount)
        else:
            pass

        account = account_balance(card_num, pin_num)
        print("Account:", account[int(select_account) - 1][3], "| Balance:", account[int(select_account) - 1][5])

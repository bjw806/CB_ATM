# CB_ATM
A simple ATM controller  


# Functions
* database(): If there is no database, create a new database.  

* search_account(card, account): Enter card/account num and search the database. Return result or -1.  

* check_pin(card, pin): Enter card/pin num and verify that it matches the database.  

* withdraw_deposit(str1, card, account, pin, amount): Used for deposit and withdrawal.  
  str1: "deposit" or "withdraw"
  card: card number
  account: account number
  pin: pin number
  amount: deposit/withdraw balance amount  
  
* account_balance(card, pin): Check your multi-account balance in the database with card/pin number.


* if __name__ == "__main__": Function tester. You can test all functions with this.

# Database
* There is "bankdata.db" for test.

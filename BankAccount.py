# -*- coding: utf-8 -*-

from sys import breakpointhook
from typing import Optional
class Account:
  def __init__(self, name, startingBalance):
    self.name = name
    self.balance = startingBalance

  def print_account (self):
    print("%s $%.2f" % (self.name, self.balance))

  def deposit_account (self):
    depositAmount = float(input("Please enter your deposit amount: $"))
    self.balance += depositAmount
    self.print_account()

  def withdraw_account (self):
    withdrawAmount = float(input("Please enter your withdrawal amount: $"))
    while (((self.balance - withdrawAmount) < 0) or (withdrawAmount <= 0)):
      if ((self.balance - withdrawAmount) < 0):
        withdrawAmount = float(input("Please enter a valid amount: $"))
      else:
        withdrawAmount - float(input("Please enter an amount: $"))
    self.balance -= withdrawAmount
    self.print_account()

#...............................................
accountList = []
accountList.append(Account("Fred", 100.0))
accountList.append(Account("Jane", 80.0))

# ...............................................

def searchAccount(name):
  specificAccount = [account for account in accountList if account.name == name];
  return specificAccount;

active = True;

while (active):

  option = 0;

  while ((option < 1) or (option > 4)):
    print("1. Deposit, 2. Withdraw, 3. Print, 4. Quit");
    print("Please select one of the options")
    option = int(input());

    if (option == 1):
      accountName = input ("Please enter account name: ");
      inputAccount = searchAccount(accountName);
      if (len(inputAccount) == 0):
        print("Account does not exist");
      else:
        inputAccount[0].deposit_account();
    elif (option == 2):
      accountName = input("Please enter account name: ");
      inputAccount = searchAccount(accountName);
      if (len(inputAccount) == 0):
        print("Account does not exist");
      else:
        inputAccount[0].withdraw_account();
    elif (option == 3):
      for account in accountList:
        account.print_account()
    else:
      active = False;

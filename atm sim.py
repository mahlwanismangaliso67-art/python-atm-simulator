print('insert card')
input('press Enter')

pin = input('Enter your pin')

correct_pin = "0000"
balance = 700
if pin == correct_pin:
  print('allow access')
  while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    users_choice = input("choose option")
    if users_choice == "1":
      print("Available balance: R",balance)
    elif users_choice == '2':
      print('Place your money in the cash slot')
      deposit_amount = input('How much do you wish to deposit?')
      deposit_amount = int(deposit_amount)
      balance = balance + deposit_amount
      print("New balance: R", balance)
    elif users_choice == '3':
      print("Enter the amount you wish to withdraw")
      withdraw_amount = input('Enter withdraw amount')
      withdraw_amount = int(withdraw_amount)
      if withdraw_amount > balance:
         print('Insufficient funds')
      else:
         withdraw_amount 
         balance = balance - withdraw_amount
         print("New balance: R", balance)
    elif users_choice == '4':
         print("You may take your card")
         break
else:
  print('access denied')

balance = 0.0
transaction_history = []
Pin = 11092007
def Deposit(amt):
    global balance,transaction_history
    balance += amt
    transaction_history.append(f'{amt}')

def Withdraw(amt):
     global balance,transaction_history
     balance -= amt
     transaction_history.append(f'-{amt}')

def Security_check():
            tries = 3
            while True:
                if tries == 0:
                     print("CARD BLOCKED!")
                     exit()
                else: 
                     tries -= 1
                     Security_check_Pin = int(input("Enter your pin: "))
                if Security_check_Pin == Pin:
                     return print("Pin is correct!! you can proccess forward ")
                else:
                     print(f"Pin is wrong !! Try again. (left {tries})")
                     continue

                        

print("=======================")
print(" Welcome to ABC bank!!!")
while True:
    print("=======================")
    print('''
1) Check balance.
2) Change your pin.
3) Deposit an amount.
4) withdraw an amount.
5) Transaction history.
6) Interest calculator.
7) Exit.
          

''')
    choice = input("Enter your choice (1-6): ")
    print("=========================")
    if choice == '1':
        Security_check()
        print(f"Your balance is : ₹ {balance}")
        continue
    elif choice == '2':
       Security_check()
       
       while True:
        New_Pin = int(input("Type your new pin:"))
        Reverify = int(input("Retype your new pin to confirm:"))
        if New_Pin == Reverify:
            print("Pin is changed!")
            break
        else:
             print("Mismatched pin! Try again.")
             continue
       continue   
    elif choice == '3':
        Security_check()
        while True:
            amt = int(input("Enter amount you want to deposit: "))
            if amt <= 0:
                print("Negative or zero amount cannot be deposited!! Try again.")
                continue
            else:
                Deposit(amt)
                print(f"Deposited amount succesfully !! New balance: ₹ {balance} ")
                break
        continue
    elif choice == '4':
         Security_check()
         while True:
            amt = int(input("Enter amount you want to withdraw: "))
            if amt <= 0:
                print("Negative or zero amount cannot be withdrawed!! Try again.")
                continue
            elif amt > balance:
                print("Insufficient funds,Try again.")
                break
            elif (balance - amt) < 500:
                 print("Transacion unsuccessfull,need minimum balance")
                 break
            elif (balance - amt) >= 500:
                 Withdraw(amt)
                 print(f"Withdrawal successfull!! Updated balance: ₹ {balance}")
                 break
            continue
    elif choice == '5':
         Security_check()
         print("transaction history:")
         for i in range(len(transaction_history)):
              if int(transaction_history[i]) < 0:
                   print(f"Withdrawed amount: - ₹ {abs(int(transaction_history[i]))}")
              else:
                   print(f"Deposited amount: + ₹ {transaction_history[i]}")
         continue
    elif choice == '6':
         print("--- 📈 Interest Estimator (At 5% P.A.) ---")
         time = float(input("Enter the time period in years: "))
         si = (balance*5*time)/100
         print(f"At a 5% interest rate, your balance will grow by: ₹ {si}")
         print(f"Total amount after {time} years: ₹ {balance + si}")

         
    elif choice == '7':
         print("Thank you!! for banking with us have a good day.")
         break
    else:
         print("Invalid choice,Try again.")
         continue


                 
                 
         
    





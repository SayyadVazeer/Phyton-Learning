def show_balance(balance):
    print(f" Your Balance is ${balance:.2f}")

def deposit():
    amount = int(input("Enter an amount to be deposited: $"))
    print("*********************")
    if amount < 0:
        print("Thats not a valid amount")
        print("*********************")
        return 0
    else:
        print(f"${amount} is deposited into the account")
        print("*********************")
        return amount
def withdraw(balance):
    amount = int(input("Enter amount to be withdrawn: $"))

    if amount > balance:
        print("Balance insuffent in your account")
        withdraw(balance)
    elif amount < 0:
        print(" Please enter an valid amount")
        print("*********************")
        withdraw(balance)
    else:
        print(f"Please collect ${amount}")
        print("*********************")
        return amount
    
def main():

    balance = 0
    is_running =True

    while is_running:
        print("*********************")
        print("   Banking program   ")
        print("*********************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*********************")
        choice = input("Choose the option (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance+=deposit()
            show_balance(balance)
        elif choice == '3':
            balance-=withdraw(balance)
            show_balance(balance)
        elif choice == '4':
            is_running = False
        else:
            print("That is not a valid choice")
            print("*********************")

    print("Thank you Have a Great day !")
    print("*********************")

if __name__ == '__main__':
    main()
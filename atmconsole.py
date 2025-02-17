
# Global variables
total_dep_amount =0
user_balance = 0
Withdrawal_amount = 0
current_pin = 1234

#User Panel
def user_input():
    print("Insert Your Card...")
    input("And Press Enter >>> ")
    while True:
        try:
            entered_pin = int(input("Enter Your Pin : "))
            if entered_pin == current_pin:
                print("\nPlease select an option below :")
                print("1. Deposit")
                print("2. Fast Cash Withdrawal")
                print("3. Cash Withdrawal")
                print("4. Balance")
                print("5. PIN Change")
                print("6. Main Menu")
                print("7. Quit")
            else:
                print("Wrong PIN! Try again.")
                break
        except ValueError:
            print("Invalid input! Please enter a numeric PIN.")
        
        try:
            choice = int(input("Enter your choice: "))  
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue
        
        if choice == 1:
            deposit()
        elif choice in [2, 3]:  
            Withdrawal()
        elif choice == 4:
            show_balance()
        elif choice == 5:
            pin_change()
        elif choice== 6:
            mainmenu()
        elif choice == 7:
            print("Thank you for using our ATM. Goodbye!")
            break  

def deposit():
    global total_dep_amount, user_balance
    dep_amount = int(input("Enter the Amount: "))
    
    # Taking input for different denominations
    a1 = int(input("Enter no of 2000: ")) * 2000
    a2 = int(input("Enter no of 500: ")) * 500
    a3 = int(input("Enter no of 200: ")) * 200
    a4 = int(input("Enter no of 100: ")) * 100
    a5 = int(input("Enter no of 50: ")) * 50
    a6 = int(input("Enter no of 20: ")) * 20
    a7 = int(input("Enter no of 10: ")) * 10
    a8 = int(input("Enter no of 5: ")) * 5
    a9 = int(input("Enter no of 2: ")) * 2
    a10 = int(input("Enter no of 1: ")) * 1
    
    total_dep = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
    
    if dep_amount == total_dep:
        print("Credited in your Account Successfully...")
        total_dep += user_balance  # Update total deposited amount
        user_balance += total_dep_amount  # Update balance
    else:
        print("Invalid Amount Entered!")
        

def Withdrawal():
    global Withdrawal_amount, user_balance, total_dep_amount
    amount_input = int(input("Enter the Amount to Withdraw: "))

    if amount_input > user_balance:
        print("Insufficient Balance!")
    else:
        user_balance -= amount_input  # Deduct from balance
        Withdrawal_amount += amount_input  # Update withdrawal amount
        print("Amount Withdrawn Successfully!")


def show_balance():
    global user_balance
    print(f"Your current balance is: {user_balance}")

def pin_change():

    global current_pin 

    current_pin = int(input("Enter your current PIN: "))
    
    if current_pin == current_pin:
        new_pin = int(input("Enter your new PIN: "))
        confirm_pin = int(input("Confirm your new PIN: "))
        
        if new_pin == confirm_pin:
            current_pin  = new_pin  # Updating the PIN
            print("Your PIN has been successfully changed!")
        else:
            print("PINs do not match! Try again.")
    else:
        print("Incorrect current PIN! Returning to main menu.")



#Adminstration Panel
def admin_input():
    print("Administration Panel")
    while True:
        current_pin_admin = 1234
        try:
            entered_pin_admin = int(input("Enter Your Admin Pin: "))
            if entered_pin_admin == current_pin_admin:
                print("\nPlease select an option below:")
                print("1. Show Available Money")
                print("2. Open Valet")
                print("3. Main Menu")
                print("4. Exit")
            else:
                print("Wrong PIN! Try again.")
                break
        except ValueError:
            print("Invalid input! Please enter a numeric PIN.")

        try:
            choice = int(input("Enter your choice: "))  
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 3.")
            continue
        if choice == 1:
            print(f"Available Money in ATM: {total_dep_amount}")
        elif choice == 2:
            open_valet()
        elif choice == 3:
            mainmenu()
        elif choice == 4:
            print("Thank you for using our ATM. Goodbye!")
            break  

def open_valet():
    global total_dep_amount
    print("Valet Openned Successfully !!!")
    print("1.Add Cash")
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        dep_amount = int(input("Enter the Amount: "))
        # Taking input for different denominations
        a1 = int(input("Enter no of 2000: ")) * 2000
        a2 = int(input("Enter no of 500: ")) * 500
        a3 = int(input("Enter no of 200: ")) * 200
        a4 = int(input("Enter no of 100: ")) * 100
        a5 = int(input("Enter no of 50: ")) * 50
        a6 = int(input("Enter no of 20: ")) * 20
        a7 = int(input("Enter no of 10: ")) * 10
        a8 = int(input("Enter no of 5: ")) * 5
        a9 = int(input("Enter no of 2: ")) * 2
        a10 = int(input("Enter no of 1: ")) * 1
        
        total_dep = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
    
    if dep_amount == total_dep:
        print("Credited in your Account Successfully...")
        total_dep_amount += total_dep  # Update total deposited amount
    else:
        print("Invalid Amount Entered!")
        
    
    
# Main execution
def mainmenu():
    print("   SBI BANK \nHello...Buddy!!!")
    print("1. Customer")
    print("2. Admin")
    choice = int(input("Enter the login as: "))
    if choice == 1:
        user_input()
    elif choice == 2:
        admin_input()
    else:
        print("Invalid Input")
mainmenu()


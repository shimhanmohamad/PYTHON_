print("Welcome to COM bank ATM")
chances = 3
restart = 'Y'
bal = 1200000

while chances > 0:  # Loop should run until chances are greater than 0
    pin = input("Enter the 4 Digit PIN : ")
    
    if len(pin) != 4:  # Check if PIN is not 4 digits
        print("Invalid PIN")
        chances -= 1  # Decrease chances after an incorrect PIN
    else:
        print("Your pin is correct")
        
        while restart.lower() in ['y', 'yes']:  # Continue if restart is 'y' or 'yes'
            print("\nPlease enter 2 to withdraw")
            print("Please enter 1 to check balance")
            print("Please enter 3 to Pay")
            print("Please enter 4 to exit")
            option = int(input("Enter the option: "))
            
            if option == 1:
                print("Your balance is", bal)
                restart = input("Would you like to continue (Y/N): ")
                if restart.lower() in ['n', 'no']:
                    print("Thank you for banking with us")
                    break  # Exit the loop
            
            elif option == 2:
                amount = int(input("Enter the amount to withdraw: "))
                print("Your balance is", bal)
                if amount >= bal:
                    print("Insufficient balance, please enter less than", bal)
                    while amount < bal:
                        amount = int(input("Enter the amount to withdraw: "))
                        
                else:
                    bal -= amount
                    print("You have withdrawn", amount)
                    print("Your remaining balance is", bal)
                    restart = input("Would you like to continue (Y/N): ")
                    if restart.lower() in ['n', 'no']:
                        print("Thank you for banking with us")
                        break
            
            elif option == 3:
                amount = int(input("Enter the amount to pay: "))
                if amount >= bal:
                    print("Insufficient balance")
                else:
                    bal -= amount
                    print("You have paid", amount, "successfully")
                    print("Your remaining balance is", bal)
                    restart = input("Would you like to continue (Y/N): ")
                    if restart.lower() in ['n', 'no']:
                        print("Thank you for banking with us")
                        break  # Exit the loop
            
            elif option == 4:
                print("Thank you for banking with us")
                break  # Exit the loop
            else:
                print("Invalid option. Please enter a correct option.")
                restart = input("Do you want to continue (Y/N): ")
                if restart.lower() in ['n', 'no']:
                    break  # Exit the loop

    if chances == 0:
        print("You have exceeded the maximum number of chances.")
        break  # Exit if the user runs out of chances
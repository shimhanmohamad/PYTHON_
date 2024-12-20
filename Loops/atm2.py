print("Welcome to COM bank ATM")
bal = 100000
chances = 3
restart = 'Y'

while chances > 0:
    pin = input("Enter the 4 digit number : ")
    if len(pin) != 4:
        print("Invalid Pin, Please Enter the correct PIN number")
        chances = chances - 1
        print(f"You have {chances} left")
        if chances == 0:
            print("your card is edjected..Re-Insert the card and try with correct pin number")
            break
    else:
        print("PIN is accepeted")
        while restart.lower() in ['y','yes']:
            print("\nPlease enter  1 for check balance")
            print("Please enter 2 for withdraw")
            print("Please enter 3 for deposite")
            print("If you want to Eject the card then enter 4")
            
            option = int(input("Enter the option for what you want to do : "))
            if option == 1:
                print(f"Your balance is {bal}")
                another_chance = input("Do you want another services : ")
                if another_chance in ['N','n','NO','no']:
                    print("Thank  you for banking with us")
                
                break
            elif option == 2:
                print(f"Your last balance is {bal}")
                amount = int(input("Enter the amount you want to withdraw : "))
                if amount >= bal : 
                    print(f"Insufficient amount please enter amount less than {bal}")
                else:
                    print("Collect your cash")
                    bal = bal - amount
                    print(f"Your current balance is {bal}")
                    restart = input("If you want to get another service : (Y/N)")
                    if restart.lower() in ['n','no']:
                        print('Thank you for banking with us')
                        break
                break
                    
            elif option == 3 :
                max_chances = 0
                print(f"You current balance is {bal}")
                accnumber = input("Enter the account number you want to deposite : ")
                if len(accnumber) != 8:
                    print("Invalid account number.Enter the correct account number")
                    while len(accnumber) != 8:  
                        accnumber = input("Enter the correct account number you want to deposite : ")
                        max_chances = max_chances + 1
                        if max_chances == 5:
                            print("Thank you for banking with us.Please eject the card and re-insert it")
                            break
                    if len(accnumber) == 8 and max_chances < 5:
                        print("Account number is valid. Proceeding with the transaction.")
                
                phonenumber = input("Enter the phone number of the depositor : ")
                p_chances = 0
                if len(phonenumber) != 10:
                    print("Invalid phone number.Enter the correct phone number")
                    while len(phonenumber) != 10:  
                        phonenumber = input("Enter the correct phone number : ")
                        p_chances = p_chances + 1
                        if p_chances == 5:
                            print("Thank you for banking with us.Please eject the card and re-insert it")
                            break
                    if len(phonenumber) == 8 and NIC_chances < 5:
                        print("Phone number is valid. Proceeding with the transaction.")
                
                
                NICnumber = input("Enter the NIC number of the depositor : ")
                NIC_chances = 0
                if len(NICnumber) != 10:
                    print("Invalid NIC number.Enter the correct phone number")
                    while len(phonenumber) != 10:  
                        NICnumber = input("Enter the correct NIC number : ")
                        NIC_chances = NIC_chances + 1
                        if NIC_chances == 5:
                            print("Thank you for banking with us.Please eject the card and re-insert it")
                            break
                    if len(NICnumber) == 8 and NIC_chances < 5:
                        print("NIC number is valid. Proceeding with the transaction.")
                        
                
                # dep_amount = int(input("Enter the amount you want to deposite : ")) 
                # amo_chances = 0
                # if dep_amount >= bal:
                #     print(f"Insufficient balance.Please enter the amount less than {bal}")
                #     while dep_amount > bal:
                #         dep_amount = input("Enter the amount : ")
                #         amo_chances = amo_chances + 1
                #         if(amo_chances == 4):
                #             print("Thank you for banking with us.Please eject the card and re-insert it")
                #             break
                #     if dep_amount < bal and amo_chances < 4:
                #         print("Sufficient balance. Proceeding with the transaction.")
                #         bal = bal - dep_amount
                #         print(f"Your current balance is {bal}")
                #         restart = input("If you want to get another service : (Y/N)")
                #         if restart.lower() in ['n','no']:
                #             print('Thank you for banking with us')
                #             break
                
                
             
                amo_chances = 0

                while True:
                    try:
                        dep_amount = int(input("Enter the amount you want to deposit: "))
                        if dep_amount <= 0:
                            print("Please enter a positive amount.")
                            continue

                        if dep_amount > bal:
                            print(f"Insufficient balance. Please enter an amount less than {bal}.")
                            while dep_amount > bal:
                                dep_amount = int(input("Enter a valid amount: "))
                                amo_chances = amo_chances + 1

                                if amo_chances == 4:
                                    print("Too many invalid attempts. Please eject the card and re-insert it.")
                                    break  
                            if amo_chances == 4:  
                                break

                       
                        if dep_amount <= bal:
                            print("Sufficient balance. Proceeding with the transaction.")
                            bal = bal - dep_amount
                            print(f"Your current balance is {bal}")

                            restart = input("Would you like another service? (Y/N): ").strip().lower()
                            if restart in ['n', 'no']:
                                print("Thank you for banking with us!")
                                break  # Exit the entire process

                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
            
            else:
                print("Invalid input.Thank you for banking with us")            
                    

 
                                
                    
               
        
                    
                        
                        
                            
                            
                    
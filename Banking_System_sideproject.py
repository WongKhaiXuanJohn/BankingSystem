
def Admin_login():    # If login user is admin then the system will follow this code and below
    admin_name = str(input("Enter admin username: "))
    str(input("Enter admin password: "))
    print("Welcome " + admin_name + "!\n")
    print("Choose your option:\n1.Create new account\n2.View and search customer\n3.Specific customer's all transactions\n0.Cancel")
    Admin_edit()

def Admin_edit():
    option = int(input("Enter your option: "))
    
    if(option == 1):
        number = int(input("Enter number of new accounts to be created: "))
        data_file = open("Admin_file.txt", "a")
        mylist = []
        for i in range(number):
            print("Enter "+ str(i+1)+ " Customer Details: ")
            customer_id = int(input("Enter New Customer ID Number: "))
            customer_login_name = str(input("Enter New Customer Login ID: "))
            customer_password = str(input("Enter New Customer Password: "))
            data_file.write(str(customer_id)+"\t"+customer_login_name+"\t"+customer_password+"\n")
            mylist.append(str(customer_id) + " " + customer_login_name + " " + customer_password)
        data_file.close()

        data_file = open("Admin_file.txt", "r")
        print(data_file.read())
        data_file.close()
    
        print("Congatulations, all new accounts have been created")
        print("Your list of new created accounts are: ", mylist)        # This print list function is for future use.
                                                                        # If next time newly created then can see in summary instead of showing all accounts in text file
    elif(option == 2):
        data_file = open("Admin_file.txt", "r")
        print(data_file.read())
        data_file.close()
        
        data = str(input("Enter customer information to search: "))
        data_file = open("Admin_file.txt", "r")
        for line in data_file:
            line = line.rstrip()
            if data in line:
                print(line)

    elif(option == 3):        
        data = str(input("Enter specific customer information: "))
        data_file = open("Customer_file.txt", "r")
        for line in data_file:
            line = line.rstrip()
            if data in line:
                print(line)
        
    elif(option == 0):
        print("Goodbye! Have a nice day")
        exit()
        
    else:
        print("Invalid choice, choose again!")
        Admin_edit()

    
def Customer_login():    # If login user is customer then system will follow this code and below
    customer_name = str(input("Enter customer username: "))
    str(input("Enter customer password: "))
    print("Welcome " + customer_name + "!")
    print("Choose your choice:\n1.Perform Transactions\n2.View Own Transactions\n0.Quit")

    option = int(input("Enter your choice: "))

    if(option == 1):
        print("Select the type of transaction you desired")
        print("1.Deposit\n2.Withdrawl\n0.Cancel")

        select = int(input("Select your option: "))

        if(select == 1):
            transaction_deposit()
            
        elif(select == 2):
                transaction_withdrawl()

        elif(select == 0):
            print("Goodbye, See you again!")

        else:
            print("Invalid choice, Goodbye!")
            exit() 

    elif(option == 2):       
        data_file2 = open("Customer_file.txt", "r")
        
        customer_name 
        for line in data_file2:
            line = line.rstrip()
            if customer_name in line:
                print(line)

    elif(option == 0):
        print("Have a nice day and see you again!")
        
    else:
        print("Invalid Choice")
        exit()

                
def transaction_deposit():
    data_file2 = open("Customer_file.txt", "a")
    customer_name = str(input("Enter customer username: "))
    deposit = str(input("Enter deposit amount: "))
    status = "Deposit Action"
    data_file2.write(customer_name+"\t"+str(deposit)+"\t"+status + "\n")
    data_file2.close()

    print("You have deposited " + "RM " + deposit + " !")

def transaction_withdrawl():
    data_file2 = open("Customer_file.txt", "a")
    customer_name = str(input("Enter customer username: "))
    withdrawl = str(input("Your withdrawl amount: "))
    status = "Withdrawl Action"
    data_file2.write(customer_name+"\t"+str(withdrawl)+"\t"+status + "\n")
    data_file2.close()

    print("You have withdrawl " + "RM " + withdrawl + " sucessfully!")


def main():    # First page of bank system will land on this code
    print("Welcome To Prime Bank")
    print("User Type:\n1.Admin Login\n2.Customer Login\n0.Terminate System")

    selection = int(input("Enter your selection here: "))

    if(selection == 1):
        Admin_login()

    elif(selection == 2):
        Customer_login()

    elif(selection == 0):
        print("Have a nice day, GoodBye!")
        exit()

    else:
        print("Invalid Choice\n")
        main()


main()    # Bank system starts from here
    














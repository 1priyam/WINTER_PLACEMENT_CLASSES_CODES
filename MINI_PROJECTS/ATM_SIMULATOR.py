#-------------------------------------------------------  ATM SIMULATOR PROJECT   ------------------------------------------------

file_name = "atm_data.txt"
#balance is a global variable that stores money
balance = 1000


pin = "1234"                                      #pin is a global variable that stores ATM pin

#-------------------------------------------------------  LOAD DATA  -------------------------------------------------------------
def load_data():
    global balance, pin                           #global keywords allows us to modify outside variables global balance, pin
    try:
        file=open(file_name,"r")
        lines=file.readlines()
        file.close()
        pin=lines[0].strip()                      #strip - is removing space from the ending and beginning
        balance=int(lines[1].strip())             #it contains balance
    except:
        pass                                      # if file does not exist or error occurs, pass - DO nothing EAT five star
                                                  #   program will use default balance


#-------------------------------------------------------  CHECK BALANCE  ----------------------------------------------------------
def check_balance():
    print("Your Balance is: ",balance)

#-------------------------------------------------------  SAVE DATA  --------------------------------------------------------------
def save_data():
    file = open(file_name,"w")                   # opening a file in write mode 
    file.write(pin+"\n")                         # write a pin into the file and go to next line
    file.write(str(balance))                     # write balance as string
    file.close()                                 # close the file



#-------------------------------------------------------  DEPOSIT MONEY  ----------------------------------------------------------
def deposit_money():
    global balance                               #gloabal allows changing original balance
    try:
        amount=int(input("enter amount to deposit: "))
        balance = balance + amount               #save updated balance to the file
        save_data()
        print("Money Deposited Successfully")
    except:
        print("please enter numbers only ")


#-------------------------------------------------------  WITHDRAW MONEY  ----------------------------------------------------------
def withdraw_money():
    global balance
    try:
        amount=int(input("enter amount u want to withdraw: "))
        if(amount>balance):
            print("Insufficient balance ")
        else:
            balance = balance - amount
        save_data()
        print("Please collect your cash !!!!")
    except:
        print("Please enter numbers only ")


#-------------------------------------------------------  CHANGE PIN  ---------------------------------------------------------------
def change_pin():
    global pin
    #Ask user for old pin
    old_pin = input("Enter the old pin: ")
    #Check if old pin matches 
    if old_pin==pin:
        #ask for new pin
        new_pin = input("Enter your new pin: ")
        pin = new_pin
        save_data()
        print("Pin changed successfully!!!!!")

    else:
        print("Incorrect Pin")


#-------------------------------------------------------  MAIN FUNCTION  ----------------------------------------------------------
def main():
    #load data when program starts
    load_data()
    #ask user to enter pin
    user_pin=input("enter the pin: ")
    #if pin is wrong stop the program 
    if user_pin != pin:
        print("Incorrect PIN")
        return
    while True:
        print("\n-----------  ATM MENU  -----------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Changing Pin")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice =="1":
            check_balance()
        elif choice =="2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            change_pin()

        elif choice == "5":
            print("---------  Thank you for using ATM  --------- ")
            break
        else:
            print("Invalid Choice")


main()



#************************************************************  PROJECT ENDS  *******************************************************************************
account_list=[4001,4002,4003,4004,4005]
balance_list=[2500,3000,8000,6500,1000]
amount=4000
account_number=4003
transaction_type="Withdraw"

flag=None
if(transaction_type=="Withdraw"):
    for index in range(0,len(account_list)):
        if(account_list[index]==account_number):
            flag=True
            value=index
    if(flag==True):
        balance=balance_list[value]
        new_balance=balance-amount
        if(new_balance >= 500):
            balance_list[value]=new_balance
            print("Transaction completed successfully")
            print("Balance Amount :", new_balance)
        else:
            print("Insufficient Balance")
    else:
        print("Invalid Account number")

elif(transaction_type=="Deposit"):
    for index in range(0,len(account_list)):
        if(account_list[index]==account_number):
            flag=True
            value=index
    if(flag==True):
        balance=balance_list[value]
        new_balance=balance+amount
        balance_list[value]=new_balance
        print("Transaction completed successfully")
        print("Balance Amount :", new_balance)
    else:
        print("Invalid Account number")
elif(transaction_type=="Balance Enquiry"):
    for index in range(0,len(account_list)):
        if(account_list[index]==account_number):
            flag=True
            value=index
    if(flag==True):
        balance=balance_list[value]
        print(balance)
    else:
        print("Invalid Account number")
else:
    print("Invalid Transaction Type")

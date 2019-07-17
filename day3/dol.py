# Dictionary of lists
accts_dic={"001":["Isaac","Appiah","Loan",10.00], "002":["Nii","Okai","Savings",200.50], "003":["Elizabeth","Ofori","Current",5000.00]}
print(f"Dictionary of lists: \n {accts_dic}")

# Deposit function
def deposit(accnt_no,amnt):
    accts_dic[accnt_no][3]=accts_dic[accnt_no][3]+amnt
    return accts_dic

deposit("001",50) 
print(f"After deposit, your account details are: \n {accts_dic}")

# withdraw function
def withdraw(accnt_no,amnt):
    accts_dic[accnt_no][3]=accts_dic[accnt_no][3]-amnt
    return accts_dic

withdraw("001",40) 
print(f"After withdrawal, your account details are: \n {accts_dic}")

# List of dictionaries
dic1={"first_name":"Isaac", "last_name":"Appiah","accnt_type":"Loan","balance":10.00}
dic2={"first_name":"Nii","last_name":"Okai","accnt_type":"Savings","balance":200.50}
dic3={"first_name":"Elizabeth","last_name":"Ofori","accnt_type":"Savings","balance":500.00}

list_of_dic=[dic1,dic2,dic3]

print(f"List of dictionaries: \n {list_of_dic}")
print(list_of_dic[1]["balance"])
# Deposit function
def deposit(index,amnt):
    list_of_dic[index]["balance"]=list_of_dic[index]["balance"]+amnt
    return list_of_dic

deposit(1,50) 
print(f"After deposit, account details are: \n {list_of_dic}")

# Wihdraw function
def withdraw(index,amnt):
    list_of_dic[index]["balance"]=list_of_dic[index]["balance"]-amnt
    return list_of_dic

withdraw(1,20)
print(f"After withdrawal, account details are: \n {list_of_dic}")
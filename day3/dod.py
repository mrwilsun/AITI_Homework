#Dictionary of dictionaries
dic1={"first_name":"Isaac", "last_name":"Appiah","accnt_type":"Loan","balance":10.00}
dic2={"first_name":"Nii","last_name":"Okai","accnt_type":"Savings","balance":200.50}
dic3={"first_name":"Elizabeth","last_name":"Ofori","accnt_type":"Savings","balance":500.00}
dic_of_dic={"001":dic1,"002":dic2,"003":dic3}
print(f"Dictionary of dictionaries: \n {dic_of_dic}")

# Deposit function
def deposit(accnt_no,amnt):
    dic_of_dic[accnt_no]["balance"]=dic_of_dic[accnt_no]["balance"]+amnt
    return dic_of_dic

deposit("001",50) 
print(f"After deposit, account details are: \n {dic_of_dic}")

def withdrawal(accnt_no,amnt):
    dic_of_dic[accnt_no]["balance"]=dic_of_dic[accnt_no]["balance"]-amnt
    return dic_of_dic

withdrawal("001",30) 
print(f"After withdrawal, account details are: \n {dic_of_dic}")
import re

def word_count(file,search_item):
    # file manipulation
    f=open(file,"r")
    data=f.read()
    f.close()

    x=re.findall(search_item,data)
    print(f"The word '{search_item}'  appears {len(x)} times")

def count_lines(file):
    f=open(file,"r")
    data=f.read()
    f.close()
    
    x=re.findall("\n",data)
    print(f"The file has {len(x)+1} lines")

count_lines("hello.txt")
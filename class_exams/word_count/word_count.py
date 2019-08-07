import  re

def word_count(file,search_item):
    # file manipulation
    f=open(file,"r")
    data=f.read()
    f.close()
    # splitting according to number of spaces
    words = data.split(" " )
    # intitalizing counter
    count=0
    for i in words:
        if i== search_item:
            count+=1
    num_words = len(words)
    print(f"The word {search_item} occured {count} times.")
def line_count(file):
    f=open(file,"r")
    data=f.read()
    f.close()

    lines=data.split("\n")
    for l in lines:
        if not l:
            lines.remove(l)
    line_count=len(lines)
    print(f"The file contains {line_count} lines")
word_count("hello.txt","the")

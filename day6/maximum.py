#finding the largest number in a list  
l1=[1,3,2,8,5,-1]

def maximizer(li):
    max=l1[0]
    for i in li:
        if i>max:
            max=i
    print (f"The highest number in the list {li} is {max}")

maximizer(l1)6
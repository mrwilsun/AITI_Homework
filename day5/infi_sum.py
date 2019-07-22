# finds the sum of an infinte number of arguments
#uses the for loop
def sum(*args):
    sum=0
    for i in args:       
        sum=sum+i
    print(sum)



def adder(*numbers):
    sum=0
    i=0
    while i!=len(numbers):
        sum=numbers[i]+sum
        i=i+1
    print(numbers)
    print (sum)

adder(5,6,7)
    
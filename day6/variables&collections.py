# Variables and collections
print ("I'm Python. NIce to meet you!")

user_input =input("Enter some data:")

some_var =5

print("yahoo!") if 3>2 else print (2)

li=[4,5,6]
li.append(1)
li.append("banku")
li.append(9)

print(li)

li.pop()
print(li)

li[0]=42
print(li)

print(li[-1])

print(li[1:3])

print(li[2:])

print(li[:3])
# selecting every second entry
print(li[::2])
# reverse of the list
print(li[::-1])
# inserting into a specific index
li.insert(1,2)
print(li)

# getting the index of a value
print(li.index(2))
# checking for existence
print(1 in li)
# finding the length of a list
print(len(li))

# unpacking into Variables
a,b,c =(1,2,3)
g=4,5,6
print(g)

empty_dict={}
filled_dict={"one":1,"two":2,"three":3}

print(filled_dict["one"])

print(type(filled_dict.keys()))

print(filled_dict.items())
# using get to avoid key errors
print(filled_dict.get("four"))

# set default - only inserts into a dictionar if the givenn key is not present
filled_dict.setdefault("five",7)
print(filled_dict)
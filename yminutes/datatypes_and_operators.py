#normal math
print (1+1)
print(8-1)
print(10*2)
print(35/7)
print(5/2)
#modulo
print (7%3)
# exponentiation (x to the yth power)
print (2**4)

#enforcing precedence with parentheses
print ((1+3)*2) #giving 8 instead of 10 if there was no parentheses

#Boolean operators
#and & or are case sensitive
print (True and False)
print (False or True)

# Boolean operators with integers
print(0 and 2)
print(-5 or 0)
print(0==False)
print(2==True)
print(1==True)

print(not True)
print(not False)

# equality(==)
print (1==1)
print (2==1)

#inequality (!=)
print (1!=1)
print (2!=1)

# comparisons
print(1<10)
print(1>10)
print(2<=2)
print(2>=2)

# chained comparisons
print(1<2<3)
print(2<3<2)

#strings
print("This is a string")
print('This is also a string')
print(""" Just experimenting """)

# adding strings
print("Hello "+"world!")
#adding without the +
print("Hello " "world!")

#multiplying strings
print("Hello" * 3)

# treating a string as a list og characters
print("This is a string"[1])

#finding length of a string
print(len("This is a string"))

#string formatting with %
x="apple"
y="lemon"
z="The items in the basket are %s and %s" %(x,y)
print(z)

#format method
print("{} is a {}".format("This","placeholder"))
print("{0} can be {1}".format("strings","formatted"))
#using keywords
print("{name} wants to eat {food}".format(food="lasanga",name="Bob"))

print(None)

# equality is not used to compare objects to None
# use "is" instead
print("etc" is None)
print(None is None)
# but equality still works though
print(None == None)

# falsey and truthy values
print(bool(0))
print(bool(""))
print(bool("Hello"))

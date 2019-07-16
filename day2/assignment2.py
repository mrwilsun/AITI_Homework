#1 Printing a string with double quotation marks
print ('"There is no difference between the greek and the jew."')

#2  A string that uses an apostrophe
print("This \', is an apostrophe")

#3 A string that spans across multiple lines
print("Let us \n move to the next line.")

#4 A one-line string written on multiple lines
print("No \
multiline here")

#5 A string and its length
message = "I am groot!"
message_lenght = len(message)

#5 Printing the length
print("Message is %d characters long" %message_lenght)

#6 Two concatenated strings
response = "I am also Yorick"

print(message+response)

#7 Strings with a comma in between
conversation = message + "," + response
print(conversation)

# Printing "zing" from "bazinga" using subscripting and index numbers
new_word ="bazinga"
print(new_word[2:-1])
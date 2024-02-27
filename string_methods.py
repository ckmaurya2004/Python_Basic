# str1 = " this is a one line string "
# print(str1)
# print(str1.strip()) # remove  any white space before and after the string

# str2 = "i am kiran !!!"
# print(str2.rstrip("!")) # remove any trailling (last ka)character


# str3 = " I am kiran maurya and I am student of BCA" # all occurrences
# print(str3.replace("I",'my'))
# print(str3.find('I')) # one occurrence

# str4 = "i am kiran maurya and i am student of BCA"
# print(str4.capitalize()) # first character to uppercase while all characters in lower case

# str5 = "I am kiran maurya and i am student of BCA"
# print(str5.center(50)) # it prints the statement in given position according to  given value by user in center parameter

# str6 = "I am kiran maurya and I am student of BCA"
# print(str6.count('I')) #2
# print(str6.endswith("A"))# True
# print(str6.endswith("n",4,8))# False
# print(str6.endswith("n",4,10))# True
# print(str6.startswith('I')) # True

# str7 = "Iamkiran123KI"
# print(str7.isalnum()) # True => it return True only characters in A-Z,a-z,0-9 without any space , if include comma(,)  and space and etc so return False
# str8 = "I am kiran"
# print(str8.isalnum()) # False

# str9 = "Iamkiran"
# print(str9.isalpha()) # True => not include any other characters and not digit 

# str10 = "123"
# print(str10.isdigit()) # True 


# str11 = " i am kiran maurya "
# print(str11.islower()) # True => It returns True  if all characters are the lower case 

# str12 = "I AM KIRAN MAURYA"
# print(str12.isupper()) # True => It returns True if all characters are upper case

# str13 = " i am kiran maurya  "
# print(str13.isprintable()) # True => It returns True if all characters are printable

# str14 = "   "
# print(str14.isspace()) # True => It returns True only and only if the string is contains white space

# str15 = " I Am Kiran Maurya "
# print(str15.istitle()) # True => if first letter of each word of the string is captitalized then return True other False

# str16 = 'I am Kiran Maurya'
# print(str16.swapcase()) # lower to upper / upper to lower

str17 = " I AM KIRAN MAURYA "
print(str17.title()) # first letter is upper and all in lower case
print(str17.casefold()) # returns a copy of a string with all characters in lowercase



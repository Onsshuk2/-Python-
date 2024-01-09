#EX1
str1=input("Enter string: ")
str_1=str1[::-1]
if str1==str_1:
    print("This word is palindrome",str_1)
else:
    print("This word isn't palindrome")
#EX2
text1=input()
word1=input()
text2=" "
word=" "
for i in text1:
    if i.isalpha():
       word+=i
    else:
        if word.lower() in word1:
            text2+=word.upper()
        else:
            text+=word
        text2+=i
        word=" "
print(text2)
#EX3
text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
endText='.','!','?'
count=0
for i in text:
    if i in endText:
        count+=1
print("Number of sentanse", count)







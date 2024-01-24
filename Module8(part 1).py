with open ('file1.txt','w+',encoding='utf-8') as file1:
    file1.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry.\nLorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. \nIt has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. \nIt was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
with open ('file2.txt','w+',encoding='utf-8') as file2:
    file2.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. \nIt is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.  \nIt has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. \nIt was popularised in the of letters, as opposed to using 'Content here, content here', making it look like readable English.\nMany desktop publishing packages with desktop publishing software like Ipsum.")    
#EX1
part1="file1.txt"
part2="file2.txt"
with open (part1,'r',encoding='utf-8') as file1,open(part2,'r',encoding='utf-8') as file2:
    lines1=set(file1.readlines())
    lines2=set(file2.readlines())
diference1=list(lines1-lines2)
diference2=list(lines2-lines1)
print(f"Lines that do not match in:\n {part1}\n{diference1}\n and in: \n {part2}\n{diference2}")
#EX2
with open('file1.txt', 'r', encoding='utf-8')as file1:
    contentInFile=file1.read()
symbols=len(contentInFile)
line=len(contentInFile.splitlines())
vowel='eyuioa'
vowelCount=sum(file1.lower() in vowel for file1 in contentInFile)
consonant='qwrtpsdfghjklzxcvbnm'
consonantCount=sum(file1.lower() in consonant for file1 in contentInFile)
digit=sum(file1.isdigit() for file1 in contentInFile)

with open ('file3.txt','w+',encoding='utf-8') as file3:
    file3.write(f"Number of symbols\n{symbols}\nNumber of lines\n{line}\nNumber of vawel\n{vowelCount}\nNumber of consonant\n{consonantCount}\nNumber of digit\n{digit}")

#EX3
with open('file1.txt', 'r+', encoding='utf-8')as file1:
    contentInFile=file1.readlines()
contentInFile.pop()

with open ('file3.txt','a',encoding='utf-8') as file3:
    file3.write(f"\nNew file\n{contentInFile}")

#EX4
with open('file1.txt', 'r+', encoding='utf-8')as file1:
    contentInFile=file1.readlines()
maxLine=max(len(contentInFile) for line in contentInFile)
print(f"Longest line:\n{maxLine}")

#EX5
wordUser=input("Enter word: ")
with open('file1.txt', 'r', encoding='utf-8')as file1:
    contentInFile=file1.read()
count=contentInFile.lower().split().count(wordUser.lower())
print(f"Word {wordUser} occurs in the file {count} times")

#EX6
with open('file1.txt', 'r', encoding='utf-8')as file1:
    contentInFile=file1.read()
wordDelite=input("Enter word to delite: ")
wordNew=input("Enter new word: ")
updateFile=contentInFile.replace(wordDelite,wordNew)

with open('file1.txt', 'w', encoding='utf-8')as file1:
    file1.write(updateFile)
    








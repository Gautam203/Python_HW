#If there is vowel print it contains vowel or print it doesn't contain any vowels ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
str = input("Enter the String : ")
Vowel="aeiouAEIOU"
v=False
i=0
c=0
while i<len(str):
    if str[i] in Vowel:
        c+=1
        v=True
        break
    i+=1
    c+=1

print(c)

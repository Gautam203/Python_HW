lst=[]
l=int(input("enter the lenght of list : "))
for i in range(l):
    value=input("Enter the value : ")
    lst.append(value)
def l_w(lst):
    l_w=''
    for word in lst:
        if len(word) > len(l_w):
            l_w=word
    return l_w
print("list is :",lst)
print("The longest word id : ",l_w(lst))

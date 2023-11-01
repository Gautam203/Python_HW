def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {}
n = int(input("Enter number of key-value pairs for dictionary 1: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

dict2 = {}
m = int(input("Enter number of key-value pairs for dictionary 2: "))
for i in range(m):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

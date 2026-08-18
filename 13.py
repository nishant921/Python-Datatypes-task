# Q3: Convert List to List of dictionaries. Given list values and keys list, convert these values to key value pairs in form of list of dictionaries.
# Example 1:

# Input:

# list = ["NISHANT", 69, "Nish", 11]
# key_list = ["name", "id"]
# Output:

# [{'name': 'NISHANT', 'id': 69}, {'name': 'Nish', 'id': 11}]
# Example 2:

# Input:

# test_list = ["Neev", 66]
# key_list = ["name", "id"]
# Output:

# [{'name': 'Neev', 'id': 66}]

test_list = ["NISHANT", 69, "Nish", 11]
key_list = ["name", "id"]
l=[]

for j in test_list:
    for i in key_list:
        d={}
        d[i]=j
    l.append(d)

print(l)
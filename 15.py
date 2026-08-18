# Q5: Sort Dictionary key and values List.
# Example 1:

# Input:

# {'c': [3], 'b': [12, 10], 'a': [19, 4]}
# Output:

# {'a': [4, 19], 'b': [10, 12], 'c': [3]}
# Example 2:

# Input:

# {'c': [10, 34, 3]}
# Output:

# {'c': [3, 10, 34]}

d={'c': [3], 'b': [12, 10], 'a': [19, 4]}
# d= {'c': [10, 34, 3]}
temp={}

for key in sorted(d):
    for keys,value in d.items():
        if key==keys:
            temp[key]=sorted(value)
print(temp)


# or
temp={}
for key in sorted(d):
    temp[key]=sorted(d[key])
print(temp)

# or

temp = {key: sorted(d[key]) for key in sorted(d)}
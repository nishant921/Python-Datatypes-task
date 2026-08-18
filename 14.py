# Q4: Convert a list of Tuples into Dictionary.
# Example 1:

# Input:

# [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
# Output:

# {'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}
# Example 2:

# Input:

# [('A', 1), ('B', 2), ('C', 3)]
# Output:

# {'A': [1], 'B': [2], 'C': [3]}


l= [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
# [('A', 1), ('B', 2), ('C', 3)]


d={}
for t in l:
    for i in t:
        d[t[0]]=[i]
print(d)
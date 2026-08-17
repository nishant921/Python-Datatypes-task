# Q2: Replace words from Dictionary. Given String, replace it’s words from lookup dictionary.
# Example 1:

# Input:

# test_str = 'CampusX best for DS students.'
# repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}
# Output:

# CampusX is the best channel for Data-Science students.
# Example 2:

# Input:

# test_str = 'CampusX best for DS students.'
# repl_dict = {"good" : "is the best channel", "ds" : "Data-Science"}
# Output:

# CampusX best for DS students.

test_str = 'CampusX best for DS students.'
repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}


temp = test_str.split()

for key,value in repl_dict.items():
    if key in temp:
        indexx = temp.index(key)
        temp.remove(key)
        temp.insert(indexx,value)
print(" ".join(temp))
 


# or
test_str = 'CampusX best for DS students.'
repl_dict = {"best": "is the best channel", "DS": "Data-Science"}

temp = test_str.split()

for i in range(len(temp)):
    if temp[i] in repl_dict:
        temp[i] = repl_dict[temp[i]]

print(" ".join(temp))
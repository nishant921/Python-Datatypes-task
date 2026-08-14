# Q1: Join Tuples if similar initial element
# While working with Python tuples, we can have a problem in which we need to perform concatenation of records from the similarity of initial element. This problem can have applications in data domains such as Data Science.
# For eg.
# Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)] 
# Logic:
# Look at the first element of each tuple.
# If it has appeared before:
# Add the remaining values to the existing tuple.
# Otherwise:
# Create a new entry.

import ast

t = ast.literal_eval(input("Enter list of tuples: "))


# t = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
d={}

for item in t:
    key=item[0]
    if key in d: 
        d[key]+=item[1:]
    else:
        d[key]=item[1:]
print(d)
r=[]
for key,value in d.items():
    r.append((key,)+value)
  
print(r)

print({5:(5,6,7)}.items())



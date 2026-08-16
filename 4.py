# # Q4: Count no of tuples, list and set from a list
# # list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

# # Output:

# # List-2
# # Set-2
# # Tuples-1

# list1 = [
#     {'hi', 'bye'},
#     {'Geeks', 'forGeeks'},
#     ('a', 'b'),
#     ['hi', 'bye'],
#     ['a', 'b']
# ]

# set_count = 0
# list_count = 0 
# tuple_count = 0
# for item in list1:
#     if isinstance(item, set):
#         set_count += 1
#     elif isinstance(item, list):
#         list_count += 1
#     elif isinstance(item, tuple):
#         tuple_count += 1
# print("List :", list_count)
# print("Set :", set_count)
# print("Tuple :", tuple_count)


# # ANOTHER WAY
# list1 = [
#     {'hi', 'bye'},
#     {'Geeks', 'forGeeks'},
#     ('a', 'b'),
#     ['hi', 'bye'],
#     ['a', 'b']
# ]

# set_count = 0
# list_count = 0
# tuple_count = 0
# for item in list1:
#     if type(item) == set:
#         set_count += 1
#     elif type(item) == list:
#         list_count += 1
#     elif type(item) == tuple:
#         tuple_count += 1

# print("List :", list_count)
# print("Set :", set_count)
# print("Tuple :", tuple_count)


# # another way
# list1 = [
#     {'hi', 'bye'},
#     {'Geeks', 'forGeeks'},
#     ('a', 'b'),
#     ['hi', 'bye'],
#     ['a', 'b']
# ]

# list_count = sum(isinstance(item, list) for item in list1)
# set_count = sum(isinstance(item, set) for item in list1)
# tuple_count = sum(isinstance(item, tuple) for item in list1)

# print("List :", list_count)
# print("Set :", set_count)
# print("Tuple :", tuple_count)

import ast

l = ast.literal_eval(input())

print(l)
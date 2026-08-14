# Q2: Multiply Adjacent elements (both side) and take sum of right and left side multiplication result.
# For eg.

# The original tuple : (1, 5, 7, 8, 10)
# Resultant tuple after multiplication : 

# (1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)

# output-(5, 40, 91, 136, 80)

t = tuple(map(int,input("Enter Elements: ").split()))
print("Original tuple: ",t)
length=len(t)

if length<2:
    print("Tuple must have at least 2 Elements!")

else:
    l=[]
    for i in range(len(t)):
        if i==0:
            l.append((t[i]*t[i+1]))
        elif i==len(t)-1:
            l.append((t[i]*t[i-1]))
        else:
            l.append((t[i-1]*t[i]+t[i]*t[i+1]))
    print(tuple(l))

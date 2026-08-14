# Q3: Check is tuples are same or not?
# Two tuples would be same if both tuples have same element at same index

# t1 = (1,2,3,0)
# t2 = (0,1,2,3)

# t1 and t2 are not same

t1 = (1,2,3,0)
t2 = (1,2,3,0)
# print(t1==t2)
if len(t1)==len(t2):
    if t1==t2:
        print(f"t1: {t1} and t2: {t2} Tuples are same")
    else:
        print(f"t1: {t1} and t2: {t2} Tuples are not same")
else:
    print("Tuples are not of same size they cannot be same")


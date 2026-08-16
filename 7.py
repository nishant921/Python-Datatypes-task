# Q2: Write a program to count unique number of vowels using sets in a given string. Lowercase and upercase vowels will be taken as different.
# Input:

# Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
# Output:

# No of unique vowels-6

s={'a','e','i','o','u','A','E','I','O','U'}
print(s)

str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"

temp=set()
for i in str1:
    if i in s:
        temp.add(i)
print(f"No. of Unique Vowles: {len(temp)}")


# OR
vowels = {'a','e','i','o','u','A','E','I','O','U'}

str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"

unique_vowels = set(str1) & vowels

print(unique_vowels)
print("No. of Unique Vowels:", len(unique_vowels))

# OR
vowels = {'a','e','i','o','u','A','E','I','O','U'}

unique_vowels = {ch for ch in str1 if ch in vowels}

print(unique_vowels)
print(len(unique_vowels))
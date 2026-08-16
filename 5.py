# Q5: Shortlist Students for a Job role
# Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.

# Show every students record in form of tuples if matches all required criteria.

# It is assumed that there will be only one primry skill.

# If no such candidate found, print No such candidate

# Input:

# Enter No of records- 2
# Enter Details of student-1
# Enter Student name- Manohar
# Enter Higher Education- B.Tech
# Enter Primary Skill- Python
# Enter Year of Graduation- 2022
# Enter Details of student-2
# Enter Student name- Ponian
# Enter Higher Education- B.Sc.
# Enter Primary Skill- C++
# Enter Year of Graduation- 2020

# Enter Job Role Requirement
# Enter Skill- Python
# Enter Higher Education- B.Tech
# Enter Year of Graduation- 2022
# Output

# ('Manohar', 'B.tech', 'Python', '2022')

n=int(input("Enter NO. of Entries:"))
information=[]
for i in range(n): 
    information.append(   
        {
    'Id': int(input("Enter students id: ")),
    'Name':(input("student Name: ")),
    'Higer_ed':input("Higher Education: "),
    'Skill':input("Primary Skill[only-one]: "),
    'Graduated_year':int(input("Year of Graduation: "))
    }
    )
    
print(information)
print('-'*60)
print("Job Role Requirements: ")
prim_skill=input("Required Primary Skill: ")
edu=input("Required Education: ")
year=input("Year of Graduation(2000,2022,2024): ")
print('-'*60)

found = False

for info in information:

    if (info['Skill'] == prim_skill and
        info['Higer_ed'] == edu and
        str(info['Graduated_year']) == year):


        print(tuple(info.values()))
        # l=[]
        # for t in info.values():
        #     l.append(t)
        # print(tuple(l))
        # print(info)
        found = True


if not found:
    print("No such Candidate!")
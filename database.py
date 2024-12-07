# DataBase-Manipulation-using-Python
DataBase Manipulation using Python having sample of data in list format having tuples as elements
emp_db=[
    (1,'Akki','Maths',2000),
    (2,'kavitha','physics',5000),
    (5,'ram','Maths',51000),
    (3,'Swapna','DBMS',4000),
    (4,'Ramya','C',10000),
    (6,'Sri','Maths',1100)
]

#print least salary employees
min_sal=float("inf")
for i in emp_db:
  if i[3] < min_sal:
    min_sal=i[3]
print(f"The minimum salary is: {min_sal}")

#print max salary employees
max_sal=0
for i in emp_db:
  if i[3] > max_sal:
    max_sal=i[3]
print(f"The maximum salary is: {max_sal}")

#maths employees
print("\nEmployees who is teaching Maths")
for i in emp_db:
  if i[2].lower() == 'maths':
    print(" ",i[1].capitalize())

#sorting employees based on salaries
emp_db.sort(key=lambda x:x[3])
print("\nSorted database according to salary:------")
for i in emp_db:
  print(" ",i)

#print employees whose letter start with R
print("\nEmployees name starts with R:--------")
for i in emp_db:
  if i[1][0].upper()=='R':
    print(" ",i[1].capitalize())

#print of employees whose salary is b/w 1000 to 5000
print("\nEmployees whose salary is b/w 1000 and 5000")
for i in emp_db:
  if i[3] >= 1000 and i[3] <= 5000:
    print(" ",i[1]," ",i[3])
    
#data of even id employees
print("\nEmployees whose id's are even")
for i in emp_db:
  if i[0]%2==0:
    print(" ",i[0],"-->",i[1]," ",i[3])

#count number of vowels in each employee name
print("\nCount Vowels in each employee Name")
m={}
for i in emp_db:
  name=i[1]
  v=0
  for j in name:
    if j.lower() in "aeiou":
      v+=1
  m[name]=v
print(" ",m)
      
#Reverse the character in subjects and print only subjects
print("\nReverse the characters of subjects and displaying them--------")
for i in emp_db:
  print(" ",i[2],"--->",i[2][::-1])
  
#print the name in lowercase and subject in uppercase
print("\nPrinting name in lowercase and subject in uppercase--------")
for i in emp_db:
  print(" ",i[1].lower()," ",i[2].upper())

#Generate user id for each user by concatenation of name and id (akki_1)
print("\nUser Id Generation-------")
for i in emp_db:
  print(" ",i[1]+'_'+str(i[0]))


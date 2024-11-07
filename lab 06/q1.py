
# file = open('myInfo.txt', 'w')
# file.write('Name : Sajid Ali Khan\n')
# file.write('Roll no : 211370213\n')
# file.write('Department : Cs\n')
# file.close()

# file = open('myInfo.txt','r')
# data = file.read()

# for line in file.readlines():
#     print(line) 
# print(file.readline())
# print(data)


import csv


# fields = []
# rows = []

# with open("emp.csv","r") as file:
#     reader = csv.reader(file)

#     fields = next(reader)

#     for row in reader:
#         rows.append(row)

# print("fields : ",fields)
# print("rows : ",rows)


# fields = ["Name", "rollNo","Dept","Semester"]
# rows = [
#     ["Sajid Ali", 211370213, "Cs", 7],
#     ["Ali", 211370218, "SE", 5],
#     ["Ahmad", 211370012, "BBA", 3],
# ]

# with open("students.csv","w") as file:
#     reader = csv.writer(file)

#     reader.writerow(fields)
#     reader.writerows(rows)


import pandas as mypanda

data = mypanda.read_csv(r'emp.csv')
# print(data)

specific = mypanda.DataFrame(data,columns=['Emp_Name'])
print(specific)






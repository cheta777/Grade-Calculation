'''
The main objective of this code is to return the performance of a student
    by taking his marks.

The CPI of other students are assumed to be known and from the input of a student
    the CPI of his marks will be calculated and he will be shown the overview of
    the CPIs of the class and his rank will be provided
'''


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#imported modules[already existed]


import reportcard
#a module we created


name = input("Enter your name : ")
while True:
    try:
        roll = input("Enter your Roll number : ")
        if(roll.isdigit() == True and len(roll) == 7):
            if(roll[3] == '3'or  roll[3] == '4'or  roll[3] == '6'):
                break
            else:
                print("Entered roll number does not match to any of the branch")
        else:
            print("Please enter a valid roll number")
    finally:
        print(" ")

branch = ""
Semester = input("Enter the semester name : ")
faculty_advisor = input("Enter the name of your faculty advisor : ") 
# The above steps take the input of all basic information of the student



f1 = open(r'C:\Users\Veere\Performance.txt',"w")
# We created a file "Performance.txt" to show the student the entire output in a text file 

f1.write("""
  ------------------------------------------------------
 |======================================================  
 |******INDIAN INSTITUTE OF TECHNOLOGY GOA************  |
 |****************STUDENT REPORT CARD ****************  |    
 |======================================================|
  ------------------------------------------------------
 \n """)

f1.write("\n\nName of the student : "+name)
f1.write("\nRoll number of the student : "+roll)
f1.write("\nSemester: "+Semester)
f1.write("\nFaculty Advisor: "+faculty_advisor+"\n\n")
# These are file write operations to enter the strings into txt file

reportcard.branch(roll, name, faculty_advisor, Semester)

def inputfloat(text):
    """Ask with 'text' for an input and returns it as float(). Asks until a number is  given."""
    while True:
        try:
            mark= float(input(text))
            if mark in range(0,100):
                return mark
            else:
                print("Out of range ... Try again")
        except ValueError:
            print('Please enter in a number format only')

print("\nEnter the marks in each subject provided the course code\n")


MTH_1021=inputfloat("MTH 1021 : ")
MTH_1022=inputfloat("MTH 1022 : ")
PH_102=inputfloat("PH 102 : ")
PH_104=inputfloat("PH 104 : ")
CH_101=inputfloat("CH 101 : ")
CH_102=inputfloat("CH 102 : ")
CH_104=inputfloat("CH 104 : ")
CS_101=inputfloat("CS 101 : ")
ME_102=inputfloat("ME 102 : ")
CS_102=inputfloat("CS 102 : ")


marks = dict()
# creating a dictionary 'marks' to store the marks of a student

marks = {'MTH 1021': MTH_1021 ,
         'MTH 1022': MTH_1022,
         'PH 102': PH_102,
         'PH 104': PH_104,
         'CH 101': CH_101,
         'CH 102': CH_102,
         'CH 104': CH_104,
         'CS 101': CS_101,
         'ME 102': ME_102,
         'CS 102': CS_102}

print("\n------------------------------------------------------------------------------------\n")
print("""

  ------------------------------------------------------
 |======================================================| 
 |******INDIAN INSTITUTE OF TECHNOLOGY GOA************  |
 |******************** STUDENT REPORT CARD ************ |
 |======================================================|
  ------------------------------------------------------
 \n """)

grade = [[]] * 10
points = [[]] * 10
credits = [[]] * 10

reportcard.grades(marks, grade, points, f1)

'''
We define a function credit() to store the credits of each respective course.
The function consists of initializing the credits of all 10 courses into a list
    called credits[]
'''

def credit():
    credits[0] = 2
    credits[1] = 2
    credits[2] = 3
    credits[3] = 2
    credits[4] = 2
    credits[5] = 2
    credits[6] = 2
    credits[7] = 4
    credits[8] = 2
    credits[9] = 3


x = 0

'''
We define a function called CPI_calculate() which calculates the CPI of the student 
    by using the formula:

CPI = (C1G1 + C2G2 + ...... + CnGn) / (C1 + C2 + ..... + Cn)
    where C1,C2,.... are the credits of courses
          G1,G2,.... are the grades obtained in those respective courses.

The function has three main operations:
    1) numerator calculation from the formula of CPI 
    2) denominator calculation from the formula of CPI
    3) printing a message to the student based on the CPI that he/she has secured.

'''


def CPI_calculate():
    
    global x
    numerator = 0

    for i in range(0,10,1):
        numerator = numerator + (points[i]*credits[i])
    
    denominator = 0
    for j in range(0,10,1):
        denominator = denominator + credits[j]

    cpi = numerator/denominator
    print("\nCPI is",round(cpi,2))
    x = round(cpi,2)
    
    f1.write("\nYour CPI is : "+str(x)+'\n')
    
    if(cpi >= 9.5):
        print("\nYour performance is Outstanding \nAll the best")
    elif(cpi < 9.4 and cpi >= 9.0):
        print("\nYour performance is Excellent \nAll the best")
    elif(cpi < 9.0 and cpi >= 8.0):
        print("\nYour performance is Very Good \nTry to improve by working hard")
    elif(cpi < 8.0 and cpi >= 7.0):
        print("\nYour performance is Good \nMake sure you improve to CPI of 8")
    elif(cpi < 7.0 and cpi >= 6.0):
        print("\nYour performance is Nice \nTry to concentrate in all courses equally")
    elif(cpi < 6.0 and cpi >= 5.0):
        print("\nYour performance is Average \nFocus on important points in each subject")
    else:
        print("\nYour performance is Poor \nMake sure you are improving in easy subjects")

reportcard.feedback(f1, marks)

CPI = []

f = open(r'C:\Users\Veere\CPI.txt',"rt")

for line in f:
    line = line.split('\n')
    if(line[0] != ''):
        CPI.append(float(line[0]))
f.close()

CPI.append(x)

def rank(l):    # list datatype
    global x
    rank = len(l)
    for i in range(len(l)-1):
        if(x > l[i]):
            rank -= 1
    print("Your rank is", rank, "among", len(l),"students")
    f1.write("\nYour rank is "+str(rank)+" among "+str(len(l))+" students\n")


credit()


d={'SubjectName':['MTH 1021','MTH 1022','PH 102','PH 104','CH 101','CH 102','CH 104','CS 101','ME 102','CS 102'],'Score':[marks['MTH 1021'],marks['MTH 1022'],marks['PH 102'],marks['PH 104'],marks['CH 101'],marks['CH 102'],marks['CH 104'],marks['CS 101'],marks['ME 102'],marks['CS 102']],'Grade':[grade[0],grade[1],grade[2],grade[3],grade[4],grade[5],grade[6],grade[7],grade[8],grade[9]]}
df=pd.DataFrame(d)
print(df)


CPI_calculate()
rank(CPI)


f1.close()
print(CPI[len(CPI)-1])


#A dictionary is created to note down the number of students in a particular ranges of CPI
d={"less than 6":0, "6-7":0, "7-8":0, "8-9":0, "9-10":0, "10":0}


for value in CPI:
    if value >=6 and value < 7:
        d["6-7"] += 1
    elif value >=7 and value < 8:
        d["7-8"] += 1
    elif value >=8 and value < 9:
        d["8-9"] += 1
    elif value >=9 and value < 10:
        d["9-10"] += 1
    elif value == 10:
        d["10"] += 1
    else:
        d["less than 6"] += 1

'''
We also wanted to plot a pie chart
For that we need exact portions so we have done calculations and
successfully made the code for getting a pie chart
'''


labels = 'less than 6', '6-7', '7-8', '8-9', '9-10', '10'

total = 0
for key in d.keys():
    total += d[key]
    factor = 100/total


y = np.array([d["less than 6"]*factor, d["6-7"]*factor, d["7-8"]*factor, d["8-9"]*factor, d["9-10"]*factor, d["10"]*factor])
mylabels = ['less than 6', '6-7', '7-8', '8-9', '9-10', '10']

plt.pie(y, labels = mylabels)
plt.legend(title = "CPI:")
plt.show() 









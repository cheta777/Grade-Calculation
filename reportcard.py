# -*- coding: utf-8 -*-

""" A module named reportcard which has some functions defined in it"""

def branch(roll, name, faculty_advisor, Semester):
    """
    arguments:
               parameter(roll) = string datatype
               parameter(name) = string datatype
               parameter(faculty_advisor) = string datatype
               parameter(Semester) = string datatype

    The function takes the string arguments and implements the code and
    determines which branch the student belongs or returns the type of error
    if there is one
    
    """
    
    print("\nName of the student : ",name)
    print("Roll number of the student : ",roll)
    if(roll[3] == '3'):
        if(roll[4] == '1'):
            branch = "Computer Science and Engineering (CSE)"
        elif(roll[4] == '3'):
            branch = "Mathematics and Computing (MnC)"        
    elif(roll[3] == '4'):
        branch = "Electrical Engineering (EE)"
    elif(roll[3] == '6'):
        branch = "Mechanical Engineering (ME)"
    print("Branch of the student : ",branch)
    print("Semester: ",Semester)
    print("Faculty Advisor: ",faculty_advisor)






def grades(marks, grade, points, f1):
    """
    arguments:
               parameter(marks)  = dictionary
               parameter(grade)  = 2D list
               parameter(points) = 2D list
               parameter(f1)     = read/write file

    This functions takes 4 arguments and it basically doesn't return anything
    but the using the marks dictionary it enters the grade of the subject into
    'grade' list and points to 'points' list and the file string adds into the
    file f1

    A+ A B+ B ...... these are grades which will be awarded on the basis of
    marks of student in that subject. We followed a convention for the ranges of
    marks and accordingly grades are given 
    """
    
    i = 0
    for j in marks.keys():
            if(marks[j] >= 90):
                grade[i] = 'A+'
                points[i] = 10
            elif(marks[j] < 90 and marks[j] >= 80):
                grade[i] = 'A'
                points[i] = 9
            elif(marks[j] < 80 and marks[j] >= 70):
                grade[i] = 'B+'
                points[i] = 8
            elif(marks[j] < 70 and marks[j] >= 60):
                grade[i] = 'B'
                points[i] = 7
            elif(marks[j] < 60 and marks[j] >= 50):
                grade[i] = 'C+'
                points[i] = 6
            elif(marks[j] < 50 and marks[j] >= 40):
                grade[i] = 'C'
                points[i] = 5
            elif(marks[j] < 40 and marks[j] >= 30):
                grade[i] = 'D'
                points[i] = 4
            elif(marks[j] < 30 and marks[j] >= 20):
                grade[i] = 'E'
                points[i] = 2
            elif(marks[j] < 20 and marks[j] >= 0):
                grade[i] = 'F'
                points[i] = 0
            f1.write('\n'+j+" : "+grade[i]+'\n')
            i = i + 1






def feedback(f1, marks):
    """
    arguments:
               parameter(marks)  = dictionary
               parameter(f1)     = read/write file
    The name of this function is enough to explain what it does
    From the arguments it prints the FEEDBACK of student
    using if and else statements 

    """

    count  = 0
    print("\nCourses you are strong in : \n")
    f1.write("\nCourses you are strong in : \n")
    for i in marks:
        if(marks[i] >= 70.0):
            print(i)
            f1.write(i+'\n')
            count += 1
    if(count == 0):
        print("-------")
        f1.write("-------")


    count = 0
    print("\nCourses you are good in :\n")
    f1.write("\nCourses you are good in :\n")
    for j in marks:
        if(marks[j] < 70.0 and marks[j] >= 50.0):
            print(j)
            f1.write(j+'\n')
            count += 1
    if(count == 0):
        print("-------")
        f1.write("-------")


    count = 0
    print("\nCourses you must focus on and improve at :\n")
    f1.write("\nCourses you must focus on and improve at :\n")
    for k in marks:
        if(marks[k] < 50.0):
            print(k)
            f1.write(k+'\n')
            count += 1
    if(count == 0):
        print("-------")
        f1.write("-------"+'\n')

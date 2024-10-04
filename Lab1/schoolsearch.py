'''
Author(s): Zaid Serrano, Sinchana Shivaprasad
'''
'''
1. Parser
2. StudentFinder
3. TeacherFinder
4. BusFinder
5. GradeFinder
6. AverageFinder
7. InfoFinder

StLastName, StFirstName, Grade, Classroom, Bus, GPA, TLastName, TFirstName
0           1            2      3          4    5    6          7


part b:

list.txt
StLastName, StFirstName, Grade, Classroom, Bus, GPA
0           1            2      3          4    5  

teachers.txt
TLastName, TFirstName, Classroom
0          1            2

'''
import sys

#error messages
error_MSG_INVALID_COMMAND = "Invalid Command"
error_MSG_INVALID_COMMAND_FORMAT = "Invalid Command Format"
error_MSG_NO_RECORD = "No Record(s) Found"
error_MSG_INVALID_Grade = "Invalid Grade"
error_MSG_INVALID_Bus = "Invalid Bus Route"
error_MSG_INVALID_Classroom = "Invalid Classroom"

#Note: grace will be added to passed names of students and teachers (case insensitive)
def stundent_bus_finder(record, last_name):
    count = 0
    for line in record:
        line = line.split(",")
        if(line[0] == last_name.upper()):
            print(line[0] + ", "  + line[1] + ", "  + line[4])
            count += 1
    if(count == 0):
        print(error_MSG_NO_RECORD)
    return

#NR1
def classroom_student_finder(record, classroom):
    count = 0
    for line in record:
        line = line.split(",")
        if(line[3] == classroom):
            print(line[0] + ", "  + line[1] + ", "  + line[2])
            count += 1
    if(count == 0):
        print(error_MSG_INVALID_Classroom)
    return

# NR 2
def classroom_teacher_finder(teachers, classroom):
    count = 0
    for line in teachers:
        line = line.split(",")
        if(line[2] == classroom):
            print(line[0] + ", "  + line[1] + ", "  + line[2])
            count += 1
    if(count == 0):
        print(error_MSG_INVALID_Classroom)
    return

#NR3
def grade_teacher_finder(teachers, students, grade):
    #go through student records and find students at the given grade level, append the classroom number to a list
    grade_classes = []
    for student in students:
        student = student.split(",")
        if student[2] == grade:
            grade_classes.append(student[3])
    #go through teacher records, check if their class is in the list and print out their info 
    for teacher in teachers:
        teacher = teacher.split(",")
        if teacher[2] in grade_classes:
            print(teachers[0], teachers[1])

#NR4
def enrollment_finder(students):
    class_freq = {}
    #map the classrooms to the number of students in each class
    for student in students:
        student = student.split(",")
        if(student[3] in class_freq):
            class_freq[student[3]] += 1
        else:
            class_freq[student[3]] = 1
    #sort the dictionary by class number
    classList = list(class_freq.keys())
    classList.sort()
    #get the value (number of students) for each class
    for c in classList:
        print(c + ": ", class_freq[c])
    return


def student_finder(record, teachers, last_name):
    count = 0
    teacher_dict = {}
    
    for line in teachers:
        line = line.split(",")
        classroom = line[2]
        teacher_dict[classroom] = (line[0], line[1])
    
    for line in record:
        line = line.split(",")
        if line[0].upper() == last_name.upper():
            teacher_info = teacher_dict.get(classroom, ("Unknown", "Unknown"))
            teacher_last, teacher_first = teacher_info
            
            print(line[0], ", ", line[1], ", ", line[2], ", ", line[3], ", ", line[4], ", ", line[5].strip(), ", ", f"{teacher_last}, {teacher_first}")
            count += 1
    
    if count == 0:
        print(error_MSG_NO_RECORD)
    return

#TODO: find student based on teacher
def teacher_finder(record, teachers, teacher_name):
    count = 0
    classroom = None
    
    for line in teachers:
        line = line.split(",")
        if line[0].upper() == teacher_name.upper():
            classroom = line[2]

    if classroom == None:
        print(error_MSG_INVALID_Classroom)
        return
    for line in record:
        line = line.split(",")
        if line[3].strip() == classroom.strip():
            print(line[0], ", ", line[1])
            count += 1
    if(count == 0):
        print(error_MSG_NO_RECORD)
    return

def grade_max_student_finder(record, grade):
    count = 0
    max_gpa = 0
    #min_gpa = 0
    #first pass finds the max_gpa
    for line in record:
        line = line.split(",")
        if(line[2] == grade):
            max_gpa = max(max_gpa, float(line[5]))
    #second pass prints the student with max_gpa
    for line in record:
        line = line.split(",")
        if((line[2] == grade) & (float(line[5]) == max_gpa)):
            print(line[0] + ", "  + line[1] + ", "  + line[5] + ", "  + line[6] + ", "  + line[7] + ", "  + line[4])
            count += 1
    if(count == 0):
        print(error_MSG_INVALID_Grade)
    return

def grade_min_student_finder(record, grade):
    count = 0
    min_gpa = 10
    #first pass finds the min_gpa
    for line in record:
        line = line.split(",")
        if(line[2] == grade):
            min_gpa = min(min_gpa, float(line[5]))
    #second pass prints the student with min_gpa
    for line in record:
        line = line.split(",")
        if((line[2] == grade) & (float(line[5]) == min_gpa)):
            print(line[0] + ", "  + line[1] + ", "  + line[5] + ", "  + line[6] + ", "  + line[7] + ", "  + line[4])
            count += 1
    #print(min_gpa)
    if(count == 0):
        print(error_MSG_INVALID_Grade)
    return

def grade_student_finder(record, grade):
    count = 0
    for line in record:
        line = line.split(",")
        if(line[2] == grade):
            print(line[0] + ", "  + line[1])
            count += 1
    if(count == 0):
        print(error_MSG_INVALID_Grade)
    return

def bus_student_finder(record, bus):
    count = 0
    for line in record:
        line = line.split(",")
        if(line[4] == bus):
            print(line[0] + ", "  + line[1] + ", "  + line[2] + ", "  + line[3])
            count += 1
    if(count == 0):
        print(error_MSG_INVALID_Bus)
    return

def grade_level_average_finder(record, grade):
    count = 0
    gpa_sum = 0
    for line in record:
        line = line.split(",")
        if(line[2] == grade):
            count += 1
            gpa_sum += float(line[5])
    #check errors before printing (avoid division by zero)
    if(count == 0):
        print(error_MSG_INVALID_Grade)
        return
    average_gpa = gpa_sum/count
    print(grade + ": " + f"{average_gpa:.2f}")    
    return

def info_finder(record):
    grade_dict = {}
    #map the grades to the number of students in each grade
    for line in record:
        line = line.split(",")
        if(line[2] in grade_dict):
            grade_dict[line[2]] += 1
        else:
            grade_dict[line[2]] = 1
    #sort the dictionary by grade
    gradeList = list(grade_dict.keys())
    gradeList.sort()
    #get the value (number of students) for each grade
    for grade in gradeList:
        print(grade + ": ", grade_dict[grade])
    return

def parse_command(command):
    #check if student.txt file exists
    try:
        #open students.txt file and pass to all helper functions
        with open("list.txt") as f:
            record = f.readlines()
        with open("teachers.txt") as t:
            teachers = t.readlines()

        if((command[0] == 'C:') | (command[0] == 'Class:') and len(command) == 3):
                #check 3rd command to see if they want teacher or student info from the class
                if((command[2] == 'S')):
                    classroom_student_finder(record, command[1]) #NR1*
                if((command[2] == 'T')):
                    classroom_teacher_finder(teachers, command[1]) #NR2*
                else:
                    print(error_MSG_INVALID_COMMAND_FORMAT)


        elif((command[0] == 'S:') | (command[0] == 'Student:')):
                if(len(command) == 3):
                    stundent_bus_finder(record, command[1])
                else:
                    student_finder(record, teachers, command[1])

        elif((command[0] == 'T:') | (command[0] == 'Teacher:')): 
            teacher_finder(record, teachers, command[1])
        elif((command[0] == 'G:') | (command[0] == 'Grade:')): 
            if(len(command) == 3):
                if((command[2] == 'H') | (command[2] == 'High')):
                    grade_max_student_finder(record, command[1])
                elif((command[2] == 'L') | (command[2] == 'Low')):
                    grade_min_student_finder(record, command[1])
                elif(command[2] == 'T'): #NR3*
                    grade_teacher_finder(teachers, record, command[1])
                      
            else:
                grade_student_finder(record, command[1])
        elif((command[0] == 'B:') | (command[0] == 'Bus:')): 
            bus_student_finder(record, command[1])
        elif((command[0] == 'A:') | (command[0] == 'Average:')): 
            grade_level_average_finder(record, command[1]) 
        elif((command[0] == 'I') | (command[0] == 'Info')): 
            info_finder(record)
        elif((command[0] == 'E') | (command[0] == 'Enrollment')):  #NR4*
            enrollment_finder(record)

        else:
            print(error_MSG_INVALID_COMMAND)   
        return
    except FileNotFoundError:
        sys.exit("Exiting Program: students.txt not found")

def main():
    while True:
        user_input = input("Enter a command: ")
    #split the input into a list
        user_input_list = user_input.split()
        if((user_input_list[0] == 'Q') | (user_input_list[0] == 'Quit')):
            print("Exiting Program")
            break
        parse_command(user_input_list)
    return 

if __name__ == "__main__":
    main()

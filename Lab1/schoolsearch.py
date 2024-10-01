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


'''
import sys

#error messages
error_MSG_INVALID_COMMAND = "Invalid Command"
error_MSG_INVALID_COMMAND_FORMAT = "Invalid Command Format"
error_MSG_NO_RECORD = "No Record(s) Found"
error_MSG_INVALID_Grade = "Invalid Grade"
error_MSG_INVALID_Bus = "Invalid Bus Route"

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

def student_finder(record, last_name):
    count = 0
    for line in record:
        line = line.split(",")
        if(line[0] == last_name.upper()):
            print(line[0] + ", "  + line[1] + ", "  + line[2] + ", "  + line[3] + ", "  + line[6] + ", "  + line[7])
            count += 1
    if(count == 0):
        print(error_MSG_NO_RECORD)
    return

def teacher_finder(record, teacher_name):
    count = 0
    for line in record:
        line = line.split(",")
        if(line[6] == teacher_name.upper()):
            print(line[0] + ", "  + line[1])
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
    min_gpa = 0
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
        with open("students.txt") as f:
            record = f.readlines()

        if((command[0] == 'S:') | (command[0] == 'Student:')):
                if(len(command) == 3):
                    stundent_bus_finder(record, command[1])
                else:
                    student_finder(record, command[1])

        elif((command[0] == 'T:') | (command[0] == 'Teacher:')): 
            teacher_finder(record, command[1])
        elif((command[0] == 'G:') | (command[0] == 'Grade:')): 
            if(len(command) == 3):
                if((command[2] == 'H') | (command[2] == 'High')):
                    grade_max_student_finder(record, command[1])
                elif((command[2] == 'L') | (command[2] == 'Low')):
                    grade_min_student_finder(record, command[1])
                    
            else:
                grade_student_finder(record, command[1])
        elif((command[0] == 'B:') | (command[0] == 'Bus:')): 
            bus_student_finder(record, command[1])
        elif((command[0] == 'A:') | (command[0] == 'Average:')): 
            grade_level_average_finder(record, command[1]) 
        elif((command[0] == 'I') | (command[0] == 'Info')): 
            info_finder(record)
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

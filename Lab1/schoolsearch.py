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

def stundent_bus_finder(record, last_name):
    for line in record:
        line = line.split(",")
        if(line[0] == last_name):
            print(line[0], line[1], line[4])
    return


def student_finder(record, student_name):
    for line in record:
        line = line.split(",")
        if(line[0] == student_name):
            print(line[0], line[1], line[2], line[3], line[6], line[7])
    return

def teacher_finder(record, teacher_name):
    for line in record:
        line = line.split(",")
        if(line[6] == teacher_name):
            print(line[0], line[1])
    return

def grade_max_student_finder(record, grade):
    max_gpa = 0
    #first pass finds the max_gpa
    for line in record:
        line = line.split(",")
        if(line[2] == grade):
            max_gpa = max(max_gpa, float(line[5]))
    #second pass prints the student with max_gpa
    for line in record:
        line = line.split(",")
        if((line[2] == grade) & (float(line[5]) == max_gpa)):
            print(line[0], line[1], line[5], line[6], line[7], line[4])
    return

def grade_min_student_finder(record, grade):
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
            print(line[0], line[1], line[5], line[6], line[7], line[4])
    return

def grade_student_finder(record, grade):
    for line in record:
        line = line.split(",")
        if(line[2] == grade):
            print(line[0], line[1])
    return

def bus_student_finder(record, bus):
    for line in record:
        line = line.split(",")
        if(line[4] == bus):
            print(line[0], line[1], line[2], line[3])
    return

def grade_level_average_finder(record, grade):
    count = 0
    gpa_sum = 0
    for line in record:
        line = line.split(",")
        if(line[2] == grade):
            count += 1
            gpa_sum += float(line[5])
    average_gpa = gpa_sum/count
    print(grade + ":", round(average_gpa, 2))    
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
        print(grade + ":", grade_dict[grade])
    return

def parse_command(command):
    #open students.txt file and pass to all helper functions
    with open("students.txt") as f:
        record = f.readlines()

    if((command[0] == 'S') | (command[0] == 'Student:')):
            if(len(command) == 3):
                print("print the last name, first name and the bus route the student takes")
                stundent_bus_finder(record, command[1])
            else:
                print("print the last name, first name, grade and classroom assignment for each student found and the name of their teacher (last and first name)")
                student_finder(record, command[1])

    elif((command[0] == 'T') | (command[0] == 'Teacher:')): 
        print("print the last and the first name of the student")
        teacher_finder(record, command[1])
    elif((command[0] == 'G') | (command[0] == 'Grade:')): 
        if(len(command) == 3):
            if((command[2] == 'H') | (command[2] == 'High')):
                print("print info of student with highest GPA")
                grade_max_student_finder(record, command[1], command[2])
            elif((command[2] == 'L') | (command[2] == 'Low')):
                print("print info of student with lowest GPA")
                grade_min_student_finder(record, command[1], command[2])
                
        else:
            print("print the name (last and first) of the student")
            grade_student_finder(record, command[1])
    elif((command[0] == 'B') | (command[0] == 'Bus:')): 
        print("print the name of the student (last and first) and their grade and classroom")
        bus_student_finder(record, command[1])
    elif((command[0] == 'A') | (command[0] == 'Average:')): 
        print("print the grade level (the number provided in command) and the average GPA score rounded to two decimal places")
        grade_level_average_finder(record, command[1]) 
    elif((command[0] == 'I') | (command[0] == 'Info')): 
        print("print the number of students in each grade in the format <Grade>: <Number of Students> sorted in ascending order by grade") 
        info_finder(record)   
    return


def main():
    print("Hello, World!")
    while True:
        user_input = input("Enter a command: ")
    #split the input into a list
        user_input_list = user_input.split()
        if((user_input_list[0] == 'Q') | (user_input_list[0] == 'Quit')):
            break
        parse_command(user_input_list)
    print(user_input_list)
    #parser()

if __name__ == "__main__":
    main()



# def csv_parser():
#     with open("students.txt") as f:
#         record = f.readlines()
#         print(record)
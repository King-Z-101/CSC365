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


'''

def csv_parser():
    with open("students.txt") as f:
        record = f.readlines()
        print(record)

def parse_command(command):
    if((command[0] == 'S') | (command[0] == 'Student:')):
            if(len(command) == 3):
                print("print the last name, first name and the bus route the student takes")
            else:
                print("print the last name, first name, grade and classroom assignment for each student found and the name of their teacher (last and first name)")
    elif((command[0] == 'T') | (command[0] == 'Teacher:')): 
        print("print the last and the first name of the student")
    elif((command[0] == 'G') | (command[0] == 'Grade:')): 
        if(len(command) == 3):
            if((command[2] == 'H') | (command[2] == 'High')):
                print("print info of student with highest GPA")
            elif((command[2] == 'L') | (command[2] == 'Low')):
                print("print info of student with lowest GPA")
        else:
            print("print the name (last and first) of the student")
    elif((command[0] == 'B') | (command[0] == 'Bus:')): 
        print("print the name of the student (last and first) and their grade and classroom")
    elif((command[0] == 'A') | (command[0] == 'Average:')): 
        print("print the grade level (the number provided in command) and the average GPA score rounded to two decimal places") 
    elif((command[0] == 'I') | (command[0] == 'Info')): 
        print("print the number of students in each grade in the format <Grade>: <Number of Students> sorted in ascending order by grade")    
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
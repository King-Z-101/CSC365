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

def parser_command(command):
    return


def main():
    print("Hello, World!")
    while True:
        user_input = input("Enter a command: ")
    #split the input into a list
        user_input_list = user_input.split()
        parser_command(user_input_list)
    print(user_input_list)
    #parser()

if __name__ == "__main__":
    main()
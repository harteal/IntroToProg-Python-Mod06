# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
# Alex Harteloo, 2/15/24
# ------------------------------------------------------------------------------------------ #

import json


# Define the constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
'''
FILE_NAME: str = "Enrollments.json"


# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice: str = ''


class FileProcessor:
    """
    A collection of functions that process files in JSON format.

    Change log:
    Alex Harteloo, 2/15/24, created class.
    Alex Harteloo, 2/18/24, created read_data_to_file.
    Alex Harteloo, 2/19/24, created write_data_to_file.
    """


    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        # Takes student data and places into a file in JSON format.
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("Student information has been saved!")
        except Exception as e:
            IO.output_error_message(error=e)
        finally:
            if file.closed == False:
                file.close()


    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        # Reads a JSON file and extracts its data as 'student_data.'
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_message(message="Text file must exist before running this script!", error=e)
        except Exception as e:
            IO.output_error_message(error=e)
        finally:
            if file.closed == False:
                file.close()
        return student_data


class IO:
    """
    A collection of presentation layer functions that manage user input and output.

    Change log:
    Alex Harteloo, 2/15/24, created class.
    Alex Harteloo, 2/16/24, created output_menu().
    Alex Harteloo, 2/18/24, created input_menu_choice().
    Alex Harteloo, 2/18/24, created output_error_message().
    Alex Harteloo, 2/18/24, created input_student_data().
    Alex Harteloo, 2/18/24, created output_student_courses().

    """

    @staticmethod
    def output_menu(menu: str):
        # Presents menu to user.
        print('-' * 50)
        print(menu)
        print('-' * 50)


    @staticmethod
    def input_menu_choice():
        # Records the user menu choice.
        global menu_choice
        menu_choice = None
        try:
            menu_choice = input("What would you like to do: ")
            if menu_choice not in ("1", "2", "3", "4"):
                raise Exception("Did not recognize choice, please choose 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_message(error=e)



    @staticmethod
    def output_error_message(message: str = "There's a non-specific error!", error: Exception = None):
        # Presents error message to user and technical error message.
        print(message, end="\n\n")
        if error is not None:
            print("--Technical Error Message--")
            print(error, error.__doc__, error.__str__(), sep= " | ")


    @staticmethod
    def input_student_data(student_data: list):
        # Records user input of student information with error handling.
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_message(message="That value is not the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_message(message="There's a non-specific error!", error=e)

    @staticmethod
    def output_student_courses(student_data: list):
        # Presents student information to user when presented a list.
        for student in student_data:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

# Application layer
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while (True):
    IO.output_menu(MENU)
    IO.input_menu_choice()


    if menu_choice == "1":
        IO.input_student_data(students)
        continue

    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")

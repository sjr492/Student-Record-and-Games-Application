import random

# Global dictionary for letter grades and GPA values
letter_grade_to_gpa_dictionary = {'A+': 4.0, 'A': 4.0, 'A-': 3.7,
                                  'B+': 3.3, 'B': 3.0, 'B-': 2.7,
                                  'C+': 2.3, 'C': 2.0, 'C-': 1.7,
                                  'D+': 1.3, 'D': 1.0
                                  }


class Course:
    # Course class to store course information
    def __init__(self, name, credit_hours, letter_grade):
        self.name = name
        self.credit_hours = credit_hours
        self.letter_grade = letter_grade

    def __str__(self):
        # Get the GPA value for this course's letter grade
        course_gpa = letter_grade_to_gpa_dictionary.get(self.letter_grade, 0.0)
        result = (f"{self.name}, {self.credit_hours} credits, "
                  f"Grade: {self.letter_grade}, GPA: {course_gpa:.1f}")
        return result


class Student:
    # Student class to store student information and courses
    def __init__(self, full_name, email, major, id):
        self.full_name = full_name
        self.email = email
        self.major = major
        self.id = id
        self.courses = []

    def add_course(self, course):
        # Add a course to the student's list
        self.courses.append(course)

    def calculate_final_gpa(self):
        # Calculate overall GPA using quality points
        total_quality_points = 0.0
        total_credit_hours = 0

        # Loop through each course to calculate quality points
        for course in self.courses:
            # Get the GPA for this course's letter grade
            course_gpa = letter_grade_to_gpa_dictionary.get(course.letter_grade, 0.0)

            # Calculate quality points: GPA * credit hours
            quality_points = course_gpa * course.credit_hours

            # Add to totals
            total_quality_points += quality_points
            total_credit_hours += course.credit_hours

        # Calculate overall GPA
        if total_credit_hours > 0:
            overall_gpa = total_quality_points / total_credit_hours
        else:
            overall_gpa = 0.0

        return overall_gpa

    def print_transcript(self):
        # Print student transcript to screen and save to file
        # Create transcript header
        transcript = "=" * 60 + "\n"
        transcript += "STUDENT TRANSCRIPT\n"
        transcript += "=" * 60 + "\n"
        transcript += f"Name: {self.full_name}\n"
        transcript += f"Email: {self.email}\n"
        transcript += f"Major: {self.major}\n"
        transcript += f"Student ID: {self.id}\n"
        transcript += "=" * 60 + "\n"
        transcript += "COURSES:\n"
        transcript += "-" * 60 + "\n"

        # Add each course to the transcript
        for course in self.courses:
            transcript += str(course) + "\n"

        # Calculate and add final GPA
        final_gpa = self.calculate_final_gpa()
        transcript += "-" * 60 + "\n"
        transcript += f"FINAL GPA: {final_gpa:.2f}\n"
        transcript += "=" * 60 + "\n"

        # Print transcript to screen
        print(transcript)

        # Write transcript to file
        filename = f"{self.full_name}.txt"
        with open(filename, 'w') as file:
            file.write(transcript)
        print(f"Transcript saved to {filename}")


def student_record():
    # Function to create student record and transcript
    print("\n--- Student Record ---")

    # Get student information
    student_info = input("Enter student info (Full Name, Email, Major, Student ID): ")

    # Parse the student information
    info_parts = [part.strip() for part in student_info.split(',')]

    # Validate that we have 4 parts
    if len(info_parts) != 4:
        print("Error: Please enter all 4 pieces of information separated by commas.")
        return

    # Create Student object
    full_name, email, major, student_id = info_parts
    my_student = Student(full_name, email, major, student_id)

    # Get number of courses with validation
    number_of_courses = 0
    while number_of_courses < 2 or number_of_courses > 6:
        try:
            number_of_courses = int(input("How many courses (2-6)? "))
            if number_of_courses < 2 or number_of_courses > 6:
                print("Error: Please enter a number between 2 and 6.")
        except ValueError:
            print("Error: Please enter a valid number.")

    # Get course information for each course
    for i in range(number_of_courses):
        print(f"\nCourse {i + 1}:")
        course_info = input("Enter course info (Course Name, Credit Hours, Letter Grade): ")

        # Parse course information
        course_parts = [part.strip() for part in course_info.split(',')]

        # Validate that we have 3 parts
        if len(course_parts) != 3:
            print("Error: Please enter all 3 pieces of information separated by commas.")
            continue

        # Extract course details
        course_name = course_parts[0]
        try:
            credit_hours = int(course_parts[1])
        except ValueError:
            print("Error: Credit hours must be a number.")
            continue

        letter_grade = course_parts[2].upper()

        # Validate letter grade
        if letter_grade not in letter_grade_to_gpa_dictionary:
            print(f"Error: Invalid letter grade '{letter_grade}'.")
            continue

        # Create Course object and add to student
        course = Course(course_name, credit_hours, letter_grade)
        my_student.add_course(course)

    # Print the student's transcript
    print()
    my_student.print_transcript()


def lottery_number_generator():
    # This function creates lottery numbers
    # Create a list for the first five numbers
    lottery_numbers_list = []

    # Add five unique numbers between one and sixty nine
    while len(lottery_numbers_list) < 5:
        number = random.randint(1, 69)
        if number not in lottery_numbers_list:
            lottery_numbers_list.append(number)

    # Generate Power number between 1 and 26
    power_number = random.randint(1, 26)

    # Sort the first five numbers and print all six without brackets
    lottery_numbers_list.sort()
    print("Your lucky numbers are:", *lottery_numbers_list, end=". ")
    print(f"Your Power Number is: {power_number}")
    print("Here is your result:", *lottery_numbers_list, power_number)
    print("")


def pig_latin():
    # This function converts a sentence to Pig Latin
    # Get the original sentence from the user
    original_sentence = input("Enter sentence to be converted into Pig Latin: ").upper().split()

    # Convert each word to Pig Latin
    print("")
    for current_word in original_sentence:
        current_word = current_word[1:] + current_word[0] + "AY"
        print(current_word, end=" ")
    print("\n")


def rock_paper_scissors_game():
    # This function plays Rock Paper Scissors
    # List of valid choices
    choices_list = ["rock", "paper", "scissors"]

    game_result = "tie"

    # Repeat the game when there is a tie
    while game_result == "tie":
        # Create the computer choice with a random number
        random_number = random.randint(1, 3)
        computer_choice = choices_list[random_number - 1]

        # Get a valid player choice
        player_choice = input("Enter a choice rock, paper, or scissors ----> ").lower()
        while player_choice not in choices_list:
            player_choice = input("Invalid input  Enter rock, paper, or scissors ----> ").lower()

        # Decide winner with the game rules
        if (
                (player_choice == "rock" and computer_choice == "scissors")
                or (player_choice == "paper" and computer_choice == "rock")
                or (player_choice == "scissors" and computer_choice == "paper")
        ):
            game_result = "player"
        elif (
                (computer_choice == "rock" and player_choice == "scissors")
                or (computer_choice == "paper" and player_choice == "rock")
                or (computer_choice == "scissors" and player_choice == "paper")
        ):
            game_result = "computer"
        else:
            game_result = "tie"

        # Show choices and result
        print("")
        print("-" * 30)
        if game_result == "player":
            print("Player wins")
        elif game_result == "computer":
            print("Computer wins")
        else:
            print("It is a tie. Play again")
        print(f"Player choice: {player_choice}")
        print(f"Computer choice: {computer_choice}")
        print("-" * 30)
        print("")


def main():
    # Print project title and line
    print("CSC 115 - FALL 2025 FINAL PROJECT")
    print("-" * 130)

    # Print menu instructions
    menu = ("Welcome to the CSC115 Final Project Program."
            "\nEnter 1 to Student Record"
            "\nEnter 2 for Lottery Number Generator"
            "\nEnter 3 for Pig Latin"
            "\nEnter 4 for Rock, Paper, Scissors")

    # Valid menu options
    valid_option_list = ["1", "2", "3", "4", "9"]

    # Show menu and get user's choice
    print(menu)
    print("")
    input_choice = input("Enter your choice 1, 2, 3, 4, or 9 to exit: ")
    while input_choice not in valid_option_list:
        input_choice = input(f"Invalid input. Re-enter your choice 1, 2, 3, 4, or 9 to exit: ")

    # Main loop to process user choices
    while input_choice != "9":
        print("")
        if input_choice == "1":
            student_record()
        elif input_choice == "2":
            lottery_number_generator()
        elif input_choice == "3":
            pig_latin()
        elif input_choice == "4":
            rock_paper_scissors_game()

        # Show menu again
        print(menu)
        input_choice = input("\nEnter your choice 1, 2, 3, 4, or 9 to exit: ")
        while input_choice not in valid_option_list:
            input_choice = input(f"Invalid input. Re-enter your choice 1, 2, 3, 4, or 9 to exit: ")

    # Exit message
    print("User select option 9. Exit program")


# Call the main function
if __name__ == '__main__':
    main()

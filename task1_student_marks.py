# Task 1: Create a Dictionary of Student Marks

def get_student_marks(student_dict, name):
    return student_dict.get(name, "Student not found.")

# Main program
if __name__ == "__main__":
    # Predefined dictionary of student marks
    student_marks = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "Diana": 90,
        "Eve": 88
    }

    # Input from the user
    student_name = input("Enter the student's name: ")

    # Retrieve and display the marks
    marks = get_student_marks(student_marks, student_name)
    if isinstance(marks, int):
        print(f"{student_name}'s marks: {marks}")
    else:
        print(marks)
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}  # {assignment_name: grade}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added grade {grade} for '{assignment_name}' to student {self.name}.")

    def display_grades(self):
        print(f"\nGrades for {self.name}:")
        if not self.assignments:
            print("  No assignments yet.")
        else:
            for assignment, grade in self.assignments.items():
                print(f"  {assignment}: {grade}")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []  # list of Student objects

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' added to the course '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = self.find_student_by_id(student_id)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"No student found with ID {student_id}.")

    def display_all_students(self):
        if not self.students:
            print("No students enrolled yet.")
            return
        print(f"\nStudents in {self.course_name}:")
        for student in self.students:
            print(f"- {student.name} (ID: {student.student_id})")
            student.display_grades()

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None


# Interactive system
def run_instructor_interface():
    instructor_name = input("Enter instructor name: ")
    course_name = input("Enter course name: ")
    instructor = Instructor(instructor_name, course_name)

    while True:
        print("\n--- Instructor Menu ---")
        print("1. Add Student")
        print("2. Assign Grade")
        print("3. Display All Students and Grades")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == "2":
            student_id = input("Enter student ID to assign grade: ")
            assignment = input("Enter assignment name: ")
            try:
                grade = float(input("Enter grade (0-100): "))
                instructor.assign_grade(student_id, assignment, grade)
            except ValueError:
                print("Invalid grade. Please enter a number.")

        elif choice == "3":
            instructor.display_all_students()

        elif choice == "4":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


# Run the program
run_instructor_interface()

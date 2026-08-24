from file_handler import load_students

def generate_report():

    students = load_students()

    student_id = input("Enter Student ID : ")

    for student in students:

        if student["student_id"] == student_id:

            print("\n")
            print("="*60)
            print("        STUDENT REPORT CARD")
            print("="*60)

            print(f"ID         : {student['student_id']}")
            print(f"Name       : {student['name']}")
            print(f"Branch     : {student['branch']}")
            print(f"Semester   : {student['semester']}")
            print(f"Marks      : {student['marks']}")
            print(f"CGPA       : {student['cgpa']}")
            print(f"Attendance : {student['attendance']}%")
            print(f"Supplies   : {student['supplies']}")

            print("="*60)

            return

    print("Student Not Found")

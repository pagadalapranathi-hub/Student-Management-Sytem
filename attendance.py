from file_handler import load_students, save_students

def update_attendance():

    students = load_students()

    sid = input("Student ID : ")

    for student in students:

        if student["student_id"] == sid:

            attendance = input("Attendance (%) : ")

            student["attendance"] = attendance

            save_students(students)

            print("Attendance Updated Successfully")

            return

    print("Student Not Found")

from file_handler import load_students, save_students

def update_cgpa():

    students = load_students()

    sid = input("Student ID : ")

    for student in students:

        if student["student_id"] == sid:

            cgpa = input("Enter CGPA : ")

            student["cgpa"] = cgpa

            save_students(students)

            print("CGPA Updated Successfully")

            return

    print("Student Not Found")

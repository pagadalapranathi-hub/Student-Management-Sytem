from datetime import datetime
from file_handler import load_students, save_students
from validation import (
    validate_student_id,
    validate_email,
    validate_password,
    validate_mobile,
    validate_age,
    validate_year
)


# -----------------------------
# Register Student
# -----------------------------
def register_student():

    students = load_students()

    student_id = input("Enter Student ID : ")

    if not validate_student_id(student_id):
        print("Invalid Student ID.")
        return

    for student in students:
        if student["student_id"] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter Name : ")

    email = input("Enter Email : ")

    if not validate_email(email):
        print("Invalid Email.")
        return

    password = input("Enter Password : ")

    if not validate_password(password):
        print("Password must be at least 6 characters.")
        return

    mobile = input("Enter Mobile Number : ")

    if not validate_mobile(mobile):
        print("Invalid Mobile Number.")
        return

    gender = input("Enter Gender (Male/Female) : ")

    age = input("Enter Age : ")

    if not validate_age(age):
        print("Invalid Age.")
        return

    branch = input("Enter Branch : ")

    semester = input("Enter Semester : ")

    year = input("Enter Year (1-4) : ")

    if not validate_year(year):
        print("Invalid Year.")
        return

    subjects = input("Enter Subjects (comma separated) : ").split(",")

    marks = input("Enter Marks : ")

    attendance = input("Enter Attendance (%) : ")

    cgpa = input("Enter CGPA : ")

    supplies = input("Enter Number of Supplies : ")

    join_date = datetime.now().strftime("%d-%m-%Y")

    pass_out_year = str(2026 + (4 - int(year)))

    status = "Active"

    student = {
        "student_id": student_id,
        "name": name,
        "email": email,
        "password": password,
        "mobile": mobile,
        "gender": gender,
        "age": age,
        "branch": branch,
        "semester": semester,
        "year": year,
        "subjects": subjects,
        "marks": marks,
        "attendance": attendance,
        "cgpa": cgpa,
        "join_date": join_date,
        "pass_out_year": pass_out_year,
        "supplies": supplies,
        "status": status
    }

    students.append(student)

    save_students(students)

    print("\nStudent Registered Successfully.")

# -----------------------------
# View Students
# -----------------------------
def view_students():

    students = load_students()

    if len(students) == 0:
        print("\nNo Students Found.")
        return

    print("\n" + "=" * 70)
    print("                STUDENT LIST")
    print("=" * 70)

    for student in students:

        print(f"\nStudent ID   : {student['student_id']}")
        print(f"Name         : {student['name']}")
        print(f"Email        : {student['email']}")
        print(f"Mobile       : {student['mobile']}")
        print(f"Gender       : {student['gender']}")
        print(f"Age          : {student['age']}")
        print(f"Branch       : {student['branch']}")
        print(f"Semester     : {student['semester']}")
        print(f"Year         : {student['year']}")
        print(f"Subjects     : {', '.join(student['subjects'])}")
        print(f"Marks        : {student['marks']}")
        print(f"Attendance   : {student.get('attendance', 'Not Available')}")
        print(f"CGPA         : {student.get('cgpa', 'Not Available')}")
        print(f"Join Date    : {student['join_date']}")
        print(f"Pass Out     : {student['pass_out_year']}")
        print(f"Supplies     : {student['supplies']}")
        print(f"Status       : {student['status']}")
        print("-" * 70)


# -----------------------------
# Search Student
# -----------------------------
def search_student():

    students = load_students()

    student_id = input("\nEnter Student ID : ")

    for student in students:

        if student["student_id"] == student_id:

            print("\nStudent Found")
            print("=" * 40)
            print(f"Student ID : {student['student_id']}")
            print(f"Name       : {student['name']}")
            print(f"Email      : {student['email']}")
            print(f"Mobile     : {student['mobile']}")
            print(f"Branch     : {student['branch']}")
            print(f"Semester   : {student['semester']}")
            print(f"Year       : {student['year']}")
            print(f"Marks      : {student['marks']}")
            print(f"Attendance   : {student.get('attendance', 'Not Available')}")
            print(f"CGPA         : {student.get('cgpa', 'Not Available')}")
            
            return

    print("\nStudent Not Found.")


# -----------------------------
# Update Student
# -----------------------------
def update_student():

    students = load_students()

    student_id = input("\nEnter Student ID to Update : ")

    for student in students:

        if student["student_id"] == student_id:

            print("\nStudent Found")
            print("Press Enter to keep old value.\n")

            name = input(f"Enter New Name ({student['name']}): ")

            email = input(f"Enter New Email ({student['email']}): ")

            branch = input(f"Enter New Branch ({student['branch']}): ")

            year = input(f"Enter New Year ({student['year']}): ")

            if name != "":
                student["name"] = name

            if email != "":
                if validate_email(email):
                    student["email"] = email
                else:
                    print("Invalid Email")
                    return

            if branch != "":
                student["branch"] = branch

            if year != "":
                student["year"] = year

            save_students(students)

            print("\nStudent Updated Successfully.")

            return

    print("\nStudent Not Found.")
# -----------------------------
# Delete Student
# -----------------------------
def delete_student():

    students = load_students()

    student_id = input("\nEnter Student ID to Delete : ")

    for student in students:

        if student["student_id"] == student_id:

            print("\nStudent Found")
            print("-" * 40)
            print(f"Student ID : {student['student_id']}")
            print(f"Name       : {student['name']}")
            print(f"Email      : {student['email']}")
            print(f"Branch     : {student['branch']}")
            print(f"Year       : {student['year']}")

            confirm = input("\nAre you sure? (yes/no) : ").lower()

            if confirm == "yes":

                students.remove(student)

                save_students(students)

                print("\nStudent Deleted Successfully.")

            else:

                print("\nDeletion Cancelled.")

            return

    print("\nStudent Not Found.")


# -----------------------------
# Dashboard
# -----------------------------
def dashboard():

    students = load_students()

    if len(students) == 0:
        print("\nNo Student Records Found.")
        return

    total_students = len(students)

    male = 0
    female = 0
    active = 0
    inactive = 0
    supplies = 0

    branch_count = {}

    topper = students[0]

    for student in students:

        if student["gender"].lower() == "male":
            male += 1

        elif student["gender"].lower() == "female":
            female += 1

        if student["status"] == "Active":
            active += 1
        else:
            inactive += 1

        if int(student["supplies"]) > 0:
            supplies += 1

        branch = student["branch"]

        if branch in branch_count:
            branch_count[branch] += 1
        else:
            branch_count[branch] = 1

        if int(student["marks"]) > int(topper["marks"]):
            topper = student

    print("\n" + "=" * 60)
    print("           STUDENT DASHBOARD")
    print("=" * 60)

    print(f"Total Students       : {total_students}")
    print(f"Male Students        : {male}")
    print(f"Female Students      : {female}")
    print(f"Active Students      : {active}")
    print(f"Inactive Students    : {inactive}")
    print(f"Students with Supply : {supplies}")

    print("\nBranch Wise Count")
    print("-" * 30)

    for branch, count in branch_count.items():
        print(f"{branch} : {count}")

    print("\nTopper Student")
    print("-" * 30)
    print(f"Name   : {topper['name']}")
    print(f"Marks  : {topper['marks']}")
    print(f"CGPA   : {topper['cgpa']}")
    print(f"Branch : {topper['branch']}")

# -----------------------------
# Search Student by Name
# -----------------------------
def search_by_name():

    students = load_students()

    name = input("\nEnter Student Name : ").lower()

    found = False

    for student in students:

        if student["name"].lower() == name:

            print("\nStudent Found")
            print("-" * 40)
            print(f"Student ID : {student['student_id']}")
            print(f"Name       : {student['name']}")
            print(f"Email      : {student['email']}")
            print(f"Branch     : {student['branch']}")
            print(f"Semester   : {student['semester']}")
            print(f"Marks      : {student['marks']}")
            print(f"CGPA       : {student.get('cgpa', 'Not Available')}")
            student.get("cgpa", "Not Available")
            student.get("mobile", "Not Available")
            found = True

    if not found:
        print("\nStudent Not Found.")




# -----------------------------
# Search Student by Branch
# -----------------------------
def search_by_branch():

    students = load_students()

    branch = input("\nEnter Branch : ").upper()

    found = False

    for student in students:

        if student["branch"].upper() == branch:

            print("-" * 40)
            print(f"Student ID : {student['student_id']}")
            print(f"Name       : {student['name']}")
            print(f"Branch     : {student['branch']}")
            print(f"Semester   : {student['semester']}")
            print(f"Marks      : {student['marks']}")
            found = True

    if not found:
        print("\nNo Student Found.")


# -----------------------------
# Search Student by Semester
# -----------------------------
def search_by_semester():

    students = load_students()

    semester = input("\nEnter Semester : ")

    found = False

    for student in students:

        if student["semester"] == semester:

            print("-" * 40)
            print(f"Student ID : {student['student_id']}")
            print(f"Name       : {student['name']}")
            print(f"Semester   : {student['semester']}")
            print(f"Branch     : {student['branch']}")
            found = True

    if not found:
        print("\nNo Student Found.")


# -----------------------------
# Sort Students by Name
# -----------------------------
def sort_by_name():

    students = load_students()

    students.sort(key=lambda x: x["name"].lower())

    print("\nStudents Sorted by Name")
    print("-" * 40)

    for student in students:

        print(f"{student['student_id']}  -  {student['name']}")


# -----------------------------
# Sort Students by Marks
# -----------------------------
def sort_by_marks():

    students = load_students()

    students.sort(key=lambda x: int(x["marks"]), reverse=True)

    print("\nStudents Sorted by Marks")
    print("-" * 40)

    for student in students:

        print(f"{student['name']}  -  {student['marks']} Marks")

def student_report():

    students = load_students()

    student_id = input("\nEnter Student ID : ")

    for student in students:

        if student["student_id"] == student_id:

            marks = int(student["marks"])

            if marks >= 90:
                grade = "A+"
                result = "PASS"

            elif marks >= 80:
                grade = "A"
                result = "PASS"

            elif marks >= 70:
                grade = "B+"
                result = "PASS"

            elif marks >= 60:
                grade = "B"
                result = "PASS"

            elif marks >= 50:
                grade = "C"
                result = "PASS"

            else:
                grade = "FAIL"
                result = "FAIL"

            print("\n" + "=" * 50)
            print("          STUDENT REPORT CARD")
            print("=" * 50)

            print(f"Student ID : {student['student_id']}")
            print(f"Name       : {student['name']}")
            print(f"Branch     : {student['branch']}")
            print(f"Semester   : {student['semester']}")
            print(f"Subjects   : {', '.join(student['subjects'])}")
            print(f"Marks      : {student['marks']}")
            print(f"Attendance : {student.get('attendance', 'N/A')}")
            print(f"CGPA       : {student.get('cgpa', 'N/A')}")
            print(f"Result     : {result}")
            print(f"Grade      : {grade}")

            print("=" * 50)

            return

    print("\nStudent Not Found.")        

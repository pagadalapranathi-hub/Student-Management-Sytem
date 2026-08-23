from report import generate_report
from attendance import update_attendance
from cgpa import update_cgpa
from analytics import analytics
from export import export_csv
from student import student_report

from menu import display_menu

from login import admin_login,change_admin_password

from student import (
    register_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    dashboard,
    search_by_name,
    search_by_branch,
    search_by_semester,
    sort_by_name,
    sort_by_marks,
    student_report,
)

from export import export_csv


print("=" * 50)
print("      STUDENT MANAGEMENT SYSTEM")
print("=" * 50)

print("\nADMIN LOGIN\n")

if not admin_login():
    print("Access Denied!")
    exit()


while True:

    display_menu()

    choice = input("\nEnter Your Choice : ")

    if choice == "1":
        register_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        dashboard()

    elif choice == "7":
        generate_report()

    elif choice == "8":
        update_attendance()

    elif choice == "9":
        update_cgpa()

    elif choice == "10":
        analytics()

    elif choice == "11":
        export_csv()

    elif choice == "12":
        print("Thank you!")

    elif choice == "15":
         print("\nThank You")
         print("Project Closed Successfully.")
         break

    else:
        print("\nInvalid Choice! Please Try Again.")

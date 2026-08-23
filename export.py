import csv
from file_handler import load_students


def export_csv():

    students = load_students()

    if not students:
        print("No student records found.")
        return

    fieldnames = set()

    for student in students:
          fieldnames.update(student.keys())

    fieldnames = list(fieldnames)

    with open("students.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for student in students:

            student_copy = student.copy()

            if "subjects" in student_copy and isinstance(student_copy["subjects"], list):
                student_copy["subjects"] = ", ".join(student_copy["subjects"])

            writer.writerow(student_copy)

    print("\nStudents exported successfully!")

from file_handler import load_students

def analytics():

    students = load_students()

    total = len(students)

    if total == 0:
        print("No Records")
        return

    total_marks = 0

    for student in students:

        total_marks += int(student["marks"])

    average = total_marks / total

    print("\n")
    print("="*40)
    print("PROJECT ANALYTICS")
    print("="*40)
    print(f"Total Students : {total}")
    print(f"Average Marks  : {average:.2f}")

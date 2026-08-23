import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import json

from file_handler import load_students, save_students

from validation import (
    validate_student_id,
    validate_email,
    validate_password,
    validate_mobile,
    validate_age,
    validate_year
)


# =========================================================
# MAIN WINDOW
# =========================================================

window = None


# =========================================================
# FUNCTIONS
# =========================================================
def admin_login_gui():

    login_window = tk.Tk()

    login_window.title("Admin Login")

    login_window.geometry("400x300")

    login_window.resizable(False, False)

    # -----------------------------------------------------
    # Title
    # -----------------------------------------------------

    tk.Label(
        login_window,
        text="ADMIN LOGIN",
        font=("Arial", 24, "bold")
    ).pack(pady=30)

    # -----------------------------------------------------
    # Username
    # -----------------------------------------------------

    tk.Label(
        login_window,
        text="Username"
    ).pack()

    username_entry = tk.Entry(
        login_window,
        width=30
    )

    username_entry.pack(pady=8)

    # -----------------------------------------------------
    # Password
    # -----------------------------------------------------

    tk.Label(
        login_window,
        text="Password"
    ).pack()

    password_entry = tk.Entry(
        login_window,
        width=30,
        show="*"
    )

    password_entry.pack(pady=8)

    # -----------------------------------------------------
    # Login Function
    # -----------------------------------------------------

    def login():

        username = username_entry.get().strip()

        password = password_entry.get().strip()

        if not username or not password:

            messagebox.showwarning(
                "Missing Information",
                "Please enter username and password."
            )

            return

        try:

            with open(
                "admin.json",
                "r",
                encoding="utf-8"
            ) as file:

                admin = json.load(file)

        except FileNotFoundError:

            messagebox.showerror(
                "Error",
                "admin.json file not found."
            )

            return

        except json.JSONDecodeError:

            messagebox.showerror(
                "Error",
                "admin.json contains invalid data."
            )

            return

        if (
            username == admin.get("username")
            and
            password == admin.get("password")
        ):

            messagebox.showinfo(
                "Login Successful",
                "Welcome Admin!"
            )

            login_window.destroy()

            open_main_window()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )

            password_entry.delete(
                0,
                tk.END
            )

    # -----------------------------------------------------
    # Login Button
    # -----------------------------------------------------

    tk.Button(
        login_window,
        text="Login",
        width=20,
        command=login
    ).pack(pady=20)

    login_window.mainloop()

def export_csv_gui():

    students = load_students()

    if not students:

        messagebox.showinfo(
            "Export CSV",
            "No student records available."
        )

        return

    file_path = filedialog.asksaveasfilename(
        title="Save Student Data",
        defaultextension=".csv",
        filetypes=[
            ("CSV Files", "*.csv"),
            ("All Files", "*.*")
        ],
        initialfile="students.csv"
    )

    if not file_path:
        return

    try:

        # Collect all possible fields
        fieldnames = []

        for student in students:

            for key in student.keys():

                if key not in fieldnames:
                    fieldnames.append(key)

        with open(
            file_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for student in students:

                row = student.copy()

                # Convert list of subjects to text
                if isinstance(row.get("subjects"), list):

                    row["subjects"] = ", ".join(
                        row["subjects"]
                    )

                writer.writerow(row)

        messagebox.showinfo(
            "Export Successful",
            "Student data exported successfully!"
        )

    except Exception as error:

        messagebox.showerror(
            "Export Error",
            f"Unable to export data.\n\n{error}"
        )

def register_student_gui():

    register_window = tk.Toplevel(window)

    register_window.title("Register Student")

    register_window.geometry("600x700")

    register_window.resizable(False, False)

    # -----------------------------------------------------
    # Title
    # -----------------------------------------------------

    tk.Label(
        register_window,
        text="REGISTER STUDENT",
        font=("Arial", 20, "bold")
    ).pack(pady=15)

    # -----------------------------------------------------
    # Form Frame
    # -----------------------------------------------------

    form_frame = tk.Frame(register_window)

    form_frame.pack(pady=5)

    # -----------------------------------------------------
    # Variables
    # -----------------------------------------------------

    student_id_var = tk.StringVar()
    name_var = tk.StringVar()
    email_var = tk.StringVar()
    password_var = tk.StringVar()
    mobile_var = tk.StringVar()
    gender_var = tk.StringVar()
    age_var = tk.StringVar()
    branch_var = tk.StringVar()
    semester_var = tk.StringVar()
    year_var = tk.StringVar()
    subjects_var = tk.StringVar()
    marks_var = tk.StringVar()
    cgpa_var = tk.StringVar()
    attendance_var = tk.StringVar()
    supplies_var = tk.StringVar()

    # -----------------------------------------------------
    # Form Fields
    # -----------------------------------------------------

    fields = [
        ("Student ID", student_id_var),
        ("Name", name_var),
        ("Email", email_var),
        ("Password", password_var),
        ("Mobile", mobile_var),
        ("Age", age_var),
        ("Branch", branch_var),
        ("Semester", semester_var),
        ("Year", year_var),
        ("Subjects", subjects_var),
        ("Marks", marks_var),
        ("CGPA", cgpa_var),
        ("Attendance", attendance_var),
        ("Supplies", supplies_var)
    ]

    entries = {}

    for row, (label_text, variable) in enumerate(fields):

        tk.Label(
            form_frame,
            text=label_text + ":",
            width=15,
            anchor="w"
        ).grid(
            row=row,
            column=0,
            padx=10,
            pady=6
        )

        if label_text == "Password":

            entry = tk.Entry(
                form_frame,
                textvariable=variable,
                width=35,
                show="*"
            )

        else:

            entry = tk.Entry(
                form_frame,
                textvariable=variable,
                width=35
            )

        entry.grid(
            row=row,
            column=1,
            padx=10,
            pady=6
        )

        entries[label_text] = entry

    # -----------------------------------------------------
    # Gender
    # -----------------------------------------------------

    tk.Label(
        form_frame,
        text="Gender:",
        width=15,
        anchor="w"
    ).grid(
        row=len(fields),
        column=0,
        padx=10,
        pady=6
    )

    gender_box = ttk.Combobox(
        form_frame,
        textvariable=gender_var,
        values=["Male", "Female", "Other"],
        state="readonly",
        width=32
    )

    gender_box.grid(
        row=len(fields),
        column=1,
        padx=10,
        pady=6
    )

    # -----------------------------------------------------
    # Register Function
    # -----------------------------------------------------

    def register():

        student_id = student_id_var.get().strip()
        name = name_var.get().strip()
        email = email_var.get().strip()
        password = password_var.get().strip()
        mobile = mobile_var.get().strip()
        gender = gender_var.get().strip()
        age = age_var.get().strip()
        branch = branch_var.get().strip()
        semester = semester_var.get().strip()
        year = year_var.get().strip()
        subjects = subjects_var.get().strip()
        marks = marks_var.get().strip()
        cgpa = cgpa_var.get().strip()
        attendance = attendance_var.get().strip()
        supplies = supplies_var.get().strip()

        # -------------------------------------------------
        # Empty Field Check
        # -------------------------------------------------

        if not all([
            student_id,
            name,
            email,
            password,
            mobile,
            gender,
            age,
            branch,
            semester,
            year,
            subjects,
            marks,
            cgpa,
            attendance,
            supplies
        ]):

            messagebox.showwarning(
                "Missing Information",
                "Please fill all fields."
            )

            return

        # -------------------------------------------------
        # Student ID Validation
        # -------------------------------------------------

        if not validate_student_id(student_id):

            messagebox.showerror(
                "Invalid Student ID",
                "Student ID must contain numbers only."
            )

            return

        # -------------------------------------------------
        # Duplicate Student ID
        # -------------------------------------------------

        students = load_students()

        for student in students:

            if student.get("student_id") == student_id:

                messagebox.showerror(
                    "Duplicate ID",
                    "Student ID already exists."
                )

                return

        # -------------------------------------------------
        # Email Validation
        # -------------------------------------------------

        if not validate_email(email):

            messagebox.showerror(
                "Invalid Email",
                "Please enter a valid Gmail address."
            )

            return

        # -------------------------------------------------
        # Password Validation
        # -------------------------------------------------

        if not validate_password(password):

            messagebox.showerror(
                "Invalid Password",
                "Password must contain at least 6 characters."
            )

            return

        # -------------------------------------------------
        # Mobile Validation
        # -------------------------------------------------

        if not validate_mobile(mobile):

            messagebox.showerror(
                "Invalid Mobile",
                "Mobile number must contain 10 digits."
            )

            return

        # -------------------------------------------------
        # Age Validation
        # -------------------------------------------------

        if not validate_age(age):

            messagebox.showerror(
                "Invalid Age",
                "Age must be between 16 and 35."
            )

            return

        # -------------------------------------------------
        # Year Validation
        # -------------------------------------------------

        if not validate_year(year):

            messagebox.showerror(
                "Invalid Year",
                "Year must be 1, 2, 3, or 4."
            )

            return

        # -------------------------------------------------
        # Number Validation
        # -------------------------------------------------

        try:

            float(marks)
            float(cgpa)
            float(attendance)
            int(supplies)

        except ValueError:

            messagebox.showerror(
                "Invalid Data",
                "Marks, CGPA, Attendance and Supplies must be numbers."
            )

            return

        # -------------------------------------------------
        # Create Student
        # -------------------------------------------------

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

            "subjects": [
                subject.strip()
                for subject in subjects.split(",")
            ],

            "marks": marks,

            "cgpa": cgpa,

            "attendance": attendance,

            "join_date": "",

            "pass_out_year": "",

            "supplies": supplies,

            "status": "Active"
        }

        # -------------------------------------------------
        # Save Student
        # -------------------------------------------------

        students.append(student)

        save_students(students)

        messagebox.showinfo(
            "Success",
            "Student Registered Successfully!"
        )

        # Clear form

        for variable in [
            student_id_var,
            name_var,
            email_var,
            password_var,
            mobile_var,
            gender_var,
            age_var,
            branch_var,
            semester_var,
            year_var,
            subjects_var,
            marks_var,
            cgpa_var,
            attendance_var,
            supplies_var
        ]:

            variable.set("")

        # Refresh main table

        view_students()

    # -----------------------------------------------------
    # Register Button
    # -----------------------------------------------------

    tk.Button(
        register_window,
        text="Register Student",
        width=20,
        command=register
    ).pack(pady=15)

    # -----------------------------------------------------
    # Close Button
    # -----------------------------------------------------

    tk.Button(
        register_window,
        text="Close",
        width=20,
        command=register_window.destroy
    ).pack()

def view_students():

    students = load_students()

    # Remove old data from table
    for item in table.get_children():
        table.delete(item)

    if not students:
        messagebox.showinfo(
            "Students",
            "No student records found."
        )
        return

    for student in students:

        table.insert(
            "",
            "end",
            values=(
                student.get("student_id", ""),
                student.get("name", ""),
                student.get("email", ""),
                student.get("branch", ""),
                student.get("semester", ""),
                student.get("year", ""),
                student.get("marks", ""),
                student.get("cgpa", ""),
                student.get("attendance", ""),
                student.get("status", "")
            )
        )


def search_student():

    search_window = tk.Toplevel(window)

    search_window.title("Search Student")
    search_window.geometry("400x250")

    tk.Label(
        search_window,
        text="Search Student",
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    tk.Label(
        search_window,
        text="Enter Student ID:"
    ).pack()

    student_id_entry = tk.Entry(
        search_window,
        width=30
    )

    student_id_entry.pack(pady=10)

    def search():

        student_id = student_id_entry.get().strip()

        if not student_id:
            messagebox.showwarning(
                "Warning",
                "Please enter Student ID."
            )
            return

        students = load_students()

        for student in students:

            if student.get("student_id") == student_id:

                details = (
                    f"Student ID : {student.get('student_id', '')}\n"
                    f"Name       : {student.get('name', '')}\n"
                    f"Email      : {student.get('email', '')}\n"
                    f"Mobile     : {student.get('mobile', '')}\n"
                    f"Gender     : {student.get('gender', '')}\n"
                    f"Age        : {student.get('age', '')}\n"
                    f"Branch     : {student.get('branch', '')}\n"
                    f"Semester   : {student.get('semester', '')}\n"
                    f"Year       : {student.get('year', '')}\n"
                    f"Marks      : {student.get('marks', '')}\n"
                    f"CGPA       : {student.get('cgpa', '')}\n"
                    f"Attendance : {student.get('attendance', '')}\n"
                    f"Supplies   : {student.get('supplies', '')}\n"
                    f"Status     : {student.get('status', '')}"
                )

                messagebox.showinfo(
                    "Student Details",
                    details
                )

                return

        messagebox.showerror(
            "Not Found",
            "Student not found."
        )

    tk.Button(
        search_window,
        text="Search",
        command=search,
        width=15
    ).pack(pady=15)


def dashboard():

    students = load_students()

    if not students:
        messagebox.showinfo(
            "Dashboard",
            "No student records found."
        )
        return

    total = len(students)

    male = 0
    female = 0
    active = 0
    inactive = 0
    supplies = 0

    branches = {}

    topper = None

    for student in students:

        gender = student.get("gender", "").lower()

        if gender == "male":
            male += 1

        elif gender == "female":
            female += 1

        status = student.get("status", "").lower()

        if status == "active":
            active += 1

        elif status == "inactive":
            inactive += 1

        try:
            if int(student.get("supplies", 0)) > 0:
                supplies += 1
        except ValueError:
            pass

        branch = student.get("branch", "Unknown")

        branches[branch] = branches.get(branch, 0) + 1

        try:
            marks = float(student.get("marks", 0))

            if topper is None or marks > float(topper.get("marks", 0)):
                topper = student

        except ValueError:
            pass

    branch_text = ""

    for branch, count in branches.items():
        branch_text += f"{branch} : {count}\n"

    topper_text = "No topper information"

    if topper:
        topper_text = (
            f"Name  : {topper.get('name', '')}\n"
            f"Marks : {topper.get('marks', '')}\n"
            f"Branch: {topper.get('branch', '')}"
        )

    dashboard_text = (
        f"Total Students       : {total}\n"
        f"Male Students        : {male}\n"
        f"Female Students      : {female}\n"
        f"Active Students      : {active}\n"
        f"Inactive Students    : {inactive}\n"
        f"Students with Supply : {supplies}\n\n"
        f"Branch Wise Count\n"
        f"-------------------------\n"
        f"{branch_text}\n"
        f"Topper Student\n"
        f"-------------------------\n"
        f"{topper_text}"
    )

    messagebox.showinfo(
        "Student Dashboard",
        dashboard_text
    )

def update_student_gui():

    selected = table.selection()

    if not selected:
        messagebox.showwarning(
            "Select Student",
            "Please select a student from the table."
        )
        return

    values = table.item(selected[0], "values")

    student_id = values[0]

    students = load_students()

    selected_student = None

    for student in students:
        if student.get("student_id") == student_id:
            selected_student = student
            break

    if selected_student is None:
        messagebox.showerror(
            "Error",
            "Student not found."
        )
        return

    update_window = tk.Toplevel(window)

    update_window.title("Update Student")

    update_window.geometry("500x500")

    update_window.resizable(False, False)

    tk.Label(
        update_window,
        text="UPDATE STUDENT",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    form = tk.Frame(update_window)

    form.pack()

    name_var = tk.StringVar(
        value=selected_student.get("name", "")
    )

    email_var = tk.StringVar(
        value=selected_student.get("email", "")
    )

    mobile_var = tk.StringVar(
        value=selected_student.get("mobile", "")
    )

    branch_var = tk.StringVar(
        value=selected_student.get("branch", "")
    )

    semester_var = tk.StringVar(
        value=selected_student.get("semester", "")
    )

    marks_var = tk.StringVar(
        value=selected_student.get("marks", "")
    )

    cgpa_var = tk.StringVar(
        value=selected_student.get("cgpa", "")
    )

    attendance_var = tk.StringVar(
        value=selected_student.get("attendance", "")
    )

    fields = [
        ("Name", name_var),
        ("Email", email_var),
        ("Mobile", mobile_var),
        ("Branch", branch_var),
        ("Semester", semester_var),
        ("Marks", marks_var),
        ("CGPA", cgpa_var),
        ("Attendance", attendance_var)
    ]

    for row, (label, variable) in enumerate(fields):

        tk.Label(
            form,
            text=label + ":",
            width=15,
            anchor="w"
        ).grid(
            row=row,
            column=0,
            padx=10,
            pady=7
        )

        tk.Entry(
            form,
            textvariable=variable,
            width=30
        ).grid(
            row=row,
            column=1,
            padx=10,
            pady=7
        )

    def update():

        if not name_var.get().strip():
            messagebox.showwarning(
                "Invalid Data",
                "Name cannot be empty."
            )
            return

        try:
            float(marks_var.get())
            float(cgpa_var.get())
            float(attendance_var.get())

        except ValueError:
            messagebox.showerror(
                "Invalid Data",
                "Marks, CGPA and Attendance must be numbers."
            )
            return

        selected_student["name"] = name_var.get().strip()
        selected_student["email"] = email_var.get().strip()
        selected_student["mobile"] = mobile_var.get().strip()
        selected_student["branch"] = branch_var.get().strip()
        selected_student["semester"] = semester_var.get().strip()
        selected_student["marks"] = marks_var.get().strip()
        selected_student["cgpa"] = cgpa_var.get().strip()
        selected_student["attendance"] = attendance_var.get().strip()

        save_students(students)

        messagebox.showinfo(
            "Success",
            "Student Updated Successfully!"
        )

        update_window.destroy()

        view_students()

    tk.Button(
        update_window,
        text="Update Student",
        width=20,
        command=update
    ).pack(pady=20)

    tk.Button(
        update_window,
        text="Cancel",
        width=20,
        command=update_window.destroy
    ).pack()


def delete_student_gui():

    selected = table.selection()

    if not selected:
        messagebox.showwarning(
            "Select Student",
            "Please select a student from the table."
        )
        return

    values = table.item(selected[0], "values")

    student_id = values[0]
    student_name = values[1]

    confirmation = messagebox.askyesno(
        "Confirm Delete",
        f"Are you sure you want to delete\n"
        f"{student_name} ({student_id})?"
    )

    if not confirmation:
        return

    students = load_students()

    new_students = []

    for student in students:

        if student.get("student_id") != student_id:
            new_students.append(student)

    if len(new_students) == len(students):

        messagebox.showerror(
            "Error",
            "Student not found."
        )

        return

    save_students(new_students)

    messagebox.showinfo(
        "Success",
        "Student Deleted Successfully!"
    )

    view_students()

def report_card_gui():

    selected = table.selection()

    if not selected:
        messagebox.showwarning(
            "Select Student",
            "Please select a student from the table first."
        )
        return

    values = table.item(selected[0], "values")

    student_id = values[0]

    students = load_students()

    student = None

    for record in students:

        if record.get("student_id") == student_id:
            student = record
            break

    if student is None:

        messagebox.showerror(
            "Error",
            "Student not found."
        )

        return

    report_window = tk.Toplevel(window)

    report_window.title("Student Report Card")

    report_window.geometry("600x700")

    report_window.resizable(False, False)

    # -----------------------------------------------------
    # Title
    # -----------------------------------------------------

    tk.Label(
        report_window,
        text="STUDENT REPORT CARD",
        font=("Arial", 22, "bold")
    ).pack(pady=20)

    # -----------------------------------------------------
    # Report Frame
    # -----------------------------------------------------

    report_frame = tk.Frame(
        report_window
    )

    report_frame.pack(
        padx=30,
        pady=10
    )

    subjects = student.get("subjects", [])

    if isinstance(subjects, list):
        subjects_text = ", ".join(subjects)
    else:
        subjects_text = str(subjects)

    details = [
        ("Student ID", student.get("student_id", "")),
        ("Name", student.get("name", "")),
        ("Email", student.get("email", "")),
        ("Mobile", student.get("mobile", "")),
        ("Gender", student.get("gender", "")),
        ("Age", student.get("age", "")),
        ("Branch", student.get("branch", "")),
        ("Semester", student.get("semester", "")),
        ("Year", student.get("year", "")),
        ("Subjects", subjects_text),
        ("Marks", student.get("marks", "")),
        ("CGPA", student.get("cgpa", "")),
        ("Attendance", student.get("attendance", "")),
        ("Supplies", student.get("supplies", "")),
        ("Status", student.get("status", ""))
    ]

    for row, (label, value) in enumerate(details):

        tk.Label(
            report_frame,
            text=label + " :",
            font=("Arial", 11, "bold"),
            width=15,
            anchor="w"
        ).grid(
            row=row,
            column=0,
            padx=10,
            pady=6
        )

        tk.Label(
            report_frame,
            text=value,
            font=("Arial", 11),
            width=35,
            anchor="w"
        ).grid(
            row=row,
            column=1,
            padx=10,
            pady=6
        )

    # -----------------------------------------------------
    # Close Button
    # -----------------------------------------------------

    tk.Button(
        report_window,
        text="Close",
        width=20,
        command=report_window.destroy
    ).pack(pady=20)


# =========================================================
# TITLE
# =========================================================

title = tk.Label(
    window,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 24, "bold")
)

title.pack(pady=20)


# =========================================================
# BUTTON FRAME
# =========================================================

button_frame = tk.Frame(window)

button_frame.pack(pady=10)


tk.Button(
    button_frame,
    text="Register Student",
    width=20,
    command=register_student_gui
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)


tk.Button(
    button_frame,
    text="View Students",
    width=20,
    command=view_students
).grid(row=0, column=1, padx=10, pady=10)


tk.Button(
    button_frame,
    text="Search Student",
    width=20,
    command=search_student
).grid(row=0, column=2, padx=10, pady=10)


tk.Button(
    button_frame,
    text="Dashboard",
    width=20,
    command=dashboard
).grid(row=1, column=0, padx=10, pady=10)

tk.Button(
    button_frame,
    text="Update Student",
    width=20,
    command=update_student_gui
).grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)

tk.Button(
    button_frame,
    text="Delete Student",
    width=20,
    command=delete_student_gui
).grid(
    row=1,
    column=2,
    padx=10,
    pady=10
)


tk.Button(
    button_frame,
    text="Refresh",
    width=20,
    command=view_students
).grid(
    row=2,
    column=0,
    padx=10,
    pady=10
)


tk.Button(
    button_frame,
    text="Exit",
    width=20,
    command=window.destroy
).grid(
    row=2,
    column=1,
    padx=10,
    pady=10
)

tk.Button(
    button_frame,
    text="Report Card",
    width=20,
    command=report_card_gui
).grid(
    row=2,
    column=2,
    padx=10,
    pady=10
)

tk.Button(
    button_frame,
    text="Export CSV",
    width=20,
    command=export_csv_gui
).grid(
    row=3,
    column=0,
    padx=10,
    pady=10
)


# =========================================================
# STUDENT TABLE
# =========================================================

table_frame = tk.Frame(window)

table_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)


columns = (
    "ID",
    "Name",
    "Email",
    "Branch",
    "Semester",
    "Year",
    "Marks",
    "CGPA",
    "Attendance",
    "Status"
)


table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=10
)


for column in columns:

    table.heading(
        column,
        text=column
    )

    table.column(
        column,
        width=100
    )


table.pack(
    side="left",
    fill="both",
    expand=True
)


# =========================================================
# SCROLLBAR
# =========================================================

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=table.yview
)

table.configure(
    yscrollcommand=scrollbar.set
)

scrollbar.pack(
    side="right",
    fill="y"
)


# =========================================================
# START APPLICATION
# =========================================================

window.mainloop()

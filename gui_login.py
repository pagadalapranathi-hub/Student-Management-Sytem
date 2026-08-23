import tkinter as tk
from tkinter import messagebox, ttk
import csv

from file_handler import load_students, save_students

from validation import (
    validate_student_id,
    validate_name,
    validate_email,
    validate_password,
    validate_mobile,
    validate_age,
    validate_semester,
    validate_year,
    validate_marks,
    validate_cgpa,
    validate_attendance,
    validate_supplies,
    validate_pass_out_year,
    calculate_result,
    calculate_grade
)


# =========================================================
# GLOBAL LOGIN WINDOW
# =========================================================

login_window = None


# =========================================================
# ADMIN DASHBOARD
# =========================================================

def open_admin_dashboard():

    admin_window = tk.Toplevel()

    admin_window.title(
        "Admin Dashboard"
    )

    admin_window.geometry(
        "750x650"
    )

    admin_window.resizable(
        False,
        False
    )

    tk.Label(
        admin_window,
        text="ADMIN DASHBOARD",
        font=("Arial", 25, "bold")
    ).pack(pady=20)

    # =====================================================
    # REGISTER STUDENT
    # =====================================================

    def register_student_gui():

        register_window = tk.Toplevel(
            admin_window
        )

        register_window.title(
            "Register Student"
        )

        register_window.geometry(
            "650x750"
        )

        register_window.resizable(
            False,
            False
        )

        tk.Label(
            register_window,
            text="REGISTER STUDENT",
            font=("Arial", 22, "bold")
        ).pack(pady=15)

        frame = tk.Frame(
            register_window
        )

        frame.pack(
            padx=20,
            pady=10
        )

        labels = [
            "Student ID",
            "Name",
            "Email",
            "Password",
            "Mobile",
            "Gender",
            "Age",
            "Branch",
            "Semester",
            "Year",
            "Subjects",
            "Marks",
            "Join Date",
            "Pass Out Year",
            "Supplies",
            "Status",
            "Attendance",
            "CGPA"
        ]

        entries = {}

        for row, label in enumerate(labels):

            tk.Label(
                frame,
                text=label + ":",
                font=("Arial", 11, "bold"),
                width=18,
                anchor="w"
            ).grid(
                row=row,
                column=0,
                padx=5,
                pady=5
            )

            entry = tk.Entry(
                frame,
                width=35
            )

            entry.grid(
                row=row,
                column=1,
                padx=5,
                pady=5
            )

            entries[label] = entry

        # -------------------------------------------------
        # SAVE NEW STUDENT
        # -------------------------------------------------

        def save_new_student():

            student_id = entries[
                "Student ID"
            ].get().strip()

            name = entries[
                "Name"
            ].get().strip()

            email = entries[
                "Email"
            ].get().strip()

            password = entries[
                "Password"
            ].get().strip()

            mobile = entries[
                "Mobile"
            ].get().strip()

            gender = entries[
                "Gender"
            ].get().strip()

            age = entries[
                "Age"
            ].get().strip()

            branch = entries[
                "Branch"
            ].get().strip()

            semester = entries[
                "Semester"
            ].get().strip()

            year = entries[
                "Year"
            ].get().strip()

            subjects = entries[
                "Subjects"
            ].get().strip()

            marks = entries[
                "Marks"
            ].get().strip()

            join_date = entries[
                "Join Date"
            ].get().strip()

            pass_out_year = entries[
                "Pass Out Year"
            ].get().strip()

            supplies = entries[
                "Supplies"
            ].get().strip()

            status = entries[
                "Status"
            ].get().strip()

            attendance = entries[
                "Attendance"
            ].get().strip()

            cgpa = entries[
                "CGPA"
            ].get().strip()

            # -------------------------------------------------
            # REQUIRED FIELD CHECK
            # -------------------------------------------------

            if not student_id:

                messagebox.showwarning(
                    "Validation",
                    "Please enter Student ID."
                )

                return

            if not name:

                messagebox.showwarning(
                    "Validation",
                    "Please enter Name."
                )

                return

            if not email:

                messagebox.showwarning(
                    "Validation",
                    "Please enter Email."
                )

                return

            if not password:

                messagebox.showwarning(
                    "Validation",
                    "Please enter Password."
                )

                return

            # -------------------------------------------------
            # VALIDATION
            # -------------------------------------------------

            if not validate_student_id(
                student_id
            ):

                messagebox.showerror(
                    "Validation Error",
                    "Invalid Student ID."
                )

                return

            if not validate_name(
                name
            ):

                messagebox.showerror(
                    "Validation Error",
                    "Name should contain only letters and spaces."
                )

                return

            if not validate_email(
                email
            ):

                messagebox.showerror(
                    "Validation Error",
                    "Please enter a valid email address."
                )

                return

            if not validate_password(
                password
            ):

                messagebox.showerror(
                    "Validation Error",
                    "Password must contain at least 6 characters."
                )

                return

            if not validate_mobile(
                mobile
            ):

                messagebox.showerror(
                    "Validation Error",
                    "Mobile number must contain exactly 10 digits."
                )

                return

            if not validate_age(
                age
            ):

                messagebox.showerror(
                    "Validation Error",
                    "Age must be between 15 and 60."
                )

                return

            if not validate_semester(
                semester
            ):

                messagebox.showerror(
                    "Validation Error",
                    "Semester must be between 1 and 8."
                )

                return

            if not validate_year(
                year
            ):

                messagebox.showerror(
                    "Validation Error",
                    "Year must be between 1 and 4."
                )

                return

            if not validate_marks(
                marks
            ):

                messagebox.showerror(
                    "Validation Error",
                    "Marks must be between 0 and 100."
                )

                return

            if not validate_cgpa(
                cgpa
            ):

                messagebox.showerror(
                    "Validation Error",
                    "CGPA must be between 0 and 10."
                )

                return

            if not validate_attendance(
                attendance
            ):

                messagebox.showerror(
                    "Validation Error",
                    "Attendance must be between 0 and 100."
                )

                return

            if not validate_supplies(
                supplies
            ):

                messagebox.showerror(
                    "Validation Error",
                    "Supplies cannot be negative."
                )

                return

            if not validate_pass_out_year(
                pass_out_year
            ):

                messagebox.showerror(
                    "Validation Error",
                    "Please enter a valid Pass Out Year."
                )

                return

            # -------------------------------------------------
            # LOAD STUDENTS
            # -------------------------------------------------

            students = load_students()

            # -------------------------------------------------
            # CHECK DUPLICATE ID
            # -------------------------------------------------

            for student in students:

                if str(
                    student.get(
                        "student_id",
                        ""
                    )
                ) == student_id:

                    messagebox.showerror(
                        "Duplicate",
                        "Student ID already exists."
                    )

                    return

            # -------------------------------------------------
            # CALCULATE GRADE
            # -------------------------------------------------

            grade = calculate_grade(
                marks
            )

            # -------------------------------------------------
            # CALCULATE RESULT
            # -------------------------------------------------

            result = calculate_result(
                marks,
                attendance,
                supplies
            )

            # -------------------------------------------------
            # CREATE STUDENT
            # -------------------------------------------------

            new_student = {

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

                "join_date": join_date,

                "pass_out_year": pass_out_year,

                "supplies": supplies,

                "status": result,

                "attendance": attendance,

                "cgpa": cgpa,

                "grade": grade
            }

            students.append(
                new_student
            )

            save_students(
                students
            )

            messagebox.showinfo(
                "Success",
                "Student registered successfully."
            )

            register_window.destroy()

        tk.Button(
            register_window,
            text="Register Student",
            width=25,
            height=2,
            command=save_new_student
        ).pack(
            pady=15
        )

    # =====================================================
    # VIEW STUDENTS
    # =====================================================

    def view_students_gui():

        view_window = tk.Toplevel(
            admin_window
        )

        view_window.title(
            "View Students"
        )

        view_window.geometry(
            "1100x550"
        )

        tk.Label(
            view_window,
            text="ALL STUDENTS",
            font=("Arial", 22, "bold")
        ).pack(pady=15)

        # -------------------------------------------------
        # TABLE FRAME
        # -------------------------------------------------

        table_frame = tk.Frame(
            view_window
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columns = (
            "ID",
            "Name",
            "Email",
            "Branch",
            "Semester",
            "Marks",
            "CGPA",
            "Attendance"
        )

        tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            tree.heading(
                column,
                text=column
            )

            tree.column(
                column,
                width=130
            )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=tree.yview
        )

        tree.configure(
            yscrollcommand=scrollbar.set
        )

        tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # -------------------------------------------------
        # LOAD TABLE
        # -------------------------------------------------

        def load_table():

            for item in tree.get_children():

                tree.delete(
                    item
                )

            students = load_students()

            for student in students:

                tree.insert(
                    "",
                    tk.END,
                    values=(

                        student.get(
                            "student_id",
                            ""
                        ),

                        student.get(
                            "name",
                            ""
                        ),

                        student.get(
                            "email",
                            ""
                        ),

                        student.get(
                            "branch",
                            ""
                        ),

                        student.get(
                            "semester",
                            ""
                        ),

                        student.get(
                            "marks",
                            ""
                        ),

                        student.get(
                            "cgpa",
                            ""
                        ),

                        student.get(
                            "attendance",
                            ""
                        )
                    )
                )

        # -------------------------------------------------
        # REFRESH BUTTON
        # -------------------------------------------------

        tk.Button(
            view_window,
            text="Refresh",
            width=20,
            command=load_table
        ).pack(
            pady=10
        )

        load_table()

    # =====================================================
    # SEARCH STUDENT
    # =====================================================

    def search_student_gui():

        search_window = tk.Toplevel(
            admin_window
        )

        search_window.title(
            "Search Student"
        )

        search_window.geometry(
            "550x500"
        )

        tk.Label(
            search_window,
            text="SEARCH STUDENT",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        tk.Label(
            search_window,
            text="Enter Student ID:"
        ).pack(pady=5)

        search_entry = tk.Entry(
            search_window,
            width=35
        )

        search_entry.pack(
            pady=5
        )

        result_label = tk.Label(
            search_window,
            text="",
            font=("Arial", 11),
            justify="left"
        )

        result_label.pack(
            pady=20
        )

        def search():

            student_id = search_entry.get().strip()

            if not student_id:

                messagebox.showwarning(
                    "Warning",
                    "Please enter Student ID."
                )

                return

            students = load_students()

            for student in students:

                if str(
                    student.get(
                        "student_id",
                        ""
                    )
                ) == student_id:

                    result = (

                        f"Student ID : {student.get('student_id', '')}\n\n"

                        f"Name       : {student.get('name', '')}\n\n"

                        f"Email      : {student.get('email', '')}\n\n"

                        f"Mobile     : {student.get('mobile', '')}\n\n"

                        f"Branch     : {student.get('branch', '')}\n\n"

                        f"Semester   : {student.get('semester', '')}\n\n"

                        f"Marks      : {student.get('marks', '')}\n\n"

                        f"Grade      : {student.get('grade', '')}\n\n"

                        f"CGPA       : {student.get('cgpa', '')}\n\n"

                        f"Attendance : {student.get('attendance', '')}%\n\n"

                        f"Result     : {student.get('status', '')}"
                    )

                    result_label.config(
                        text=result
                    )

                    return

            result_label.config(
                text="Student not found."
            )

        tk.Button(
            search_window,
            text="Search",
            width=20,
            command=search
        ).pack(
            pady=10
        )

    # =====================================================
    # DELETE STUDENT
    # =====================================================

    def delete_student_gui():

        delete_window = tk.Toplevel(
            admin_window
        )

        delete_window.title(
            "Delete Student"
        )

        delete_window.geometry(
            "600x550"
        )

        delete_window.resizable(
            False,
            False
        )

        tk.Label(
            delete_window,
            text="DELETE STUDENT",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        search_frame = tk.Frame(
            delete_window
        )

        search_frame.pack(
            pady=10
        )

        tk.Label(
            search_frame,
            text="Student ID:",
            font=("Arial", 11, "bold")
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        id_entry = tk.Entry(
            search_frame,
            width=30
        )

        id_entry.grid(
            row=0,
            column=1,
            padx=5
        )

        details_label = tk.Label(
            delete_window,
            text="",
            font=("Arial", 11),
            justify="left"
        )

        details_label.pack(
            pady=20
        )

        # -------------------------------------------------
        # LOAD STUDENT
        # -------------------------------------------------

        def load_student():

            student_id = id_entry.get().strip()

            if not student_id:

                messagebox.showwarning(
                    "Warning",
                    "Please enter Student ID."
                )

                return

            students = load_students()

            for student in students:

                if str(
                    student.get(
                        "student_id",
                        ""
                    )
                ) == student_id:

                    details = (

                        "Student Details\n"
                        "------------------------------\n\n"

                        f"Student ID : "
                        f"{student.get('student_id', '')}\n\n"

                        f"Name       : "
                        f"{student.get('name', '')}\n\n"

                        f"Email      : "
                        f"{student.get('email', '')}\n\n"

                        f"Mobile     : "
                        f"{student.get('mobile', '')}\n\n"

                        f"Branch     : "
                        f"{student.get('branch', '')}\n\n"

                        f"Semester   : "
                        f"{student.get('semester', '')}\n\n"

                        f"Marks      : "
                        f"{student.get('marks', '')}\n\n"

                        f"CGPA       : "
                        f"{student.get('cgpa', '')}\n\n"

                        f"Attendance : "
                        f"{student.get('attendance', '')}%\n\n"

                        f"Result     : "
                        f"{student.get('status', '')}"
                    )

                    details_label.config(
                        text=details
                    )

                    return

            details_label.config(
                text="Student not found."
            )

        # -------------------------------------------------
        # DELETE
        # -------------------------------------------------

        def delete_student():

            student_id = id_entry.get().strip()

            if not student_id:

                messagebox.showwarning(
                    "Warning",
                    "Please enter Student ID."
                )

                return

            students = load_students()

            student_found = None

            for student in students:

                if str(
                    student.get(
                        "student_id",
                        ""
                    )
                ) == student_id:

                    student_found = student

                    break

            if student_found is None:

                messagebox.showerror(
                    "Error",
                    "Student not found."
                )

                return

            confirm = messagebox.askyesno(

                "Confirm Delete",

                "Are you sure you want to delete "
                f"{student_found.get('name', '')} "
                f"(ID: {student_id})?"
            )

            if not confirm:

                return

            students.remove(
                student_found
            )

            save_students(
                students
            )

            messagebox.showinfo(
                "Success",
                "Student deleted successfully."
            )

            delete_window.destroy()

        tk.Button(
            search_frame,
            text="Load Student",
            width=18,
            command=load_student
        ).grid(
            row=0,
            column=2,
            padx=10
        )

        tk.Button(
            delete_window,
            text="Delete Student",
            width=25,
            height=2,
            command=delete_student
        ).pack(
            pady=15
        )

    # =====================================================
    # UPDATE STUDENT
    # =====================================================

    def update_student_gui():

        update_window = tk.Toplevel(
            admin_window
        )

        update_window.title(
            "Update Student"
        )

        update_window.geometry(
            "650x700"
        )

        update_window.resizable(
            False,
            False
        )

        tk.Label(
            update_window,
            text="UPDATE STUDENT",
            font=("Arial", 22, "bold")
        ).pack(pady=15)

        search_frame = tk.Frame(
            update_window
        )

        search_frame.pack(
            pady=10
        )

        tk.Label(
            search_frame,
            text="Student ID:",
            font=("Arial", 11, "bold")
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        id_entry = tk.Entry(
            search_frame,
            width=25
        )

        id_entry.grid(
            row=0,
            column=1,
            padx=5
        )

        form_frame = tk.Frame(
            update_window
        )

        form_frame.pack(
            pady=10
        )

        fields = [
            "Name",
            "Email",
            "Mobile",
            "Gender",
            "Age",
            "Branch",
            "Semester",
            "Year",
            "Subjects",
            "Marks",
            "Join Date",
            "Pass Out Year",
            "Supplies",
            "Attendance",
            "CGPA"
        ]

        entries = {}

        for row, field in enumerate(fields):

            tk.Label(
                form_frame,
                text=field + ":",
                font=("Arial", 10, "bold"),
                width=18,
                anchor="w"
            ).grid(
                row=row,
                column=0,
                padx=5,
                pady=3
            )

            entry = tk.Entry(
                form_frame,
                width=35
            )

            entry.grid(
                row=row,
                column=1,
                padx=5,
                pady=3
            )

            entries[field] = entry

        # -------------------------------------------------
        # LOAD STUDENT
        # -------------------------------------------------

        def load_student():

            student_id = id_entry.get().strip()

            if not student_id:

                messagebox.showwarning(
                    "Warning",
                    "Please enter Student ID."
                )

                return

            students = load_students()

            for student in students:

                if str(
                    student.get(
                        "student_id",
                        ""
                    )
                ) == student_id:

                    for field in fields:

                        entries[field].delete(
                            0,
                            tk.END
                        )

                    entries["Name"].insert(
                        0,
                        student.get(
                            "name",
                            ""
                        )
                    )

                    entries["Email"].insert(
                        0,
                        student.get(
                            "email",
                            ""
                        )
                    )

                    entries["Mobile"].insert(
                        0,
                        student.get(
                            "mobile",
                            ""
                        )
                    )

                    entries["Gender"].insert(
                        0,
                        student.get(
                            "gender",
                            ""
                        )
                    )

                    entries["Age"].insert(
                        0,
                        student.get(
                            "age",
                            ""
                        )
                    )

                    entries["Branch"].insert(
                        0,
                        student.get(
                            "branch",
                            ""
                        )
                    )

                    entries["Semester"].insert(
                        0,
                        student.get(
                            "semester",
                            ""
                        )
                    )

                    entries["Year"].insert(
                        0,
                        student.get(
                            "year",
                            ""
                        )
                    )

                    subjects = student.get(
                        "subjects",
                        ""
                    )

                    if isinstance(
                        subjects,
                        list
                    ):

                        subjects = ", ".join(
                            subjects
                        )

                    entries["Subjects"].insert(
                        0,
                        subjects
                    )

                    entries["Marks"].insert(
                        0,
                        student.get(
                            "marks",
                            ""
                        )
                    )

                    entries["Join Date"].insert(
                        0,
                        student.get(
                            "join_date",
                            ""
                        )
                    )

                    entries["Pass Out Year"].insert(
                        0,
                        student.get(
                            "pass_out_year",
                            ""
                        )
                    )

                    entries["Supplies"].insert(
                        0,
                        student.get(
                            "supplies",
                            ""
                        )
                    )

                    entries["Attendance"].insert(
                        0,
                        student.get(
                            "attendance",
                            ""
                        )
                    )

                    entries["CGPA"].insert(
                        0,
                        student.get(
                            "cgpa",
                            ""
                        )
                    )

                    messagebox.showinfo(
                        "Success",
                        "Student details loaded."
                    )

                    return

            messagebox.showerror(
                "Error",
                "Student not found."
            )

        # -------------------------------------------------
        # SAVE UPDATE
        # -------------------------------------------------

        def save_update():

            student_id = id_entry.get().strip()

            name = entries[
                "Name"
            ].get().strip()

            email = entries[
                "Email"
            ].get().strip()

            mobile = entries[
                "Mobile"
            ].get().strip()

            gender = entries[
                "Gender"
            ].get().strip()

            age = entries[
                "Age"
            ].get().strip()

            branch = entries[
                "Branch"
            ].get().strip()

            semester = entries[
                "Semester"
            ].get().strip()

            year = entries[
                "Year"
            ].get().strip()

            subjects = entries[
                "Subjects"
            ].get().strip()

            marks = entries[
                "Marks"
            ].get().strip()

            join_date = entries[
                "Join Date"
            ].get().strip()

            pass_out_year = entries[
                "Pass Out Year"
            ].get().strip()

            supplies = entries[
                "Supplies"
            ].get().strip()

            attendance = entries[
                "Attendance"
            ].get().strip()

            cgpa = entries[
                "CGPA"
            ].get().strip()

            # -------------------------------------------------
            # VALIDATION
            # -------------------------------------------------

            if not validate_student_id(
                student_id
            ):

                messagebox.showerror(
                    "Error",
                    "Invalid Student ID."
                )

                return

            if not validate_name(
                name
            ):

                messagebox.showerror(
                    "Error",
                    "Invalid name."
                )

                return

            if not validate_email(
                email
            ):

                messagebox.showerror(
                    "Error",
                    "Invalid email."
                )

                return

            if not validate_mobile(
                mobile
            ):

                messagebox.showerror(
                    "Error",
                    "Mobile number must contain 10 digits."
                )

                return

            if not validate_age(
                age
            ):

                messagebox.showerror(
                    "Error",
                    "Age must be between 15 and 60."
                )

                return

            if not validate_semester(
                semester
            ):

                messagebox.showerror(
                    "Error",
                    "Semester must be between 1 and 8."
                )

                return

            if not validate_year(
                year
            ):

                messagebox.showerror(
                    "Error",
                    "Year must be between 1 and 4."
                )

                return

            if not validate_marks(
                marks
            ):

                messagebox.showerror(
                    "Error",
                    "Marks must be between 0 and 100."
                )

                return

            if not validate_cgpa(
                cgpa
            ):

                messagebox.showerror(
                    "Error",
                    "CGPA must be between 0 and 10."
                )

                return

            if not validate_attendance(
                attendance
            ):

                messagebox.showerror(
                    "Error",
                    "Attendance must be between 0 and 100."
                )

                return

            if not validate_supplies(
                supplies
            ):

                messagebox.showerror(
                    "Error",
                    "Supplies cannot be negative."
                )

                return

            if not validate_pass_out_year(
                pass_out_year
            ):

                messagebox.showerror(
                    "Error",
                    "Invalid Pass Out Year."
                )

                return

            # -------------------------------------------------
            # LOAD STUDENTS
            # -------------------------------------------------

            students = load_students()

            found = False

            # -------------------------------------------------
            # UPDATE
            # -------------------------------------------------

            for student in students:

                if str(
                    student.get(
                        "student_id",
                        ""
                    )
                ) == student_id:

                    student["name"] = name

                    student["email"] = email

                    student["mobile"] = mobile

                    student["gender"] = gender

                    student["age"] = age

                    student["branch"] = branch

                    student["semester"] = semester

                    student["year"] = year

                    student["subjects"] = subjects

                    student["marks"] = marks

                    student["join_date"] = join_date

                    student["pass_out_year"] = (
                        pass_out_year
                    )

                    student["supplies"] = supplies

                    student["attendance"] = (
                        attendance
                    )

                    student["cgpa"] = cgpa

                    student["grade"] = (
                        calculate_grade(
                            marks
                        )
                    )

                    student["status"] = (
                        calculate_result(
                            marks,
                            attendance,
                            supplies
                        )
                    )

                    found = True

                    break

            if not found:

                messagebox.showerror(
                    "Error",
                    "Student not found."
                )

                return

            save_students(
                students
            )

            messagebox.showinfo(
                "Success",
                "Student details updated successfully."
            )

            update_window.destroy()

        # -------------------------------------------------
        # UPDATE BUTTONS
        # -------------------------------------------------

        tk.Button(
            search_frame,
            text="Load Student",
            width=18,
            command=load_student
        ).grid(
            row=0,
            column=2,
            padx=10
        )

        tk.Button(
            update_window,
            text="Save Changes",
            width=25,
            height=2,
            command=save_update
        ).pack(
            pady=15
        )

    # =====================================================
    # ADMIN DASHBOARD STATISTICS
    # =====================================================

    def dashboard_gui():

        dashboard_window = tk.Toplevel(
            admin_window
        )

        dashboard_window.title(
            "Dashboard"
        )

        dashboard_window.geometry(
            "600x500"
        )

        students = load_students()

        total = len(
            students
        )

        passed = 0

        failed = 0

        branches = {}

        for student in students:

            status = str(
                student.get(
                    "status",
                    ""
                )
            ).lower()

            if status == "pass":

                passed += 1

            elif status == "fail":

                failed += 1

            branch = student.get(
                "branch",
                "Unknown"
            )

            branches[
                branch
            ] = branches.get(
                branch,
                0
            ) + 1

        tk.Label(
            dashboard_window,
            text="SYSTEM DASHBOARD",
            font=("Arial", 24, "bold")
        ).pack(pady=25)

        tk.Label(
            dashboard_window,
            text=f"Total Students : {total}",
            font=("Arial", 16)
        ).pack(pady=10)

        tk.Label(
            dashboard_window,
            text=f"Passed Students : {passed}",
            font=("Arial", 16)
        ).pack(pady=10)

        tk.Label(
            dashboard_window,
            text=f"Failed Students : {failed}",
            font=("Arial", 16)
        ).pack(pady=10)

        branch_text = (
            "Students by Branch:\n\n"
        )

        for branch, count in branches.items():

            branch_text += (
                f"{branch} : {count}\n"
            )

        tk.Label(
            dashboard_window,
            text=branch_text,
            font=("Arial", 14),
            justify="left"
        ).pack(pady=20)

    # =====================================================
    # EXPORT CSV
    # =====================================================
    # =====================================================
    # EXPORT STUDENTS TO CSV
    # =====================================================

    def export_csv():

        try:
            students = load_students()

            # Check whether students exist
            if not students:

                messagebox.showwarning(
                     "Export CSV",
                     "No student records found."
                )

                return

            # CSV file name
            file_name = "students.csv"

            # Get all fields from all students
            fields = set()

            for student in students:

                fields.update(
                     student.keys()
                )

            # Convert set to sorted list
            fields = sorted(
                 fields
            )

            # Write CSV file
            with open(
                 file_name,
                 "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=fields,
                    extrasaction="ignore"
                )

                writer.writeheader()

                writer.writerows(
                     students
                )

            messagebox.showinfo(
                "Export Successful",
                f"Student data exported successfully!\n\n"
                f"File: {file_name}"
             )

        except Exception as error:

            messagebox.showerror(
                   "Export Error",
                   f"Unable to export CSV.\n\n"
                   f"Error:\n{error}"
             )

    
    # =====================================================
    # ADMIN BUTTONS
    # =====================================================

    button_frame = tk.Frame(
        admin_window
    )

    button_frame.pack(
        pady=20
    )

    buttons = [

        (
            "Register Student",
            register_student_gui
        ),

        (
            "View Students",
            view_students_gui
        ),

        (
            "Search Student",
            search_student_gui
        ),

        (
            "Update Student",
            update_student_gui
        ),

        (
            "Delete Student",
            delete_student_gui
        ),

        (
            "Dashboard",
            dashboard_gui
        ),

        (
            "Export CSV",
            export_csv
        ),

        (
            "Logout",
            admin_window.destroy
        )
    ]

    for index, (
        text,
        command
    ) in enumerate(buttons):

        tk.Button(
            button_frame,
            text=text,
            width=25,
            height=2,
            command=command
        ).grid(
            row=index // 2,
            column=index % 2,
            padx=10,
            pady=10
        )


# =========================================================
# STUDENT DASHBOARD
# =========================================================

def open_student_dashboard(student):

    student_window = tk.Toplevel()

    student_window.title(
        "Student Dashboard"
    )

    student_window.geometry(
        "650x600"
    )

    student_window.resizable(
        False,
        False
    )

    tk.Label(
        student_window,
        text="STUDENT DASHBOARD",
        font=("Arial", 24, "bold")
    ).pack(pady=20)

    tk.Label(
        student_window,
        text=f"Welcome, {student.get('name', '')}",
        font=("Arial", 16)
    ).pack(pady=5)

    button_frame = tk.Frame(
        student_window
    )

    button_frame.pack(
        pady=30
    )

    # =====================================================
    # MY PROFILE
    # =====================================================

    def show_profile():

        window = tk.Toplevel(
            student_window
        )

        window.title(
            "My Profile"
        )

        window.geometry(
            "550x550"
        )

        tk.Label(
            window,
            text="MY PROFILE",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        details = [

            (
                "Student ID",
                student.get(
                    "student_id",
                    ""
                )
            ),

            (
                "Name",
                student.get(
                    "name",
                    ""
                )
            ),

            (
                "Email",
                student.get(
                    "email",
                    ""
                )
            ),

            (
                "Mobile",
                student.get(
                    "mobile",
                    ""
                )
            ),

            (
                "Gender",
                student.get(
                    "gender",
                    ""
                )
            ),

            (
                "Age",
                student.get(
                    "age",
                    ""
                )
            ),

            (
                "Branch",
                student.get(
                    "branch",
                    ""
                )
            ),

            (
                "Semester",
                student.get(
                    "semester",
                    ""
                )
            ),

            (
                "Year",
                student.get(
                    "year",
                    ""
                )
            ),

            (
                "Join Date",
                student.get(
                    "join_date",
                    ""
                )
            ),

            (
                "Pass Out Year",
                student.get(
                    "pass_out_year",
                    ""
                )
            )
        ]

        frame = tk.Frame(
            window
        )

        frame.pack(
            padx=20,
            pady=10
        )

        for row, (
            label,
            value
        ) in enumerate(details):

            tk.Label(
                frame,
                text=label + ":",
                font=("Arial", 12, "bold"),
                width=20,
                anchor="w"
            ).grid(
                row=row,
                column=0,
                padx=10,
                pady=6
            )

            tk.Label(
                frame,
                text=value,
                font=("Arial", 12),
                width=30,
                anchor="w"
            ).grid(
                row=row,
                column=1,
                padx=10,
                pady=6
            )

    # =====================================================
    # MY MARKS
    # =====================================================

    def show_marks():

        window = tk.Toplevel(
            student_window
        )

        window.title(
            "My Marks"
        )

        window.geometry(
            "500x400"
        )

        tk.Label(
            window,
            text="MY MARKS",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        subjects = student.get(
            "subjects",
            ""
        )

        if isinstance(
            subjects,
            list
        ):

            subjects = ", ".join(
                subjects
            )

        tk.Label(
            window,
            text=f"Subjects: {subjects}",
            font=("Arial", 13)
        ).pack(pady=15)

        tk.Label(
            window,
            text=f"Marks: {student.get('marks', '')}",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        grade = student.get(
            "grade",
            calculate_grade(
                student.get(
                    "marks",
                    0
                )
            )
        )

        tk.Label(
            window,
            text=f"Grade: {grade}",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

    # =====================================================
    # MY ATTENDANCE
    # =====================================================

    def show_attendance():

        window = tk.Toplevel(
            student_window
        )

        window.title(
            "My Attendance"
        )

        window.geometry(
            "450x350"
        )

        attendance = student.get(
            "attendance",
            0
        )

        tk.Label(
            window,
            text="MY ATTENDANCE",
            font=("Arial", 22, "bold")
        ).pack(pady=30)

        tk.Label(
            window,
            text=f"{attendance}%",
            font=("Arial", 35, "bold")
        ).pack(pady=20)

        try:

            attendance_value = float(
                attendance
            )

        except (
            ValueError,
            TypeError
        ):

            attendance_value = 0

        if attendance_value >= 75:

            message = (
                "Attendance Requirement Satisfied"
            )

        else:

            message = (
                "Attendance Below 75%"
            )

        tk.Label(
            window,
            text=message,
            font=("Arial", 13)
        ).pack(pady=10)

    # =====================================================
    # MY RESULT
    # =====================================================

    def show_result():

        window = tk.Toplevel(
            student_window
        )

        window.title(
            "My Result"
        )

        window.geometry(
            "500x450"
        )

        marks = student.get(
            "marks",
            0
        )

        grade = student.get(
            "grade",
            calculate_grade(
                marks
            )
        )

        tk.Label(
            window,
            text="MY RESULT",
            font=("Arial", 22, "bold")
        ).pack(pady=25)

        tk.Label(
            window,
            text=f"Marks : {marks}",
            font=("Arial", 15)
        ).pack(pady=10)

        tk.Label(
            window,
            text=f"Grade : {grade}",
            font=("Arial", 15)
        ).pack(pady=10)

        tk.Label(
            window,
            text=f"CGPA : {student.get('cgpa', '')}",
            font=("Arial", 15)
        ).pack(pady=10)

        tk.Label(
            window,
            text=f"Supplies : {student.get('supplies', '')}",
            font=("Arial", 15)
        ).pack(pady=10)

        tk.Label(
            window,
            text=f"Result : {student.get('status', '')}",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

    # =====================================================
    # MY REPORT CARD
    # =====================================================

    def show_report_card():

        window = tk.Toplevel(
            student_window
        )

        window.title(
            "My Report Card"
        )

        window.geometry(
            "700x650"
        )

        tk.Label(
            window,
            text="MY REPORT CARD",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        report_text = tk.Text(
            window,
            width=75,
            height=28,
            font=("Courier New", 11)
        )

        report_text.pack(
            padx=10,
            pady=10
        )

        subjects = student.get(
            "subjects",
            ""
        )

        if isinstance(
            subjects,
            list
        ):

            subjects = ", ".join(
                subjects
            )

        report = (

            "==================================================\n"
            "                 STUDENT REPORT CARD\n"
            "==================================================\n\n"

            f"Student ID : {student.get('student_id', '')}\n"
            f"Name       : {student.get('name', '')}\n"
            f"Email      : {student.get('email', '')}\n"
            f"Mobile     : {student.get('mobile', '')}\n"
            f"Branch     : {student.get('branch', '')}\n"
            f"Semester   : {student.get('semester', '')}\n"
            f"Year       : {student.get('year', '')}\n\n"

            f"Subjects   : {subjects}\n"
            f"Marks      : {student.get('marks', '')}\n"
            f"Grade      : {student.get('grade', '')}\n"
            f"CGPA       : {student.get('cgpa', '')}\n"
            f"Attendance : {student.get('attendance', '')}%\n"
            f"Supplies   : {student.get('supplies', '')}\n"
            f"Result     : {student.get('status', '')}\n\n"

            "=================================================="
        )

        report_text.insert(
            tk.END,
            report
        )

        report_text.config(
            state="disabled"
        )

    # =====================================================
    # STUDENT BUTTONS
    # =====================================================

    student_buttons = [

        (
            "My Profile",
            show_profile
        ),

        (
            "My Marks",
            show_marks
        ),

        (
            "My Attendance",
            show_attendance
        ),

        (
            "My Result",
            show_result
        ),

        (
            "My Report Card",
            show_report_card
        ),

        (
            "Logout",
            student_window.destroy
        )
    ]

    for index, (
        text,
        command
    ) in enumerate(
        student_buttons
    ):

        tk.Button(
            button_frame,
            text=text,
            width=25,
            height=2,
            command=command
        ).grid(
            row=index // 2,
            column=index % 2,
            padx=10,
            pady=10
        )


# =========================================================
# STUDENT LOGIN
# =========================================================

def open_student_login():

    window = tk.Toplevel(
        login_window
    )

    window.title(
        "Student Login"
    )

    window.geometry(
        "450x400"
    )

    window.resizable(
        False,
        False
    )

    tk.Label(
        window,
        text="STUDENT LOGIN",
        font=("Arial", 22, "bold")
    ).pack(pady=25)

    tk.Label(
        window,
        text="Student ID"
    ).pack()

    student_id_entry = tk.Entry(
        window,
        width=35
    )

    student_id_entry.pack(
        pady=8
    )

    tk.Label(
        window,
        text="Password"
    ).pack()

    password_entry = tk.Entry(
        window,
        width=35,
        show="*"
    )

    password_entry.pack(
        pady=8
    )

    def student_login():

        student_id = (
            student_id_entry
            .get()
            .strip()
        )

        password = (
            password_entry
            .get()
            .strip()
        )

        students = load_students()

        for student in students:

            if (

                str(
                    student.get(
                        "student_id",
                        ""
                    )
                ) == student_id

                and

                str(
                    student.get(
                        "password",
                        ""
                    )
                ) == password
            ):

                messagebox.showinfo(
                    "Success",
                    f"Welcome {student.get('name', '')}!"
                )

                window.destroy()

                open_student_dashboard(
                    student
                )

                return

        messagebox.showerror(
            "Login Failed",
            "Invalid Student ID or Password."
        )

    tk.Button(
        window,
        text="Student Login",
        width=25,
        height=2,
        command=student_login
    ).pack(
        pady=20
    )

    tk.Button(
        window,
        text="Close",
        width=25,
        command=window.destroy
    ).pack()


# =========================================================
# ADMIN LOGIN
# =========================================================

def admin_login():

    username = (
        username_entry
        .get()
        .strip()
    )

    password = (
        password_entry
        .get()
        .strip()
    )

    if (

        username == "admin"

        and

        password == "admin123"
    ):

        messagebox.showinfo(
            "Login Successful",
            "Welcome Admin!"
        )

        login_window.withdraw()

        open_admin_dashboard()

    else:

        messagebox.showerror(
            "Login Failed",
            "Invalid Admin Username or Password."
        )


# =========================================================
# MAIN LOGIN WINDOW
# =========================================================

login_window = tk.Tk()

login_window.title(
    "Student Management System"
)

login_window.geometry(
    "500x550"
)

login_window.resizable(
    False,
    False
)

tk.Label(
    login_window,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 22, "bold")
).pack(
    pady=30
)

tk.Label(
    login_window,
    text="LOGIN",
    font=("Arial", 18, "bold")
).pack(
    pady=10
)

tk.Label(
    login_window,
    text="Username"
).pack(
    pady=5
)

username_entry = tk.Entry(
    login_window,
    width=35
)

username_entry.pack(
    pady=5
)

tk.Label(
    login_window,
    text="Password"
).pack(
    pady=5
)

password_entry = tk.Entry(
    login_window,
    width=35,
    show="*"
)

password_entry.pack(
    pady=5
)


# =========================================================
# ADMIN LOGIN BUTTON
# =========================================================

tk.Button(
    login_window,
    text="Admin Login",
    width=25,
    height=2,
    command=admin_login
).pack(
    pady=20
)


# =========================================================
# STUDENT LOGIN BUTTON
# =========================================================

tk.Button(
    login_window,
    text="Student Login",
    width=25,
    height=2,
    command=open_student_login
).pack(
    pady=5
)


# =========================================================
# EXIT BUTTON
# =========================================================

tk.Button(
    login_window,
    text="Exit",
    width=25,
    height=2,
    command=login_window.destroy
).pack(
    pady=15
)


# =========================================================
# START APPLICATION
# =========================================================

login_window.mainloop()

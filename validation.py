import re


# =====================================================
# STUDENT ID VALIDATION
# =====================================================

def validate_student_id(student_id):

    student_id = str(student_id).strip()

    if not student_id:

        return False

    return True


# =====================================================
# NAME VALIDATION
# =====================================================

def validate_name(name):

    name = str(name).strip()

    if not name:

        return False

    if not re.fullmatch(
        r"[A-Za-z ]+",
        name
    ):

        return False

    return True


# =====================================================
# EMAIL VALIDATION
# =====================================================

def validate_email(email):

    email = str(email).strip()

    pattern = (
        r"^[A-Za-z0-9._%+-]+@"
        r"[A-Za-z0-9.-]+\."
        r"[A-Za-z]{2,}$"
    )

    return bool(
        re.fullmatch(
            pattern,
            email
        )
    )


# =====================================================
# PASSWORD VALIDATION
# =====================================================

def validate_password(password):

    password = str(password).strip()

    if len(password) < 6:

        return False

    return True


# =====================================================
# MOBILE VALIDATION
# =====================================================

def validate_mobile(mobile):

    mobile = str(mobile).strip()

    return bool(
        re.fullmatch(
            r"[0-9]{10}",
            mobile
        )
    )


# =====================================================
# AGE VALIDATION
# =====================================================

def validate_age(age):

    try:

        age = int(age)

        return 15 <= age <= 60

    except ValueError:

        return False


# =====================================================
# SEMESTER VALIDATION
# =====================================================

def validate_semester(semester):

    try:

        semester = int(semester)

        return 1 <= semester <= 8

    except ValueError:

        return False


# =====================================================
# YEAR VALIDATION
# =====================================================

def validate_year(year):

    try:

        year = int(year)

        return 1 <= year <= 4

    except ValueError:

        return False


# =====================================================
# MARKS VALIDATION
# =====================================================

def validate_marks(marks):

    try:

        marks = float(marks)

        return 0 <= marks <= 100

    except ValueError:

        return False


# =====================================================
# CGPA VALIDATION
# =====================================================

def validate_cgpa(cgpa):

    try:

        cgpa = float(cgpa)

        return 0 <= cgpa <= 10

    except ValueError:

        return False


# =====================================================
# ATTENDANCE VALIDATION
# =====================================================

def validate_attendance(attendance):

    try:

        attendance = float(attendance)

        return 0 <= attendance <= 100

    except ValueError:

        return False


# =====================================================
# SUPPLIES VALIDATION
# =====================================================

def validate_supplies(supplies):

    try:

        supplies = int(supplies)

        return supplies >= 0

    except ValueError:

        return False


# =====================================================
# PASS OUT YEAR VALIDATION
# =====================================================

def validate_pass_out_year(year):

    try:

        year = int(year)

        return 2020 <= year <= 2100

    except ValueError:

        return False


# =====================================================
# GRADE CALCULATION
# =====================================================

def calculate_grade(marks):

    marks = float(marks)

    if marks >= 90:

        return "A+"

    elif marks >= 80:

        return "A"

    elif marks >= 70:

        return "B"

    elif marks >= 60:

        return "C"

    elif marks >= 50:

        return "D"

    elif marks >= 40:

        return "E"

    else:

        return "F"


# =====================================================
# RESULT CALCULATION
# =====================================================

def calculate_result(
    marks,
    attendance,
    supplies
):

    marks = float(marks)

    attendance = float(attendance)

    supplies = int(supplies)

    if marks < 40:

        return "Fail"

    if attendance < 75:

        return "Fail"

    if supplies > 0:

        return "Fail"

    return "Pass"

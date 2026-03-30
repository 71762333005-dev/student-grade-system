from student import Student
from grade import calculate_grade
from utils import validate_marks

def get_student_result(name, marks):
    validate_marks(marks)
    student = Student(name, marks)
    avg = student.average()
    grade = calculate_grade(avg)
    return {"name": name, "average": avg, "grade": grade}

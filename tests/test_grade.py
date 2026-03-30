from grade import calculate_grade

def test_grade_A():
    assert calculate_grade(95) == "A"

def test_grade_fail():
    assert calculate_grade(30) == "Fail"

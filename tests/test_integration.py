from main import get_student_result

def test_full_flow():
    result = get_student_result("John", [80, 90, 100])
    assert result["grade"] == "A"
    assert result["average"] == 90

from student import Student
import pytest

def test_average():
    s = Student("John", [80, 90, 100])
    assert s.average() == 90

def test_invalid_name():
    with pytest.raises(ValueError):
        Student("", [80, 90])

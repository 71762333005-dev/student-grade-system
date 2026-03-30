class Student:
    def __init__(self, name, marks):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

def validate_marks(marks):
    if not marks:
        raise ValueError("Marks list cannot be empty")

    for m in marks:
        if m < 0 or m > 100:
            raise ValueError("Invalid marks")
    return True

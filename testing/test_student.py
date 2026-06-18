from student.student import Student

def test_student_name():
    student = Student(102, "John", "john@example.com")
    assert student.name == "John"

def test_student_email():
    student = Student(103, "Alice", "alice@example.com")
    assert student.email == "alice@example.com"

def test_student_id():
    student = Student(104, "Bob", "bob@example.com")
    assert student.id == 104

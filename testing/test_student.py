import unittest
from contextlib import redirect_stdout
from io import StringIO

from student.student import Student


class StudentTests(unittest.TestCase):
    def test_init_sets_fields(self):
        student = Student(1, "Alice", "alice@example.com")

        self.assertEqual(student.id, 1)
        self.assertEqual(student.name, "Alice")
        self.assertEqual(student.email, "alice@example.com")

    def test_display_prints_expected_output(self):
        student = Student(1, "Alice", "alice@example.com")
        buffer = StringIO()

        with redirect_stdout(buffer):
            student.display()

        self.assertEqual(
            buffer.getvalue(),
            "ID: 1\nNAME: Alice\nEMAIL: alice@example.com\n",
        )


if __name__ == "__main__":
    unittest.main()

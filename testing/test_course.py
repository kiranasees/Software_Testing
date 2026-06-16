import unittest

from Course.course import course
from student.student import Student


class CourseTests(unittest.TestCase):
    def test_init_uses_enrolled_students(self):
        existing = [Student(2, "Bob", "bob@example.com")]

        c = course("Math", 101, "Algebra", 2, existing)

        self.assertEqual(c.enrolled_students, existing)
        self.assertEqual(c.name, "Math")
        self.assertEqual(c.id, 101)
        self.assertEqual(c.description, "Algebra")
        self.assertEqual(c.max_seats, 2)

    def test_enroll_stops_at_capacity(self):
        c = course("Math", 101, "Algebra", 2, [])
        alice = Student(1, "Alice", "alice@example.com")
        bob = Student(2, "Bob", "bob@example.com")
        carol = Student(3, "Carol", "carol@example.com")

        c.enroll(alice)
        c.enroll(bob)
        c.enroll(carol)

        self.assertEqual([student.name for student in c.enrolled_students], ["Alice", "Bob"])
        self.assertTrue(c.isFull())
        self.assertEqual(c.getEnrolledCount(), 2)

    def test_is_full_false_before_capacity(self):
        c = course("Math", 101, "Algebra", 2, [])

        self.assertFalse(c.isFull())
        self.assertEqual(c.getEnrolledCount(), 0)


if __name__ == "__main__":
    unittest.main()

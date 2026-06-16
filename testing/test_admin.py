import unittest

from Admin.admin import Admin
from Course.course import course


class AdminTests(unittest.TestCase):
    def test_add_course_and_get_course(self):
        admin = Admin()
        math = course("Math", 101, "Algebra", 2, [])
        science = course("Science", 102, "Biology", 1, [])

        self.assertEqual(admin.get_course(), [])

        admin.add_course(math)
        admin.add_course(science)

        self.assertEqual(admin.get_course(), [math, science])


if __name__ == "__main__":
    unittest.main()

class Admin:
    def __init__(self):
        self.course = []
    def add_course(self,course):
        self.course.append(course)
    def get_course(self):
        return self.course


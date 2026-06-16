class course:
    def __init__(self,name,id,description,max_seats,enrolled_students):
        self.name = name
        self.id = id
        self.description = description
        self.max_seats = max_seats
        self.enrolled_students = list(enrolled_students) if enrolled_students is not None else []
    def enroll(self, student):
        if not self.isFull():
            self.enrolled_students.append(student)
    def isFull(self):
        return len(self.enrolled_students) >= self.max_seats
    def getEnrolledCount(self):
        return len(self.enrolled_students)

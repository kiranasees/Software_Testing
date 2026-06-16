class Student:
    def __init__(self,id,name,email):
        self.name = name
        self.id = id
        self.email = email

    def display(self):
        print("ID:", self.id)
        print("NAME:", self.name)
        print("EMAIL:", self.email)
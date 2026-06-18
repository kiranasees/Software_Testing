from Admin.admin import Admin   # change to "from admin import Admin" if needed

def test_init():
    admin = Admin()
    assert admin.course == []

def test_add_course():
    admin = Admin()
    admin.add_course("Math")

    assert admin.course == ["Math"]
    assert len(admin.course) == 1

def test_get_course():
    admin = Admin()
    admin.add_course("Science")
    admin.add_course("English")

    assert admin.get_course() == ["Science", "English"]

def test_update_course():
    admin = Admin()

    admin.add_course("Math")
    admin.add_course("Science")

    admin.update_course(0, "Physics")

    assert admin.course == ["Physics", "Science"]
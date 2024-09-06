import pytest

from src.school import Classroom, Teacher, Student, TooManyStudents

# Helper functions to create Hogwarts characters
def create_teacher(name):
    return Teacher(name)

def create_student(name):
    return Student(name)

def test_classroom_initialization():
    dumbledore = create_teacher("Albus Dumbledore")
    harry = create_student("Harry Potter")
    potions_class = Classroom(dumbledore, [harry], "Potions")

    assert potions_class.teacher.name == "Albus Dumbledore"
    assert len(potions_class.students) == 1
    assert potions_class.course_title == "Potions"

def test_add_student():
    mcgonagall = create_teacher("Minerva McGonagall")
    ron = create_student("Ron Weasley")
    classroom = Classroom(mcgonagall, [], "Transfiguration")

    classroom.add_student(ron)

    assert len(classroom.students) == 1
    assert classroom.students[0].name == "Ron Weasley"

def test_add_student_limit():
    snape = create_teacher("Severus Snape")
    
    classroom = Classroom(snape, [], "Dark Arts")
    for i in range(10):
        classroom.add_student(create_student(f"Student {i+2}"))
    with pytest.raises(TooManyStudents):
        classroom.add_student(create_student("Extra Student"))

def test_remove_student():
    lupin = create_teacher("Remus Lupin")
    hermione = create_student("Hermione Granger")
    classroom = Classroom(lupin, [hermione], "Defense Against the Dark Arts")

    classroom.remove_student(hermione)

    assert len(classroom.students) == 0

def test_change_teacher():
    bridge = create_teacher("Filius Flitwick")
    sprout = create_teacher("Pomona Sprout")
    harry = create_student("Harry Potter")
    classroom = Classroom(bridge, [harry], "Herbology")

    classroom.change_teacher(sprout)

    assert classroom.teacher.name == "Pomona Sprout"

# To run the tests, use the following command in the terminal:
# pytest test_classroom.py
from homework5.task1 import Homework, Student, Teacher


def test_teacher_init():
    """initialization check"""
    teacher = Teacher("Daniil", "Shadrin")
    assert teacher.first_name == "Daniil"
    assert teacher.last_name == "Shadrin"


def test_student_init():
    """initialization check"""
    student = Student("Roman", "Petrov")
    assert student.first_name == "Roman"
    assert student.last_name == "Petrov"


def test_homework_init_and_create_homework():
    """check initialization and create_homework methods"""
    teacher = Teacher("Daniil", "Shadrin")
    expired_homework = teacher.create_homework("Learn functions", 0)
    assert isinstance(expired_homework, Homework)


def test_student_do_homework():
    """check that is_active method Homework class"""
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    assert student.do_homework(oop_homework)
    math_homework = create_homework_too("learn multiply table", 0)
    assert not student.do_homework(math_homework)

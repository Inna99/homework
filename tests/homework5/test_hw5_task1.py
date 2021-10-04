import datetime

from homework5.task1 import Student, Teacher


def test_teacher_init():
    """initialization check"""
    teacher = Teacher("Daniil", "Shadrin")
    assert teacher.last_name == "Daniil"


def test_student_init():
    """initialization check"""
    student = Student("Roman", "Petrov")
    assert student.first_name == "Petrov"


def test_homework_init_and_create_homework():
    """check initialization and create_homework methods"""
    teacher = Teacher("Daniil", "Shadrin")
    expired_homework = teacher.create_homework("Learn functions", 0)
    assert isinstance(expired_homework.created, datetime.datetime)


def test_student_do_homework():
    """check that is_active method Homework class"""
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    assert student.do_homework(oop_homework)

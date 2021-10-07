import pytest

from homework6.task2 import DeadlineError, HomeworkResult, Student, Teacher


@pytest.mark.xfail(raises=TypeError)
def test_homework_result_raises_exeption():
    """calling an exception when creating an instance of a class  """
    good_student = Student("Lev", "Sokolov")
    HomeworkResult(good_student, "fff", "Solution")


@pytest.mark.xfail(raises=DeadlineError)
def test_create_homework_raises_exeption():
    """calling an exception when creating an instance of a class"""
    opp_teacher = Teacher("Daniil", "Shadrin")
    epam_hw = opp_teacher.create_homework("Do hw6", 0)
    lazy_student = Student("Roman", "Petrov")
    lazy_student.do_homework(epam_hw, "done")


def test_create_homework_done():
    """correct creation of a class instance"""
    opp_teacher = Teacher("Daniil", "Shadrin")
    epam_hw = opp_teacher.create_homework("Do hw6", 5)
    lazy_student = Student("Roman", "Petrov")
    result_3 = lazy_student.do_homework(epam_hw, "done")
    assert isinstance(result_3, HomeworkResult)


def test_check_homework():
    """after checking, the homework is recorded in homework_done"""
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")
    good_student = Student("Lev", "Sokolov")
    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)
    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    check = opp_teacher.check_homework(result_1)
    assert check

    temp_1 = opp_teacher.homework_done
    advanced_python_teacher.check_homework(result_2)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

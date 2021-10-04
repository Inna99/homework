"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class Homework:
    def __init__(self, text: str, deadline: datetime.timedelta):
        self.text = text
        self.deadline = deadline
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        now = datetime.datetime.now()
        if self.created + self.deadline > now:
            return True
        else:
            return False


class Person:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name


class Student(Person):
    def __init__(self, last_name: str, first_name: str):
        super().__init__(last_name, first_name)

    def do_homework(self, homework: Homework, solution: str):
        if homework.is_active():
            return HomeworkResult(self, homework=homework, solution=solution)
        else:
            raise DeadlineError("You are late")


class DeadlineError(Exception):
    def __init__(self, text):
        self.txt = text


class HomeworkResult:
    def __init__(self, author: Student, homework: Homework, solution: str):
        #  homework - для объекта Homework, если передан не этот класс -  выкинуть
        #     подходящие по смыслу исключение с сообщением:
        #     'You gave a not Homework object'
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()


class Teacher(Person):
    def __init__(self, last_name: str, first_name: str):
        super().__init__(last_name, first_name)
        # global homework_done
        # self.homework_done = homework_done

    @staticmethod
    def create_homework(text, days):
        return Homework(text, datetime.timedelta(days))

    def check_homework(self, hw_result: HomeworkResult):
        if len(hw_result.solution) > 5:
            homework_done[hw_result.homework].append(hw_result)
            return True
        else:
            return False

    def reset_results(self, *args):
        if isinstance(args[0], Homework):
            homework_done.pop(args[0], "homework")
        # если ничего не передавать,
        #     то полностью обнулит homework_done.
        # elif not args:
        #     del homework_done


if __name__ == "__main__":
    homework_done = defaultdict(list)

    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")
    print(opp_teacher)
    print(advanced_python_teacher)

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)
    print(oop_hw, docs_hw)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    print("1. ", result_1)
    print("2. ", result_2)
    print("3. ", result_3)
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print("There was an exception here")
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    # opp_teacher.check_homework(result_2)
    # opp_teacher.check_homework(result_3)
    #
    # print(Teacher.homework_done[oop_hw])
    # Teacher.reset_results()





# if __name__ == '__main__':
#     opp_teacher = Teacher('Daniil', 'Shadrin')
#     advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')
#
#     lazy_student = Student('Roman', 'Petrov')
#     good_student = Student('Lev', 'Sokolov')
#
#     oop_hw = opp_teacher.create_homework('Learn OOP', 1)
#     docs_hw = opp_teacher.create_homework('Read docs', 5)
#
#     result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
#     result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
#     result_3 = lazy_student.do_homework(docs_hw, 'done')
#     try:
#         result_4 = HomeworkResult(good_student, "fff", "Solution")
#     except Exception:
#         print('There was an exception here')
#     opp_teacher.check_homework(result_1)
#     temp_1 = opp_teacher.homework_done
#
#     advanced_python_teacher.check_homework(result_1)
#     temp_2 = Teacher.homework_done
#     assert temp_1 == temp_2
#
#     opp_teacher.check_homework(result_2)
#     opp_teacher.check_homework(result_3)
#
#     print(Teacher.homework_done[oop_hw])
#     Teacher.reset_results()


"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""
import logging


def instances_counter(cls):
    """decorator for counting the number of objects of the class"""
    class NewCls:
        _count_objects = 0

        # def __new__(cls, *args, **kwargs):
        #     cls._count_objects += 1
        #     return super(NewCls, cls).__new__(cls)

        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)
            NewCls._count_objects += 1

        def __getattribute__(self, attr_name):
            try:
                exist_attr = super().__getattribute__(attr_name)
            except AttributeError:
                logging.info("the requested attribute is an attribute of the source class")
            else:
                return exist_attr

            return self._obj.__getattribute__(attr_name)

        @classmethod
        def get_created_instances(cls):
            return cls._count_objects

        @classmethod
        def reset_instances_counter(cls):
            save_count = cls._count_objects
            cls._count_objects = 0
            return save_count

    return NewCls


@instances_counter
class User:
    pass


if __name__ == '__main__':
    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3



#
# #  мои попытки написать декоратор
# def instances_counter(cls):
#     # def timeit_all_methods(cls):
#     class NewCls:
#         def __init__(self, *args, **kwargs):
#             # проксируем полностью создание класса
#             # как создали этот NewCls, также создадим и декорируемый класс
#             self._obj = cls(*args, **kwargs)
#
#         def get_created_instances():
#             print("get_created_instances")
#
#         def reset_instances_counter(self):
#             print("reset_instances_counter")
#
#         def __getattribute__(self, s):
#             try:
#                 # папа, у меня есть атрибут s?
#                 x = super().__getattribute__(s)
#             except AttributeError:
#                 # нет сынок, это не твой атрибут
#                 pass
#             else:
#                 # да сынок, это твое
#                 return x
#             # объект, значит у тебя должен быть атрибут s
#             attr = self._obj.__getattribute__(s)
#             # метод ли он?
#             # if isinstance(attr, type(self.__init__)):
#             #     # да, обернуть его в измеритель времени
#             #     return timeit(attr)
#             # else:
#             #     # не метод, что-то другое
#             #     return attr
#
#     return NewCls


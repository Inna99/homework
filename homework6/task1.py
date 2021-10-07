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
                logging.info(
                    "the requested attribute is an attribute of the source class"
                )
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


if __name__ == "__main__":
    User.get_created_instances()  # type: ignore
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # type: ignore
    user.reset_instances_counter()  # type: ignore

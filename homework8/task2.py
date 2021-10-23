import sqlite3
from os import path


class TableData:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def __len__(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * from {self.table_name}")
        data = cursor.fetchall()
        conn.close()
        return len(data)

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise TypeError
        else:
            conn = sqlite3.connect(self.database_name)
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * from {self.table_name} where name=:name", {"name": item}
            )
            data = cursor.fetchall()
            conn.close()
            if bool(data):
                return data
            else:
                raise KeyError

    def __iter__(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * from {self.table_name}")
        yield cursor.fetchall()
        conn.close()

    def __contains__(self, item):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT * from {self.table_name} where name=:name", {"name": item}
        )
        data = cursor.fetchall()
        conn.close()
        return bool(data)


if __name__ == "__main__":  # pragma: no cover
    filename = path.join(path.dirname(__file__), "example.sqlite")
    presidents = TableData(database_name=filename, table_name="presidents")
    print(presidents["Yeltsin"])
    print(presidents["Popov"])
    print(presidents[5])

    print(len(presidents))
    print("Yeltsin" in presidents)
    for president in presidents:
        print(president)

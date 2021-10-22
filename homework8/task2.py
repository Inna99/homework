import sqlite3


class TableData(dict):
    def __init__(self, database_name, table_name):
        super().__init__()
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * from {table_name}")
        for line in cursor.fetchall():
            president, value, country = line
            self.__setattr__(president, [president, value, country])
        conn.close()

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':  # pragma: no cover
    presidents = TableData(database_name='example.sqlite', table_name='presidents')
    print(presidents)
    print(presidents['Yeltsin'])
    print(len(presidents))
    print('Yeltsin' in presidents)
    for president in presidents:
        print(president)

# import sqlite3
# conn = sqlite3.connect('example_test.sqlite')
# cursor = conn.cursor()
# presidents = "presidents"
# cursor.execute(f"SELECT * from {presidents}")
# data = cursor.fetchall()  # will get all records with this name. You can also use .fetchone() to get one record.
# print(data)

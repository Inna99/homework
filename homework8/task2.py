import sqlite3

# conn = sqlite3.connect('example.sqlite')
# cursor = conn.cursor()
# cursor.execute('SELECT * from presidents')
# data = cursor.fetchall()  # will be a list with data.
# print(data)


class TableData(dict):
    def __init__(self, db_name, table):
        super().__init__()
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * from ' + table)
        data = cursor.fetchall()  # will be a list with data.
        print(data)
        for line in data:
            president, value, country = line
            self.__setattr__(president, [value, country])

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':  # pragma: no cover
    storage = TableData('example.sqlite', 'presidents')
    print(storage['Yeltsin'])

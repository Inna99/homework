import sqlite3

# conn = sqlite3.connect('example.sqlite')
# cursor = conn.cursor()
# cursor.execute('SELECT * from presidents')
# data = cursor.fetchall()  # will be a list with data.
# print(data)


class TableData(dict):
    def __init__(self, database_name, table_name):
        super().__init__()
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * from ' + table_name)
        data = cursor.fetchall()  # will be a list with data.
        for line in data:
            president, value, country = line
            self.__setattr__(president, [president, value, country])

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':  # pragma: no cover
    presidents = TableData(database_name='example.sqlite', table_name='presidents')
    print(presidents)
    # print(presidents['Yeltsin'])
    # print(len(presidents))
    # print('Yeltsin' in presidents)
    # for president in presidents:
    #     print(president['name'])

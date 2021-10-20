class KeyValueStorage(dict):
    def __init__(self, path_to_file):
        super().__init__()
        with open(path_to_file, 'r') as f:
            for line in f. readlines():
                key, value = line.rstrip().split('=')
                if value.isdigit():
                    self.__setattr__(key, int(value))
                else:
                    self.__setattr__(key, value)

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':  # pragma: no cover
    storage = KeyValueStorage('task1.txt')
    print(storage)
    print(storage['1'])
    print(storage.song)
    print(storage.power)

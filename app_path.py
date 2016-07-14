class Path:
    def __init__(self, app_id):
        self.app = app_id
        self.__path = []

    def append(self, lst_id):
        self.__path.append(lst_id)

    def pop(self):
        poped = self.__path[-1]
        del self.__path[-1]
        return poped

    def __len__(self):
        return len(self.__path)

    def __getitem__(self, i):
        return self.__path[i]

    def __repr__(self):
        return str(self.__path)

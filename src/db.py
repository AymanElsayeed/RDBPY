import sqlite3


class Db:

    _shared_data = {}

    def __init__(self, name):
        self.name = name
        if self.name in self._shared_data:
            self.connection, self.cursor = self._shared_data.get(self.name)
        else:
            self.connection = sqlite3.connect(self.name)
            self.cursor = self.connection.cursor()
            self._shared_data[self.name] = (self.connection, self.cursor)

    def __str__(self):
        return str(self._shared_data)

    def __del__(self):
        self.connection.close()
        self._shared_data.pop(self.name)

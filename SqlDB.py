import sqlite3


class DAO(object):
    def __init__(self):
        self.filename = 'sqlite.db'
        self.connect = sqlite3.connect(self.filename)
        self.cursor = self.connect.cursor()
        sql = ("CREATE TABLE IF NOT EXISTS phonebook (\n"
               + " name text PRIMARY KEY,\n"
               + " number text NOT NULL\n"
               + ");")
        self.cursor.execute(sql)

    def put(self, name, number):
        if self.get(name) is None:
            sql = "INSERT INTO phonebook VALUES('{}', '{}');".format(
                name, number)
            self.cursor.execute(sql)
        else:
            self.edit(name, number)

        self.connect.commit()

    def get(self, name):
        sql = "SELECT number from phonebook where name = '{}';".format(name)
        result = self.cursor.execute(sql)
        fetch = result.fetchone()
        self.connect.commit()
        if fetch is None:
            return None
        return fetch[0]

    def delete(self, name):
        sql = "DELETE from phonebook where name = '{}';".format(name)
        self.cursor.execute(sql)
        self.connect.commit()

    def edit(self, name, number):
        if self.get(name) is None:
            self.put(name, number)
        else:
            sql = "UPDATE phonebook SET number = '{}' where name = '{}';".format(
                number, name)
            self.cursor.execute(sql)
        self.connect.commit()

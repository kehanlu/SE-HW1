import csv


class DAO(object):

    def __init__(self):
        self.filename = 'plaintextDB.txt'
        open(self.filename, 'a+')

    def put(self, name, number):
        if self.get(name) is None:
            with open(self.filename, 'a+') as f:
                writer = csv.writer(f)
                writer.writerow([name, number])
        else:
            self.edit(name, number)

    def get(self, name):
        with open(self.filename, 'r+') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == name:
                    return row[1]
            else:
                return None

    def delete(self, name):
        with open(self.filename, 'r+') as f:
            reader = list(csv.reader(f))

        with open(self.filename, 'w+') as f:
            writer = csv.writer(f)
            for row in reader:
                if row[0] != name:
                    writer.writerow([row[0], row[1]])

    def edit(self, name, number):
        self.delete(name)
        self.put(name, number)

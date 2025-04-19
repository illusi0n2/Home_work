class Library:
    def __init__(self):
        self._hall = []

    def add_hall(self, hall_name):
        self._hall.append(Hall(hall_name))

class Hall:
    def __init__(self, hall_name):
        self._hallName = hall_name
        self._bookcase = []
        for i in range(1, 11):
           self._bookcase.append(Bookcase(i))

    def __str__(self):
        return self._hallName

    def __repr__(self):
        return self.__str__()


class Bookcase:
    def __init__(self, number):
        self._bookcaseNumber = number
        self._bookcaseShelf = []
        for i in range(1, 11):
            self._bookcaseShelf.append(Shelf(i))

    def __str__(self):
        return f'Шкаф №{self._bookcaseNumber}'

    def __repr__(self):
        return self.__str__()


class Shelf:
    def __init__(self, shelf_number):
        self._book_places = []
        self._shelfNumber = shelf_number
        for i in  range (1,11):
            self._book_places.append(i)

    def __str__(self):
        return f'Полка №{self._shelfNumber}'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    lib = Library()
    lib.add_hall('Зал 1')
    lib.add_hall('Зал 2')
    print(len(lib._hall[0]._bookcase[2]._bookcaseShelf))

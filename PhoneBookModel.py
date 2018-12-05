# from PlaintextDB import DAO
from SqlDB import DAO


class PhoneBookModel(object):
    ADD_NAME_STATE = "ADD_NAME"
    ADD_NUMBER_STATE = "ADD_NUMBER"
    SEARCH_STATE = "SEARCH"
    IDLE_STATE = "IDLE"
    SEARCH_RESULT_STATE = "SEARCH_RESULT"
    ERROR_STATE = "ERROR"
    EXIT_STATE = "EXIT"
    EDIT_NAME_STATE = "EDIT_NAME"
    EDIT_NUMBER_STATE = "EDIT_NUMBER"
    EDIT_RESULT_STATE = "EDIT_RESULT"
    DELETE_STATE = "DELETE_NAME"
    DELETE_RESULT_STATE = "DELETE_RESULT"

    def __init__(self, view):
        self.phonebookview = view
        self.state = "IDLE"
        self.search_result = None
        self.phoneBook = DAO()

    def set_state(self, astate):
        self.state = astate
        self.phonebookview.state_has_changed(self, astate)

    def add_an_entry(self, name, number):
        self.phoneBook.put(name, number)

    def search_phone_number(self, name):
        self.search_result = self.phoneBook.get(name)

    def get_search_result(self):
        return self.search_result

    def edit_data(self, name, number):
        self.phoneBook.edit(name, number)

    def delete_data(self, name):
        self.phoneBook.delete(name)

    def get_state(self):
        return self.state

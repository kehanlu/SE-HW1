from PhoneBookModel import PhoneBookModel


class PhoneBookController(object):

    START_COMMAND = "start"
    QUIT_COMMAND = "quit"
    ADD_COMMAND = "add"
    SEARCH_COMMAND = "search"
    EDIT_COMMAND = "edit"
    DELETE_COMMAND = "delete"

    def __init__(self):
        from PhoneBookView import PhoneBookView
        self.phonebookview = PhoneBookView(self)
        self.phonebookmodel = PhoneBookModel(self.phonebookview)

    def user_has_input(self, user_input):
        current_state = self.phonebookmodel.get_state()
        if len(user_input) > 0:
            if current_state == PhoneBookModel.IDLE_STATE:
                if user_input == PhoneBookController.ADD_COMMAND:
                    self.phonebookmodel.set_state(
                        PhoneBookModel.ADD_NAME_STATE)
                elif user_input == PhoneBookController.SEARCH_COMMAND:
                    self.phonebookmodel.set_state(PhoneBookModel.SEARCH_STATE)
                elif user_input == PhoneBookController.QUIT_COMMAND:
                    self.phonebookmodel.set_state(PhoneBookModel.EXIT_STATE)
                elif user_input == PhoneBookController.EDIT_COMMAND:
                    self.phonebookmodel.set_state(
                        PhoneBookModel.EDIT_NAME_STATE)
                elif user_input == PhoneBookController.DELETE_COMMAND:
                    self.phonebookmodel.set_state(PhoneBookModel.DELETE_STATE)
                else:
                    self.phonebookmodel.set_state(PhoneBookModel.ERROR_STATE)

            elif current_state == PhoneBookModel.ADD_NAME_STATE:
                self.name = user_input
                self.phonebookmodel.set_state(PhoneBookModel.ADD_NUMBER_STATE)

            elif current_state == PhoneBookModel.ADD_NUMBER_STATE:
                self.phonebookmodel.add_an_entry(self.name, user_input)
                self.phonebookmodel.set_state(PhoneBookModel.IDLE_STATE)

            elif current_state == PhoneBookModel.SEARCH_STATE:
                self.phonebookmodel.search_phone_number(user_input)
                self.phonebookmodel.set_state(
                    PhoneBookModel.SEARCH_RESULT_STATE)

            elif current_state == PhoneBookModel.EDIT_NAME_STATE:
                self.name = user_input
                self.phonebookmodel.set_state(PhoneBookModel.EDIT_NUMBER_STATE)

            elif current_state == PhoneBookModel.EDIT_NUMBER_STATE:
                self.phonebookmodel.edit_data(self.name, user_input)
                self.phonebookmodel.set_state(PhoneBookModel.IDLE_STATE)

            elif current_state == PhoneBookModel.DELETE_STATE:
                self.phonebookmodel.delete_data(user_input)
                self.phonebookmodel.set_state(PhoneBookModel.IDLE_STATE)

            elif (current_state == PhoneBookModel.SEARCH_RESULT_STATE or
                  current_state == PhoneBookModel.ERROR_STATE):
                if user_input == PhoneBookController.START_COMMAND:
                    self.phonebookmodel.set_state(PhoneBookModel.IDLE_STATE)
                elif user_input == PhoneBookController.QUIT_COMMAND:
                    self.phonebookmodel.set_state(PhoneBookModel.EXIT_STATE)
                else:
                    self.phonebookmodel.set_state(PhoneBookModel.ERROR_STATE)

            else:
                self.phonebookmodel.set_state(PhoneBookModel.ERROR_STATE)

    def start(self):
        self.phonebookmodel.set_state(PhoneBookModel.IDLE_STATE)
        while not self.phonebookview.finish():
            self.phonebookview.get_user_input()

from PhoneBookController import PhoneBookController
from PhoneBookModel import PhoneBookModel


class PhoneBookView(object):
    ADD_NAME_Q = "Please enter the exact person name"
    ADD_NUMBER_Q = "Please enter the phone number"
    SEARCH_Q = "Please enter the exact person name."
    IDLE_Q = ("Please enter your choice of action, \"" +
              PhoneBookController.ADD_COMMAND +
              "\" to add a phone entry or \"" +
              PhoneBookController.SEARCH_COMMAND +
              "\" to search for a phone number or \"" +
              PhoneBookController.EDIT_COMMAND +
              "\" to edit data or \"" +
              PhoneBookController.DELETE_COMMAND +
              "\" to delete data or \"" +
              PhoneBookController.QUIT_COMMAND +
              "\" to end the application.")

    SEARCH_RESULT_Q = (" - This is the located phone number.   Enter \"" +
                       PhoneBookController.START_COMMAND +
                       "\" to do more with the application or \"" +
                       PhoneBookController.QUIT_COMMAND + "\" to end the application.")

    SEARCH_NOT_FOUND_Q = (" Phone number not found.   Enter \"" +
                          PhoneBookController.START_COMMAND +
                          "\" to do more with the application or \"" +
                          PhoneBookController.QUIT_COMMAND + "\" to end the application.")

    ERROR_Q = ("You've entered an invalid choice.  Enter \"" +
               PhoneBookController.START_COMMAND +
               "\" to do more with the application or \"" +
               PhoneBookController.QUIT_COMMAND + "\" to end the application.")

    EDIT_NAME_Q = "Please enter the exact person name."

    EDIT_NUMBER_Q = "Please enter the phone number."

    DELETE_Q = "Please enter the exact person name."

    def __init__(self, controller):
        self.phonebookcontroller = controller
        self.finish_flag = False

    def finish(self):
        return self.finish_flag

    def state_has_changed(self, model, new_state):
        self.phonebookmodel = model
        self.change_view(new_state)

    def change_view(self, new_state):
        if new_state == PhoneBookModel.IDLE_STATE:
            print(PhoneBookView.IDLE_Q)
        elif new_state == PhoneBookModel.ADD_NAME_STATE:
            print(PhoneBookView.ADD_NAME_Q)
        elif new_state == PhoneBookModel.ADD_NUMBER_STATE:
            print(PhoneBookView.ADD_NUMBER_Q)
        elif new_state == PhoneBookModel.SEARCH_STATE:
            print(PhoneBookView.SEARCH_Q)
        elif new_state == PhoneBookModel.SEARCH_RESULT_STATE:
            result = self.phonebookmodel.get_search_result()
            if result is not None and len(result) > 0:
                print(result + PhoneBookView.SEARCH_RESULT_Q)
            else:
                print(PhoneBookView.SEARCH_NOT_FOUND_Q)
        elif new_state == PhoneBookModel.ERROR_STATE:
            print(PhoneBookView.ERROR_Q)
        elif new_state == PhoneBookModel.EXIT_STATE:
            print("Bye!")
            self.finish_flag = True
        elif new_state == PhoneBookModel.EDIT_NAME_STATE:
            print(PhoneBookView.EDIT_NAME_Q)
        elif new_state == PhoneBookModel.EDIT_NUMBER_STATE:
            print(PhoneBookView.EDIT_NUMBER_Q)
        elif new_state == PhoneBookModel.DELETE_STATE:
            print(PhoneBookView.DELETE_Q)

    def get_user_input(self):
        inp = input('\n>>> ')
        print('\n')
        self.phonebookcontroller.user_has_input(inp)

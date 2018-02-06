class Account():
    def __init__(self, parent_child, username, account_number, uuid):
        self.__parent_child = parent_child
        self.__username = username
        self.__account_number = account_number
        self.__uuid = uuid

    def get_username(self):
        return self.__username
    def get_account_number(self):
        return self.__account_number
    def get_parent_child(self):
        return self.__parent_child
    def get_uuid(self):
        return self.__uuid

    def set_username(self, username):
        self.__username = username
    def set_account_number(self, account_number):
        self.__account_number = account_number


from datetime import datetime

class Transactions():
    def __init__(self, user_name, goal_name, amount, date_time):

        self.__user_name = user_name
        self.__goal_name = goal_name
        self.__amount = amount
        self.__date_time = date_time

    def get_user_name(self):
        return self.__user_name

    def get_goal_name(self):
        return self.__goal_name

    def get_amount(self):
        return self.__amount

    def get_date_time(self):
        # datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
        myFormat = "%d/%m/%Y %H:%M:%S"

        formatedDate = datetime.strptime( self.__date_time, "%Y-%m-%d %H:%M:%S.%f")
        formatedDate = formatedDate.strftime(myFormat)

        return formatedDate

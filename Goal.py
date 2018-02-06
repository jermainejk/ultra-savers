class Goal():
    def __init__(self, userid,type,setter, goal,amount, duration, startdate,saveamount,status = 'A',val='x',str ='a'):
        self.__userid = userid
        self.__type = type
        self.__setter = setter
        self.__goal = goal
        self.__amount = amount
        self.__duration = duration
        self.__startdate = startdate
        self.__status = status
        self.__val = val
        self.__str = str
        self.__saveamount = saveamount
        self.__transacted_amount = 0

    def get_goal(self):
        return self.__goal
    def get_amount(self):
        return self.__amount
    def get_duration(self):
        return self.__duration
    def get_userid(self):
        return self.__userid
    def get_type(self):
        return self.__type
    def get_setter(self):
        return self.__setter
    def get_str(self):
        return self.__str
    def get_startdate(self):
        return self.__startdate
    def get_transacted_amount(self):
        return self.__transacted_amount

    def get_status(self):
        return self.__status
    def get_val(self):
        return self.__val
    def get_saveamount(self):
        return self.__saveamount


    def set_goal(self,goal):
        self.__goal = goal
    def set_amount(self,amount):
        self.__amount = amount
    def set_duration(self,duration):
        self.__duration = duration
    def set_userid(self,userid):
        self.__userid = userid
    def set_type(self,type):
        self.__type = type
    def set_setter(self,setter):
        self.__setter = setter
    def set_status(self,status):
        self.__status = status
    def set_val(self,val):
        self.__val = val
    def set_str(self,str):
        self.__str = str
    def set_startdate(self,startdate):
        self.__startdate = startdate

    def add_transacted_amount(self, amount):
        if(self.__transacted_amount):
            self.__transacted_amount =  float(self.__transacted_amount) + float(amount)
        else:
            self.__transacted_amount = float(amount)

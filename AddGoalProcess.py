from Goal import Goal
from SavingsGoal import SavingsGoal
import datetime
from datetime import date
today = date.today()
day = today.day #5(number)

def checkerdate(userdate):
    user_file = open('file/addgoals.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        userday = int(list[5])
        difference = day - userday


def processUser(userid):
    usersList = []
    user_file = open('file/addgoals.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        if list[0] == userid:
            s = Goal(list[0], list[1], list[2], list[3], int(list[4]), list[5],list[6],list[7],list[8],list[9],list[10])
            usersList.append(s)
    return usersList


def countUser(userid):
    countList = []
    user_file = open('file/addgoals.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        today = datetime.datetime.now().date()
        if list[0] == userid and list[8] =='A':
            s = Goal(list[0], list[1], list[2], list[3], int(list[4]), list[5],list[6],list[7],list[8],list[9],list[10])
            countList.append(s)
    return countList


def updateUser(userid,setter,goal):
    usersList = []
    user_file = open('file/addgoals.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        status = list[7]
        if list[0] == userid and list[2] == setter and list[3] == goal:
            status = 'D'
        writeline = list[0] + ',' + list[1] + ',' + list[2]+ ',' + list[3]+ ',' + list[4]+ ',' + list[5]+ ','+ list[6]+','+ status + ',' + 'x' + ',' + 'a' + '\n'
        usersList.append(writeline)

    writeuser_file = open('file/addgoals.txt', 'w')
    for userline in usersList:
        writeuser_file.write(userline)

    return usersList

def EditUserGoal(userid,oldsetter,oldgoal, newsetter,newgoal,newamount,newduration):
    usersList = []
    user_file = open('file/addgoals.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        setter = list[2]
        goal = list[3]
        amount = list[4]  #original amount
        duration = list[5]
        print('############')
        print(list[0])
        print(list[2])
        print(list[3])
        print('############')
        if list[0]==userid and list[2]==oldsetter and list[3]==oldgoal:
            print('----------------------')
            print(list[0])
            print(list[2])
            print(list[3])
            print('-------------------------')
            setter = newsetter
            goal = newgoal
            amount = newamount
            duration = newduration
        writeline = list[0] + ',' + list[1] + ',' + setter + ',' + goal +',' + amount +',' + duration + ','+ list[6] + ',' +list[7]+ ','+ 'x' + ',' + 'a' +'\n'
        usersList.append(writeline)

    writeuser_file = open('file/addgoals.txt', 'w')
    for userline in usersList:
        writeuser_file.write(userline)
    writeuser_file.close()


def processSavings(userid):
    usersList = []
    user_file = open('file/savegoals.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        if list[0] == userid:
            s = SavingsGoal(list[0], list[1], list[2], list[3], list[4], int(list[5]))
            usersList.append(s)
    return usersList


def registerNewUser(name,type,setter,goal,amount,duration,startdate, status='A',val = 'x',str = 'a'):
    userdata = name + ',' + type + ','+ setter + ',' + goal + ',' + amount + ',' + duration + ','+ startdate+',' + '0' +','+status + ','+ val +',' + str + '\n'
    user_file = open('file/addgoals.txt', 'a')
    user_file.write(userdata)


def updateCurrentUser(name,type,setter,goal,amount,duration):
    userdata = name + ',' + type + ','+ setter + ',' + goal + ',' + amount + ',' + duration + '\n'
    user_file = open('file/addgoals.txt', 'a')
    user_file.write(userdata)

def userslist():
    userlist = []
    user = open('file/savegoals.txt','r')
    for userid in user:
        list = userid.split(',')
        if list[0] not in userlist:
            userlist.append(list[0])
    return userlist


def checkdate(date):
    user = open('file/savegoals.txt', 'r')
    for userid in user:
        list = userid.split(',')
        ddmmyyyy = list
        if list[2] > date :
            print('Your goal has expired!')
        elif list[2] == date:
            print('Your goal is expiring today!')
        else:
            print('Remember to save up for your goals!')

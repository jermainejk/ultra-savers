from Users import Users
from SpendingLimit import SpendingLimit
from SavingHistory import SavingHistory
from Goal import Goal
from _datetime import datetime

def processUser(name,todayMonth):
    usersList = []
    print(todayMonth)
    print(name)

    user_file = open('file/usersNew.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        savedate = list[5]
        savedateStr = savedate.split('-')
        dd = int(savedateStr[0])
        mm = int(savedateStr[1])
        yy = int(savedateStr[2])
        print(mm)

        if list[0]==name and mm==todayMonth:
            goal = float(list[4])

            #current month
            #saveCurrent = float(list[3])

            saveTotal = searchHistoryforTotalSaving(list[0],list[6])
            howmuchMore = goal - saveTotal
            howmuchMore = '%.2f' %howmuchMore

            monthly = 0.05 / 12
            convert = monthly / 100
            interest = saveTotal * convert
            i = '%.2f' %interest

            s = Users(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],howmuchMore,i,list[8])
            usersList.append(s)
    return usersList


def searchHistoryforTotalSaving(name,item):
    sh_file = open('file/usersNew.txt', 'r')
    totalamount = 0
    for shlist in sh_file:
        list = shlist.split(',')
        if list[0] == name and list[6] == item:
            totalamount = totalamount + float(list[3])
    return totalamount

def retrieve(name,todayMonth):
    rList = []
    r_file = open('file/addgoals.txt','r')
    for rlist in r_file:
        list = rlist.split(',')
        savedate = list[6]
        savedateStr = savedate.split('-')
        dd = int(savedateStr[0])
        mm = int(savedateStr[1])
        yy = int(savedateStr[2])
        print(mm)

        if list[0] == name and mm == todayMonth:
            goal = float(list[4])

            saveTotal = retrieveHistory(list[0], list[5])
            howmuchMore = goal - saveTotal
            howmuchMore = '%.2f' % howmuchMore

            monthly = 0.05 / 12
            convert = monthly / 100
            interest = saveTotal * convert
            i = '%.2f' % interest

            a = '%.2f' %goal

            s = Goal(list[0], list[1], list[2], list[3], a, list[5], list[6], list[7], howmuchMore, i, list[8],list[9],list[10])
            rList.append(s)
    return rList

def retrieveHistory(name,item):
    rh_file = open('file/addgoals.txt', 'r')
    totalamount = 0
    for rhlist in rh_file:
        list = rhlist.split(',')
        if list[0] == name and list[3] == item:
            totalamount = totalamount + float(list[5])
    return totalamount


def limit(name,todayMonth):
    limitList = []
    limit_file = open('file/spendingLimit.txt', 'r')
    for limitlist in limit_file:
        list = limitlist.split(',')
        if list[0]==name and int(list[2])==todayMonth:
            s = SpendingLimit(list[0],list[1],list[2],list[3],list[4])
            limitList.append(s)

    return limitList

def over(name,todayMonth):

    o_file = open('file/spendingLimit.txt','r')
    for ofile in o_file:
        list = ofile.split(',')
        if list[0]==name and int(list[2])==todayMonth:
            limit = float(list[3])
            spend = float(list[4])

            spend -= limit
            o = '%.2f' %spend
            return o


def reward(name,todayMonth):
    r_file = open('file/users.txt','r')
    for rfile in r_file:
        list = rfile.split(',')
        if list[0] == name and list[5] == todayMonth:
            saved = float(list[3])
            if saved == 1000:
                r = 5

def displayHistory(name,goalType):
    today = datetime.today()
    todayDT = datetime(today.year, today.month, today.day)

    history = []
    d_file = open('file/savinghistory.txt','r')

    for dlist in d_file:
        list = dlist.split(',')
        saveDate = list[7]
        saveDateStr = saveDate.split('-')
        dd = int(saveDateStr[0])
        mm = int(saveDateStr[1])
        yy = int(saveDateStr[2])
        date = datetime(yy,mm,dd)
        #print(mm)
        print('^^^^^^^^^^^')
        print(list[4])
        print(list[0])
        print(name)
        print(goalType)
        print(date)
        print(todayDT)
        print('^^^^^^^^^^^^^')
        if list[0] == name and list[4] == goalType and date <= todayDT:
            print('@@@@@@@@@@')
            print(list[4])
            print('@@@@@@@@@@')
            h = SavingHistory(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7])
            history.append(h)
    return history

limit("Mary",2)
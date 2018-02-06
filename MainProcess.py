from JUsers import JUsers
from JUsers import Child
from datetime import *

from Goal import Goal

import uuid

from Account import Account
from Relations import Relations
from Transactions import Transactions

months = ["Unknaown","January","Febuary","March","April","May","June","July","August","September","October","November","December"]

now = (datetime.now())
year = (now.year)
month = (months[now.month])
print(month)

def current_Month():
    return month


def get_accounts():
    accounts = open('file/accounts.txt','r')
    accounts_list = []
    for account in accounts:
        account_split = account.replace('\n','').split(',')
        _account = Account(account_split[0], account_split[1], account_split[2], account_split[3])
        accounts_list.append( _account )

    return accounts_list

def set_accounts( accounts ):

    with open('file/accounts.txt', 'w') as file:
        for account in accounts:
            file.write(account.get_parent_child() +","+ account.get_username() +","+ account.get_account_number() +","+ account .get_uuid() + '\n')

def add_transaction( _name, _goal, _amount ):

    transaction = _name + ',' + _goal + ',' + _amount + ',' + str(datetime.now()) + '\n'
    # userdata = username + ',' + account +',' + password +'\n'
    transaction_file = open('file/transactions.txt', 'a')
    transaction_file.write(transaction)

def get_relations():
    relations = open('file/relations.txt', 'r')
    relations_list = []
    for relation in relations:
        relation_split = relation.replace('\n','').split(',')
        relations_list.append( Relations( relation_split[0], relation_split[1] ))
    return relations_list

def get_transactions():
    transactions = open('file/transactions.txt', 'r')
    transactions_list = []

    for record in transactions:
        record_split = record.replace('\n','').split(',')
        transactions_list.append( Transactions( record_split[0], record_split[1], record_split[2], record_split[3] ))

    return transactions_list

def get_goals():
    goals = open('file/addgoals.txt', 'r')
    goals_list = []

    for record in goals:
        list = record.replace('\n','').split(',')
        goals_list.append( Goal(list[0], list[1], list[2], list[3], int(list[4]), list[5],list[6],0 ) )

    return goals_list


def previous_Month():
    return months[now.month-1]

def processUserGoals(userid):
    usersList = []
    user_file = open('file/addgoals.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        if list[0] == userid:
            s = Goal(list[0], list[1], list[2], list[3], int(list[4]), list[5],list[6],0 )
            usersList.append(s)
    return usersList

def processUser(parent):
    usersList = []
    user_file = open('file/child.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        print(list)
        s= Child(list[0], list[1],list[2],list[3],list[4],list[5],int(list[6]))
        if list[0] == parent:
         usersList.append(s)
    return usersList

def processTransaction(parent, month, type='deposit'):
    t_file = open('file/child.txt', 'r')
    total = 0
    for trans in t_file:
        list = trans.split(',')

        if list[0] == parent and list[2] == month:
            total += float(list[6])
    return total

def registerNewUser(username, account, password):
    userdata = username + ',' + account +',' + password +'\n'
    user_file = open('file/login.txt', 'a')
    user_file.write(userdata)

def validate_User(username, password):
    #usersList = []
    user_file =open('file/login.txt','r')
    for ulist in user_file:
        list = ulist.split(',')
        print(list)
        #usersList.append(list)
        if username == list[0] and (password + '\n') == list[2]:
            return True

def registerNewChild(user_name, child_name, bank):
    relationship = user_name+','+child_name+'\n'
    _uuid = uuid.uuid4()
    userdata ='Child'+',' + child_name + ',' +bank+ ',' + str(_uuid) + '\n'

    user_file = open('file/accounts.txt', 'a')
    user_file.write(userdata)

    relations_file = open('file/relations.txt', 'a')
    relations_file.write(relationship)

def registerNewAcc(user_name, name, bank):
    _uuid = uuid.uuid4()
    userdata ='Parent'+','+ name + ',' +bank+ ',' +str(_uuid)+'\n'
    user_file = open('file/accounts.txt', 'a')
    user_file.write(userdata)

    relationship = user_name+','+name+'\n'
    relations_file = open('file/relations.txt', 'a')
    relations_file.write(relationship)

def TEST(name):
    List = []
    user_file = open('file/child.txt', 'r')
    for i in user_file:
        list = i.split(',')
        if list[0] == name:
            List.append(list[4])

    return List

def updateAmount(name, childName, limit):
    with open('file/child.txt', 'r') as file:
        newline = []
        for word in file:
            word = word.strip()
            s = word.split(',')
            if name == s[0] and childName == s[4]:
                print("success x2")
                newline.append(word.replace(s[6], limit))
            else:
                newline.append(word)

    with open('file/child.txt', 'w') as file:
        for line in newline:
            file.write(line + '\n')

def deleteChild(childName):
    temporary_list = []
    user_file = open('file/child.txt', 'r')
    for item in user_file:
        list = item.split(',')
        s = Child(list[0], list[1], list[2], list[3], list[4], list[5], int(list[6]))
        temporary_list.append(s)

    list = []
    for item in temporary_list:
        if item.get_child() != childName:
            s = "%s,%s,%s,%s,%s,%s,%d,\n" %(item.get_parent(),item.get_bank(),item.get_month(),item.get_year(),item.get_child(),item.get_account(),item.get_amount())
            list.append(s)
    user_file = open('file/child.txt','w')
    for i in list:
        user_file.write(i)
    user_file.close()


def diffMonths(prevMonth,currMonth,prevYear,currYear):

    currMonth = datetime.now().month
    currYear = datetime.now().year
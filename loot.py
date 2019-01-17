import sqlite3
import sys



# cursor.execute('INSERT INTO foo (id,username,password) VALUES (?,?,?)',
#                (100,'blah','blah'))
# print(cursor.lastrowid)

lootbag_db = 'lootbag.sql'


class Lootbag():

  def terminalCatch(self, *terminalString):
    if len(terminalString[0]) < 2:
      return "Please add an argument"
    elif len(terminalString[0]) == 2:
      if terminalString[0][1] == "ls":
        return self.kidsWhoGetPressents(terminalString[0])
      else:
        return "Incorrect input"
    elif len(terminalString[0]) == 3:
      if terminalString[0][1] == 'delivered':
        return "Delivered!"
      elif terminalString[0][1] == 'ls' and terminalString[0][2]:
        return "ls and name"
      else:
        return "Incorrect input"
    elif len(terminalString[0]) == 4 :
      if terminalString[0][1] == 'add':
        return self.addToy(terminalString[0])
      elif terminalString[0][1] == 'remove':
        return self.removeToy(terminalString[0])
      else:
        return "Incorect input"
    else:
      return "Too many arguments"

  def addToy(self, termList):
    print(termList)
    return "You added!"

  def removeToy(self, termList):
    print(termList)
    return "You removed :("

  def kidsWhoGetPressents(self, termList):
    print(termList)
    return "You LS'd!"


if __name__ == "__main__":
  loot = Lootbag()
  loot.terminalCatch(sys.argv)
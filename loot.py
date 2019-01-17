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
        return "You LS'd!"
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
        return "You added!"

      elif terminalString[0][1] == 'remove':
        return "You removed :("

      else:
        return "Incorect input"
    else:
      return "Too many arguments"


if __name__ == "__main__":
  loot = Lootbag()
  loot.terminalCatch(sys.argv)
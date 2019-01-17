import sqlite3
import sys



# cursor.execute('INSERT INTO foo (id,username,password) VALUES (?,?,?)',
#                (100,'blah','blah'))
# print(cursor.lastrowid)

lootbag_db = 'lootbag.sql'


class Lootbag():

  def terminalCatch(self, *terminalString):
    print(terminalString)
    if terminalString[0][1] == 'add':
      return "You added!"
    elif terminalString[0][1] == 'remove':
      return "You removed :("
    elif terminalString[0][1] == 'delivered':
      return "Delivered!"
    elif terminalString[0][1] == 'ls' and terminalString[0][2]:
      return "ls and name"
    elif terminalString[0][1] == "ls":
      return "You LS'd!"
    else:
      return "Incorect data"


if __name__ == "__main__":
  loot = Lootbag()
  loot.terminalCatch(sys.argv)
import sqlite3
import sys



# cursor.execute('INSERT INTO foo (id,username,password) VALUES (?,?,?)',
#                (100,'blah','blah'))
# print(cursor.lastrowid)

lootbag_db = '../lootbag.db'


class Lootbag():

  def terminalCatch(self, *terminalTuppleList):
    if len(terminalTuppleList[0]) < 2:
      return "Please add an argument"
    elif len(terminalTuppleList[0]) == 2:
      if terminalTuppleList[0][1] == "ls":
        return self.kidsWhoGetPressents(terminalTuppleList[0])
      else:
        return "Incorrect input"
    elif len(terminalTuppleList[0]) == 3:
      if terminalTuppleList[0][1] == 'delivered':
        return self.toysDelivered(terminalTuppleList[0])
      elif terminalTuppleList[0][1] == 'ls' and terminalTuppleList[0][2]:
        return self.singleKidsPresents(terminalTuppleList[0])
      else:
        return "Incorrect input"
    elif len(terminalTuppleList[0]) == 4 :
      if terminalTuppleList[0][1] == 'add':
        return self.addToy(terminalTuppleList[0])
      elif terminalTuppleList[0][1] == 'remove':
        return self.removeToy(terminalTuppleList[0])
      else:
        return "Incorect input"
    else:
      return "Too many arguments"

  def addToy(self, termList):
    with sqlite3.connect(lootbag_db) as conn:
      cursor = conn.cursor()
      cursor.execute(f'''INSERT INTO Toys
                        SELECT ?, ?, ChildId
                        From Children c
                        WHERE c.Name = "{termList[3]}";''',(None, termList[2] ))


      kids = cursor.fetchall()
      print(kids)
    return "You added!"

  def removeToy(self, termList):
    with sqlite3.connect(lootbag_db) as conn:
      cursor = conn.cursor()

      cursor.execute(f'''INSERT INTO Toys
                          SELECT null, "{termList[2]}", c.ChildId
                          From Children c
                          WHERE c.Name = "{termList[3]}";''')
    return "You removed :("

  def kidsWhoGetPressents(self, termList):
    print(termList)
    with sqlite3.connect(lootbag_db) as conn:
      cursor = conn.cursor()
      cursor.execute('SELECT * FROM Children')
      kids = cursor.fetchall()
      print(kids)
    return "You LS'd!"

  def singleKidsPresents(self, termList):
    print(termList[2])
    with sqlite3.connect(lootbag_db) as conn:
      cursor = conn.cursor()
      cursor.execute(f'''SELECT c.Name, t.ToyName
                        FROM Children c
                        JOIN Toys t on c.ChildId = t.ChildId
                        WHERE Name = "{termList[2]}"''')
      kids = cursor.fetchall()
      print(kids)
    return "ls and name"

  def toysDelivered(self, termList):
    with sqlite3.connect(lootbag_db) as conn:
      cursor = conn.cursor()
      cursor.execute(f'''Update Children
                          set Delivered = 1
                          where Name = "{termList[2]}";''')
      kids = cursor.fetchall()
      print(kids)
    return "Delivered!"

if __name__ == "__main__":
  loot = Lootbag()
  loot.terminalCatch(sys.argv)
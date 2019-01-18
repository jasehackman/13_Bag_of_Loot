import sqlite3
import sys



# cursor.execute('INSERT INTO foo (id,username,password) VALUES (?,?,?)',
#                (100,'blah','blah'))
# print(cursor.lastrowid)

lootbag_db = '../lootbag.db'


class Lootbag():

  def terminalCatch(self, terminalTuppleList):


    '''Filters through comands recieved in the command line '''

    if len(terminalTuppleList) < 2:
      return "Please add an argument"
    elif len(terminalTuppleList) == 2:
      if terminalTuppleList[1] == "ls":
        return self.kidsWhoGetPressents(terminalTuppleList)
      elif terminalTuppleList[1] == "help":
        return self.help()
      else:
        return "Incorrect input"
    elif len(terminalTuppleList) == 3:
      if terminalTuppleList[1] == 'delivered':
        return self.toysDelivered(terminalTuppleList)
      elif terminalTuppleList[1] == 'ls' and terminalTuppleList[2]:
        return self.singleKidsPresents(terminalTuppleList)
      else:
        return "Incorrect input"
    elif len(terminalTuppleList) == 4 :
      if terminalTuppleList[1] == 'add':
        return self.addToy(terminalTuppleList)
      elif terminalTuppleList[1] == 'remove':
        return self.removeToy(terminalTuppleList)
      else:
        return "Incorect input"
    else:
      return "Too many arguments"

  def help(self):
    helping = '''
      to execute:
        python.py ls - Lists all children who will get presents
        python.py ls [kidName] - List presents that kid will get
        python.py add [kidName] [toyName] - adds the toy to the child
        python.py remove [toyName] [kidName] - removes the toy from the child

        '''

    return print(helping)

  def addToy(self, termList):
    '''Adds toys to a child that already exist in the database'''

    with sqlite3.connect(lootbag_db) as conn:
      cursor = conn.cursor()
      try:
        cursor.execute(f'''INSERT INTO Toys
                          SELECT ?, ?, ChildId
                          From Children c
                          WHERE c.Name = "{termList[3]}";''',(None, termList[2] ))
        toy = cursor.lastrowid
        print(toy)
        if toy > 0:
          print("You added a toy!")
        else:
          print("You did not add a toy.")
        return toy

      except sqlite3.OperationalError as err:
                    print("oops", err)

  def doesChildExist(self,childName):
    '''Checks if a child is in the database'''
    with sqlite3.connect(lootbag_db) as conn:
      cursor = conn.cursor()

      cursor.execute(f'''SELECT ChildId
                          FROM Children
                          WHERE Name = "{childName}";''')
      childId = cursor.fetchone()

      return childId

  def doesToyExist(self, toyName, childId):
    '''Checks if a toy is in the database'''
    with sqlite3.connect(lootbag_db) as conn:
      cursor = conn.cursor()

      cursor.execute(f'''SELECT ToyId
                          FROM Toys
                          WHERE ToyName = "{toyName}"
                          AND ChildId = {childId};''')
      toyId = cursor.fetchone()
      return toyId


  def removeToy(self, termList):
    '''Removes a toy from the child and from the database'''

    # Calls funtion to check if a child exists
    childId = self.doesChildExist(termList[2])
    print("HERE", childId)
    if childId == None:
      print("That Child does not exist")
      return childId


    # Calls function to check if toy exist
    toyId = self.doesToyExist(termList[3], childId[0])
    if toyId == None:
      print("That Toy does not exist")
      return toyId


    with sqlite3.connect(lootbag_db) as conn:
      cursor = conn.cursor()
      cursor.execute(f'''DELETE FROM Toys
                          WHERE ToyId = {toyId[0]}
                          AND ChildId = {childId[0]}'''
                        )
    # Checks if the toy has been removed
    isToyThere = self.doesToyExist(termList[3], childId[0])
    if isToyThere == None:
      print("Your toy is deleted")
    else: print("Your toy could not be deleted")

    return isToyThere

  def kidsWhoGetPressents(self, termList):
    '''List the kids who get presents'''

    print(termList)
    with sqlite3.connect(lootbag_db) as conn:
      cursor = conn.cursor()
      cursor.execute('SELECT * FROM Children')
      kids = cursor.fetchall()
      print(kids)
    return "You LS'd!"

  def singleKidsPresents(self, termList):
    '''list the presents the named child will get'''
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
    '''states what toys have been delivered'''
    with sqlite3.connect(lootbag_db) as conn:
      cursor = conn.cursor()
      cursor.execute(f'''Update Children
                          set Delivered = 1
                          where Name = "{termList[2]}";''')
      kids = cursor.fetchall()
      print(kids)
    return "Delivered!"

  def badKid(self, termList):
    '''adds a kid to the naughty list and removes all of their toys'''
    with sqlite3.connect(lootbag_db) as conn:
      cursor = conn.cursor()
      cursor.execute(f'''Select ChildId
                          FROM Children
                          where Name = "{termList[1]}";''')
      kid = cursor.fetchone()
      print(kid)
    with sqlite3.connect(lootbag_db) as conn:
      cursor = conn.cursor()
      cursor.execute(f'''Update Children
                          set Good = 0
                          where ChildId = "{kid[0]}";''')
    with sqlite3.connect(lootbag_db) as conn:
      cursor = conn.cursor()
      cursor.execute(f'''DELETE FROM Toys
                            WHERE ChildId = {kid[0]}''')

    return "BadBOB"

if __name__ == "__main__":
  loot = Lootbag()
  loot.terminalCatch(sys.argv)
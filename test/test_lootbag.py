import unittest
import sys
sys.path.append('../')
from loot import Lootbag

def setUpModule():
  print('set up module')


def tearDownModule():
  print('tear down module')

class TestTerminalCatch(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    self.lootClass = Lootbag()

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_doesChildExist(self):
    self.assertEqual(self.lootClass.doesChildExist("kjkjh"), None)

  def test_terminalComands(self):
    '''Runs terminal comands that will result in errors'''
    self.assertEqual(self.lootClass.terminalCatch(("", 'hi')),"Incorrect input")
    self.assertEqual(self.lootClass.terminalCatch(("")),"Please add an argument")

  def test_removeToy(self):
    '''Tests if a present is removed. It first adds a gift so it can delete it'''
    self.lootClass.terminalCatch(("","add", "Bob", "box"))
    self.assertIsNotNone(self.lootClass.terminalCatch(("",'remove', "Bob", "box")))

    # if name does not exist
    self.assertIsNone(self.lootClass.terminalCatch(("", "remove", "sdfsdf", "truck")))

    # if toy does not exist
    self.assertIsNone(self.lootClass.terminalCatch(("", "remove", "lsdfkj", "sword")))

  def test_help(self):
    '''test if the help function runs'''
    self.lootClass.terminalCatch(("", "help"))

  def test_addToy(self):
    # if a toy is added the function will return a value greater than zero. It will return zero if a toy was not added
    self.assertTrue(self.lootClass.terminalCatch(("",'add', "box", "Bob")) > 0)
    self.assertTrue(self.lootClass.terminalCatch(("",'add', "squid", "slkj"))==0)

  def test_kidsWhoGetPresents(self):
    self.assertEqual(self.lootClass.terminalCatch(("",'ls')),"You LS'd!")


  def test_singleKidPresent(self):
    self.assertEqual(self.lootClass.terminalCatch(("",'ls',"Bob")),"ls and name")

  def test_toysDelivered(self):
    self.assertEqual(self.lootClass.terminalCatch(("",'delivered',"Sue")),"Delivered!")

  def test_badKid(self):
    self.assertEqual(self.lootClass.badKid(("bad", "Sue")), "BadBOB")



if __name__=='__main__':
  unittest.main()
  # test = TestTerminalCatch()
  # test

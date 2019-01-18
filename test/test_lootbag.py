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

  def test_terminalComands(self):
    self.assertEqual(self.lootClass.terminalCatch(("",'add', "string", "string")),"You added!")
    self.assertEqual(self.lootClass.terminalCatch(("",'remove', "string", "string")),"You removed :(")
    self.assertEqual(self.lootClass.terminalCatch(("", 'hi')),"Incorrect input")
    self.assertEqual(self.lootClass.terminalCatch(("")),"Please add an argument")

  def test_addToy(self):
        self.assertEqual(self.lootClass.terminalCatch(("",'add', "watch", "Bob")),"You added!")

  def test_kidsWhoGetPresents(self):
    self.assertEqual(self.lootClass.terminalCatch(("",'ls')),"You LS'd!")


  def test_singleKidPresent(self):
    self.assertEqual(self.lootClass.terminalCatch(("",'ls',"Bob")),"ls and name")

  def test_toysDelivered(self):
    self.assertEqual(self.lootClass.terminalCatch(("",'delivered',"Sue")),"Delivered!")




if __name__=='__main__':
  unittest.main()
  # test = TestTerminalCatch()
  # test

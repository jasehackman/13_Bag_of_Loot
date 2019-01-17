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
    print("hello")
    self.assertEqual(self.lootClass.terminalCatch(("",'add')),"You added!")



if __name__=='__main__':
  unittest.main()
  # test = TestTerminalCatch()
  # test

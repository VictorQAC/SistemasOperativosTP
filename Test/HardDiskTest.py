import unittest

from Code.SetUpGeneral import SetUpGeneral

class HardDiskTest(unittest.TestCase):

    def setUp(self):
        self.setUpGeneral = SetUpGeneral()
        self.setUpGeneral.hd.addProgram(self.setUpGeneral.prg1)
        self.setUpGeneral.hd.addProgram(self.setUpGeneral.prg2)

    def test_programAddedToHD(self):
        self.assertTrue(self.setUpGeneral.hd.programList.__len__() == 2)

    def test_getProgramByName(self):
        programFound = self.setUpGeneral.hd.getProgram('PrimerPrograma')
        self.assertTrue(programFound != None)
        self.assertTrue(programFound.instructionsList.__len__() == 4)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

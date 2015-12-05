import unittest

from Code.SetUpGeneral import SetUpGeneral
from Code.PCB import PCB

class Test(unittest.TestCase):

    def setUp(self):
        self.setUpGeneral = SetUpGeneral()
        self.pcb = self.setUpGeneral.pcb
        self.pcb2 = self.setUpGeneral.pcb2
        self.pcb3 = self.setUpGeneral.pcb3
        self.pcb4 = self.setUpGeneral.pcb4
        self.pcb5 = self.setUpGeneral.pcb5
        self.memory = self.setUpGeneral.mem
        self.hd = self.setUpGeneral.hd
        self.prg = self.setUpGeneral.prg1
        self.prg2 = self.setUpGeneral.prg2
        self.prg3 = self.setUpGeneral.prg3
        self.prg4 = self.setUpGeneral.prg4
        self.prg5 = self.setUpGeneral.prg5
        self.prg.instructionsToPages()
        self.prg2.instructionsToPages()
        self.prg3.instructionsToPages()
        self.prg4.instructionsToPages()
        self.prg5.instructionsToPages()
        self.hd.addProgram(self.prg)
        self.hd.addProgram(self.prg2)
        self.hd.addProgram(self.prg3)
        self.hd.addProgram(self.prg4)
        self.hd.addProgram(self.prg5)

    def test_haveBlocks(self):
        self.assertTrue(self.memory.memoryBlocks.__len__() == 4)
        self.assertTrue(self.memory.blocksTable.__len__() == 4)
        self.assertTrue(self.memory.blocksTable[1][0] == 1)
        self.assertTrue(self.memory.blocksTable[1][1] == 0)
        self.assertTrue(self.memory.blocksTable[1][2] == None)
 
    def test_refreshPositionInTable(self):
        self.memory.refreshPositionInTable(3, 1, 1)
        self.assertTrue(self.memory.blocksTable[1] == (1, 1, 3))
        
    def test_saveInstruction(self):
        self.assertEqual(self.memory.memoryBlocks[0].isEmptyBlock(), True)
        instList = [self.setUpGeneral.ins1,self.setUpGeneral.ins2]
        self.memory.saveInstruction(0,instList)
        self.assertEqual(self.memory.memoryBlocks[0].isEmptyBlock(), False)
        
    def test_spaceFreeInMemory(self):
        self.assertEqual(self.memory.spaceFreeInMemory(),True)
        instList1 = [self.setUpGeneral.ins1]
        instList2 = [self.setUpGeneral.ins2]
        instList3 = [self.setUpGeneral.ins3]
        instList4 = [self.setUpGeneral.IOins1]
        self.memory.saveInstruction(0,instList1)
        self.memory.saveInstruction(1,instList2)
        self.memory.saveInstruction(2,instList3)
        self.memory.saveInstruction(3,instList4)
        self.assertEqual(self.memory.spaceFreeInMemory(),False)
        
    def test_firstBlockFree(self):
        self.assertTrue(self.memory.firstBlockFree() == 0)
        instList1 = [self.setUpGeneral.ins1]
        self.memory.saveInstruction(0,instList1)
        self.assertTrue(self.memory.firstBlockFree() == 1)
        
    def test_assingBlockToInstructions1(self):
        # Caso en la cual tengo espacio libre en memoria para guardar el programa
        self.memory.assingBlockToInstructions(self.pcb2)
        tupleResult = (0,1,self.pcb2.getID())
        self.assertTrue(self.memory.blocksTable[0] == tupleResult)
     
    def test_assingBlockToInstructions2(self):
        # Caso en la cual no tengo espacio libre en memoria para guardar el programa
        #Lleno la memoria
        instList1 = [self.setUpGeneral.ins1]
        instList2 = [self.setUpGeneral.ins2]
        instList3 = [self.setUpGeneral.ins3]
        instList4 = [self.setUpGeneral.IOins1]
        self.memory.saveInstruction(0,instList1)
        self.memory.saveInstruction(1,instList2)
        self.memory.saveInstruction(2,instList3)
        self.memory.saveInstruction(3,instList4)
        self.assertEqual(self.memory.spaceFreeInMemory(),False)
        self.memory.assingBlockToInstructions(self.pcb2)
        self.assertEquals(self.memory.isPCBInTable(self.pcb2),True)  
     
    def test_loadInstructionsToMemory(self):
        self.memory.assingBlockToInstructions(self.pcb)
        self.assertEqual(self.memory.blocksTable[0][2],self.pcb.getID())
        self.pcb2.assignPageToBlock(0,0)
        self.memory.loadInstructionsToMemory(self.pcb2,0)
        self.assertEqual(self.memory.blocksTable[0][2],self.pcb2.getID())
          
    def test_fetch1(self):
        #Caso en la cual esta la memoria vacia
        resultExcepted = self.setUpGeneral.ins1.getMessage()
        self.assertEqual(self.memory.fetch(self.pcb, 0).getMessage(),resultExcepted)
    
    def test_fetch2(self):
        #Caso en la cual el programa esta en disco y no fue cargado anteriormenta a memoria
        fetch1 = self.memory.fetch(self.pcb, 0)
        fetch2 = self.memory.fetch(self.pcb2, 0)
        fetch3 = self.memory.fetch(self.pcb3, 0)
        fetch4 = self.memory.fetch(self.pcb4, 0)
        resultExcepted = self.setUpGeneral.ins3.getMessage()
        self.assertEqual(self.memory.fetch(self.pcb5, 0).getMessage(),resultExcepted)
        
    def test_fetch3(self):
        #Caso en la cual el programa esta en disco y fue cargado anteriormenta a memoria
        fetch1 = self.memory.fetch(self.pcb, 0)
        fetch2 = self.memory.fetch(self.pcb2, 0)
        fetch3 = self.memory.fetch(self.pcb3, 0)
        fetch4 = self.memory.fetch(self.pcb4, 0)
        fetch5 = self.memory.fetch(self.pcb5, 0)
        resultExcepted = self.setUpGeneral.IOins1.getMessage()
        self.assertEqual(self.memory.fetch(self.pcb, 1).getMessage(),resultExcepted)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

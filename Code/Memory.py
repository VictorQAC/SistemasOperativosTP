from _random import Random

import random

class Memory(object):

    def __init__(self, numberOfblocks, sizeOfBlock,hd):
        self.hardDisk = hd
        self.blockSize = sizeOfBlock
        self.memoryBlocks = self.initializeMemory(numberOfblocks)
        # Tabla de: Marco - Flag usado o no - PCB id
        self.blocksTable = self.initializeTable(numberOfblocks) 
            
    def initializeMemory(self, blocksNumber):
        aux = 0
        totalBlocks = []
        while aux < blocksNumber:
            totalBlocks.append(Block())
            aux += 1
        
        return totalBlocks
        
    def initializeTable(self, numberOfBlocks):
        aux = 0
        table = []
        while aux < numberOfBlocks:
            table.append((aux, 0, None))
            aux += 1
        return table
    
    def refreshPositionInTable(self, pcbID, numberBlock, status):
        self.blocksTable[numberBlock] = (numberBlock, status, pcbID)

    def saveInstruction(self,numberBlock,instBlock):
        block = self.memoryBlocks[numberBlock]
        block.clean()
        for item in instBlock:
            block.addInstruction(item)
                
    def spaceFreeInMemory(self):
        for item in self.memoryBlocks:
            if(item.isEmptyBlock()):
                return True
        return False
    
    def firstBlockFree(self):
        aux = -1
        for item in self.memoryBlocks:
            aux += 1
            if(item.isEmptyBlock()):
                return aux
            
    def blockAssingToPcb(self,pcb):
        aux = -1
        for item in self.blocksTable:
            aux += 1
            if(item[2] == pcb.getID()):
                return aux
            
    def addPCBToList(self, pcb):
        exist = False
        for item in self.pcbList:
            if item.pcbID == pcb.pcbID:
                exist = True
                
        if not exist:
            self.pcbList.append(pcb)
    
    def isPCBInTable(self,pcb):
        for item in self.blocksTable:
            if item[2] == pcb.getID():
                return True
        return False
              
    def loadInstructionsToMemory(self, pcb, page):
        # Traigo el programa de disco
        program = self.hardDisk.getProgram(pcb.getProgramName())
        # Obtengo instrucciones
        instBlock = program.getPage(page).instructions
        # Inserto las instruciones en la posicion indicada
        self.saveInstruction(pcb.getBlockOfPage(page), instBlock)
        # Actualizo estado de tabla
        self.refreshPositionInTable(pcb.getID(),pcb.getBlockOfPage(page),1)
         
    def assingBlockToInstructions(self,pcb):
        # Traigo el programa de disco
        program = self.hardDisk.getProgram(pcb.getProgramName())
        
        if(self.spaceFreeInMemory()):
            # Obtengo primer lugar libre de memoria
            block = self.firstBlockFree()
            # Consigo istrucciones a setear en memoria
            instBlock = program.getPage(pcb.getNextPage()).instructions
            # Informo al pcb cual seria su proxima pagina a cargar en memoria
            pcb.nextPageToLoad()
            # Guardo instruciones en memoria
            self.saveInstruction(block,instBlock)
            # Actualizo estado de tabla
            self.refreshPositionInTable(pcb.getID(),block,1)
            
        else:
            # Obtengo numero de bloque a limpiar
            numberblockToClean = random.randrange(self.memoryBlocks.__len__()-1)
            # Consigo istrucciones a setear en memoria
            instBlock = program.getPage(pcb.getNextPage()).instructions
            pcb.nextPageToLoad()
            # Guardo instruciones en memoria
            self.saveInstruction(numberblockToClean, instBlock)
            # Actualizo estado de tabla
            self.refreshPositionInTable(pcb.getID(),numberblockToClean,1)
            
                    
    def fetch(self, pcb, instruction):
        tupleResult = divmod(instruction, self.blockSize)
        page = tupleResult[0]
        instPosition = tupleResult[1]
        
        # Caso 1: el pcb tiene un marco asociado a la pagina
        if pcb.hasPageInTable(page):
            # Corroboro si esta en memoria las instrucciones de la pagina
            if (not pcb.inHardDisk(page)):
                block = self.memoryBlocks[pcb.getBlockOfPage(page)]
                return block.getInstruction(instPosition)
            else:
                # Las instrucciones no estan en memoria y debo ir a buscarlas
                
                # ir a disco y cargar la pagina a memoria
                self.loadInstructionsToMemory(pcb, page)
                # decirle al pcb que las instrucciones de esa pagina estan en memoria ahora
                self.pcbIncomingNowInMemory(pcb, page)
                # bloque donde estan las instrucciones a buscar
                block = self.memoryBlocks[pcb.getBlockOfPage(page)]
                # retornar la instruccion correspondiente
                return block.getInstruction(instPosition)
        else:
            # Caso 2: el pcb no tiene un marco asociado a la pagina
            
            #ir a disco y cargar la pagina a memoria
            self.assingBlockToInstructions(pcb)
            #Numero de block que fue asignado al pcb
            numberBlock = self.blockAssingToPcb(pcb)
            # asignar pagina y bloque al pcb
            pcb.assignPage(numberBlock)
            # bloque donde estan las instrucciones a buscar
            block = self.memoryBlocks[pcb.getBlockOfPage(page)]
            # retornar la instruccion correspondiente
            return block.getInstruction(instPosition)
        
# Bloque que esta en memoria            
class Block(object):
    
    def __init__(self):
        self.instructionsList = []
        
    def addInstruction(self,instruction):
        self.instructionsList.append(instruction)
     
    def getInstruction(self, instPosition):
        return self.instructionsList[instPosition]
    
    def isEmptyBlock(self):
        return self.instructionsList.__len__() == 0
    
    def clean(self):
        self.instructionsList = []
        

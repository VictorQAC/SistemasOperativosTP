class PCB(object):

    def __init__(self, id, prName, pS, prio):
        self.pcbID = id
        self.programName = prName
        self.pagesTable = PagesTable()
        self.programSize = pS
        self.nextInstruction = 0
        self.priority = prio
        self.nextPage = 0
        
    def getID(self):
        return self.pcbID
    
    def getProgramName(self):
        return self.programName
    
    def getNextPage(self):
        return self.nextPage
    
    def nextPageToLoad(self):
        self.nextPage +=1
    
    def assignPageToBlock(self, page, block):
        self.pagesTable.addPageToBlock(page, block)
        
    def movePageToDisk(self, page):
        self.pagesTable.moveToDisk(page)
      
    def movePageToMemory(self, page):
        self.pagesTable.moveToMemory(page)
      
    def hasPageInTable(self, page):
        return self.pagesTable.pagesToBlock.get(page) != None
    
    def getBlockOfPage(self, page):
        return self.pagesTable.getBlock(page)
        
    def inHardDisk(self, page):
        return self.pagesTable.inHD(page)
    
    def numberPage(self):
        return self.pagesTable.lastPage()
    
    def assignPage(self,numberBlock):
        self.pagesTable.addPage(numberBlock)

class PagesTable(object):
    
    def __init__(self):
        self.pagesToBlock = {}
        self.lastPageAssing = -1
        
    def addPageToBlock(self, page, block):
        self.pagesToBlock[page] = (block, 0)
        
    def moveToDisk(self, page):
        tuplePage = self.pagesToBlock[page]
        self.pagesToBlock[page] = (tuplePage[0], 1)
        
    def moveToMemory(self, page):
        tuplePage = self.pagesToBlock[page]
        self.pagesToBlock[page] = (tuplePage[0], 0)
        
    def getBlock(self, page):
        tuplePage = self.pagesToBlock[page]
        return tuplePage[0]
    
    def getNumberBlock(self,page):
        tuplePage = self.pagesToBlock[page]
        return tuplePage[0]
    
    def inHD(self,page):
        tuple = self.pagesToBlock[page]
        return tuple[1] == 1
    
    def lastPage(self):
        return self.lastPageAssing
    
    def addPage(self,numberBlock):
        self.lastPageAssing += 1
        self.pagesToBlock[self.lastPageAssing] = (numberBlock, 0)      
            
            
            
            

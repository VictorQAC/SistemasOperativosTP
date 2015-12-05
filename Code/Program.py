
class Program(object):

    def __init__(self, prName, instList, pSize, prio):
        self.programName = prName
        self.priority = prio
        self.instructionsList = instList
        self.pageSize = pSize
        self.pages = self.createPages()
        
    def createPages(self):
        tupleDiv = divmod(self.instructionsList.__len__(), self.pageSize)
           
        if tupleDiv[1] == 0:
            return self.numberOfPages(tupleDiv[0])
        else:
            return self.numberOfPages(tupleDiv[0] + 1)
            
    def numberOfPages(self, pagesNumber):
        totalPages = []
        aux = 0
               
        while aux < pagesNumber:
            totalPages.append(Page())
            aux += 1
            
        return totalPages
        
    def instructionsToPages(self):
        auxSize = self.pageSize
        currentPage = 0
        
        for inst in self.instructionsList:
            auxSize -= 1
            self.pages[currentPage].instructions.append(inst)
            if auxSize == 0:
                currentPage += 1
                auxSize = self.pageSize
                
    def getPage(self, page):
        return self.pages[page]
    
    def getName(self):
        return self.programName

class Page(object):
    
    def __init__(self):
        self.instructions = []
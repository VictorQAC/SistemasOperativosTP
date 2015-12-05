class HardDisk(object):

    def __init__(self):
        self.programList = []
        
    def addProgram(self, program):
        self.programList.append(program)
        
    def getProgram(self, prName):
        for item in self.programList:
            if item.getName() == prName:
                return item
            
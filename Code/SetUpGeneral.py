from Code.Instruction import Instruction, InstructionKind
from Code.Program import Program
from Code.HardDisk import HardDisk
from Code.Memory import Memory
from Code.PCB import PCB


class SetUpGeneral(object):

    def __init__(self):
        # Disco rigido
        self.hd = HardDisk()
        
        # Memoria
        self.mem = Memory(4, 2, self.hd)
        
        # Instrucciones
        self.ins1 = Instruction("Primera instruccion de CPU", InstructionKind.CPU)
        self.IOins1 = Instruction("Primera instruccion de IO", InstructionKind.IO)
        self.ins2 = Instruction("Segunda instruccion de CPU", InstructionKind.CPU)
        self.ins3 = Instruction("Tercera instruccion de CPU", InstructionKind.CPU)
        self.IOins2 = Instruction("Segunda instruccion de IO", InstructionKind.IO)
        
        # Programas con su lista de instrucciones
        self.prg1 = Program("PrimerPrograma", [self.ins1,self.IOins1,self.ins2,self.ins3], 2, 2)
        self.prg2 = Program("SegundoPrograma", [self.ins1,self.ins2,self.ins3,self.IOins2], 2, 1)
        self.prg3 = Program("TercerPrograma", [self.ins1,self.IOins1], 2, 3)
        self.prg4 = Program("CuartoPrograma", [self.ins1], 2, 4)
        self.prg5 = Program("QuintoPrograma",[self.ins3],2,5)
        
        # PCB apuntando a sus respectivos programas
        self.pcb = PCB(1,"PrimerPrograma", None, None)
        self.pcb2 = PCB(2,"SegundoPrograma", None, None)
        self.pcb3 = PCB(3,"TercerPrograma", None, None)
        self.pcb4 = PCB(4,"CuartoPrograma", None, None)
        self.pcb5 = PCB(5,"QuintoPrograma",None,None)
        
        
        
        
        
    
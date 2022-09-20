from tkinter import *
import time
from Memory import Memory
from SharedBus import MemoryBus
from Processor import Processor
import threading

#Main Window design paramaters 
class Design:

    def  __init__(self, root):

        #Windows basic features desing 
        self.root = Tk = root
        self.root.geometry("1300x900")
        self.root.title("Simulador protocolo MESI")
        self.root.resizable(False, False)

        #Multiprocessor elements 
        self.processors = []
        self.memory = Memory()
        self.bus = MemoryBus(self.memory)


        self.P0AInst= StringVar()
        self.P0AInst.set("P0 : ----------")
        self.P0LInst= StringVar()
        self.P0LInst.set("P0 : ----------")
        self.P0B0D= StringVar()
        self.P0B0D.set("P0 : ----------")
        self.P0B1D= StringVar()
        self.P0B1D.set("P0 : ----------")
        self.P0B2D= StringVar()
        self.P0B2D.set("P0 : ----------")
        self.P0B3D= StringVar()
        self.P0B3D.set("P0 : ----------")

        self.Window_Design()


    def Window_Design(self):

            window = self.root

            lblP0 = Label(window, text="Processor 0", width=15, height=2, bg = "#CE4912")
            lblP0.grid(row=0, column=2)

            p0AInstLabel = Label(self.root, textvariable=self.P0AInst)
            p0AInstLabel.grid(row=1, column=2)
            p0LInstLabel = Label(self.root, textvariable=self.P0LInst)
            p0LInstLabel.grid(row=2, column=2)
            p0B0DL = Label(self.root, textvariable=self.P0B0D)
            p0B0DL.grid(row=6, column=2)
            p0B1DL = Label(self.root, textvariable=self.P0B1D)
            p0B1DL.grid(row=10, column=2)
            p0B2DL = Label(self.root, textvariable=self.P0B2D)
            p0B2DL.grid(row=14, column=2)
            p0B3DL = Label(self.root, textvariable=self.P0B3D)
            p0B3DL.grid(row=18, column=2)

            lblP1 = Label(window, text="Processor 1", width=15, height=2, bg= "#F36B1C")
            lblP1.grid(row=0, column=4)

            lblP2 = Label(window, text="Processor 2", width=15, height=2, bg = "#0B6AB0")
            lblP2.grid(row=0, column=6)

            lblP3 = Label(window, text="Processor 3", width=15, height=2, bg = "#F8D605")
            lblP3.grid(row=0, column=8)

            btn = Button(window, text = "Empezar Simulación", height=2)
            btn.grid(row=2, column=9)

            btn = Button(window, text = "Pausar Simulación",  height=2)
            btn.grid(row=4, column=9)

            btn = Button(window, text = "Simulación paso a paso",  height=2)
            btn.grid(row=6, column=9)


            lblP3 = Label(window, text="Instrucción especifica", width=30, height=2)
            lblP3.grid(row=8, column=9)
            entry = Entry()
            entry.grid(row=9, column=9)
            btn = Button(window, text = "Agregar Instrucción", height=2)
            btn.grid(row=10, column=9)

            lblP3 = Label(window, text="Alertas", width=30, height=2)
            lblP3.grid(row=13, column=9)

            lbl = Label(window, text="", width=10, height=4)
            lbl.grid(row=0, column=0)
            lblE = Label(window, text="Ejecutando", width=30, height=2)
            lblE.grid(row=1, column=0)
            lblU = Label(window, text="Última ejecución", width=30, height=2)
            lblU.grid(row=2, column=0)


            #BLOCK 0 INFORMATION
            lblU = Label(window, text="Block 0", width=30, height=2, bg = "#FFE373")
            lblU.grid(row=3, column=0)
            lblU = Label(window, text="Bit State", width=30, height=2,bg = "#FFE373")
            lblU.grid(row=4, column=0)
            lblU = Label(window, text="Address", width=30, height=2,bg = "#FFE373")
            lblU.grid(row=5, column=0)
            lblU = Label(window, text="Value", width=30, height=2, bg = "#FFE373")
            lblU.grid(row=6, column=0)

            #BLOCK 1 INFORMATION
            lblU = Label(window, text="Block 1", width=30, height=2,bg = "#FFE373")
            lblU.grid(row=7, column=0)
            lblU = Label(window, text="Bit State", width=30, height=2,bg = "#FFE373")
            lblU.grid(row=8, column=0)
            lblU = Label(window, text="Address", width=30, height=2,bg = "#FFE373")
            lblU.grid(row=9, column=0)
            lblU = Label(window, text="Value", width=30,height=2, bg = "#FFE373")
            lblU.grid(row=10, column=0)

            #BLOCK 2 INFORMATION
            lblU = Label(window, text="Block 2", width=30, height=2, bg = "#FFE373")
            lblU.grid(row=11, column=0)
            lblU = Label(window, text="Bit State", width=30, height=2, bg = "#FFE373")
            lblU.grid(row=12, column=0)
            lblU = Label(window, text="Address", width=30, height=2, bg = "#FFE373")
            lblU.grid(row=13, column=0)
            lblU = Label(window, text="Value", width=30, height=2, bg = "#FFE373")
            lblU.grid(row=14, column=0)

            #BLOCK 3 INFORMATION
            lblU = Label(window, text="Block 3", width=30, height=2, bg = "#FFE373")
            lblU.grid(row=15, column=0)
            lblU = Label(window, text="Bit Satate", width=30, height=2, bg = "#FFE373")
            lblU.grid(row=16, column=0)
            lblU = Label(window, text="Address", width=30, height=2,  bg = "#FFE373")
            lblU.grid(row=17, column=0)
            lblU = Label(window, text="Value", width=30, height=2, bg = "#FFE373")
            lblU.grid(row=18, column=0)

            #Main Memory Cells
            lblU = Label(window, text="Main Memory Blocks", height=2, bg = "#FFE373")
            lblU.grid(row=19, column=4)

            lblU = Label(window, text="0b000", bg = "#FFE373")
            lblU.grid(row=20, column=1)

            lblU = Label(window, text="0b001", bg = "#FFE373")
            lblU.grid(row=20, column=2)

            lblU = Label(window, text="0b010", bg = "#FFE373")
            lblU.grid(row=20, column=3)

            lblU = Label(window, text="0b011", bg = "#FFE373")
            lblU.grid(row=20, column=4)

            lblU = Label(window, text="0b100", bg = "#FFE373")
            lblU.grid(row=20, column=5)

            lblU = Label(window, text="0b101", bg = "#FFE373")
            lblU.grid(row=20, column=6)

            lblU = Label(window, text="0b110", bg = "#FFE373")
            lblU.grid(row=20, column=7)

            lblU = Label(window, text="0b111", bg = "#FFE373")
            lblU.grid(row=20, column=8)

              #Mmemory Blocks
            lblU = Label(window, text="000", bg = "#FFE373")
            lblU.grid(row=21, column=1)

            lblU = Label(window, text="000" , bg = "#FFE373")
            lblU.grid(row=21, column=2)

            lblU = Label(window, text="000", bg = "#FFE373")
            lblU.grid(row=21, column=3)

            lblU = Label(window, text="000", bg = "#FFE373")
            lblU.grid(row=21, column=4)

            lblU = Label(window, text="000", bg = "#FFE373")
            lblU.grid(row=21, column=5)

            lblU = Label(window, text="000", bg = "#FFE373")
            lblU.grid(row=21, column=6)

            lblU = Label(window, text="000", bg = "#FFE373")
            lblU.grid(row=21, column=7)

            lblU = Label(window, text="000", bg = "#FFE373")
            lblU.grid(row=21, column=8)


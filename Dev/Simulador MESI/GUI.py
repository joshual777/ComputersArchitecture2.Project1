from tkinter import *
import time
from tkinter.tix import Tree
from turtle import width
from Memory import Memory
from SharedBus import MemoryBus
from Processor import Processor
import threading

#Main Window design paramaters 
class Design:

    def  __init__(self, root):

        #Windows basic features desing 
        self.root = Tk = root
        self.root.geometry("1000x700")
        self.root.title("MESI PROTOCOL SIMULATOR")
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

            #Background canvas and color 
            backgorund = Canvas(window, width= 1000, height= 700, bg = "#FFE373")
            backgorund.place(x= 0, y = 0)

            #Label Processor 0
            lbl_procesor0 = Label(window, text="Processor 0", width=15, height=2, bg = "#CE4912")
            lbl_procesor0.place(x=200, y=0)

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

            #CONTROL SECTION 

            #Label Processor 1
            lbl_processor1 = Label(window, text="Processor 1", width=15, height=2, bg= "#F36B1C")
            lbl_processor1.place(x=350, y=0)

            #Label Processor 2
            lbl_processor2 = Label(window, text="Processor 2", width=15, height=2, bg = "#0B6AB0")
            lbl_processor2.place(x=500, y=0)

            #Label Processor 3
            lbl_procesor3 = Label(window, text="Processor 3", width=15, height=2, bg = "#F8D605")
            lbl_procesor3.place(x=650, y=0)

            #Action Buttons Section

            #Start simulation button 
            btn_start = Button(window, text = "Start Simulation", height=2, bg= "#9EE6AA")
            btn_start.place(x=700, y=450)

            #Stop simulation button
            btn_stop = Button(window, text = "Stop Simulation",  height=2, bg= "#9EE6AA")
            btn_stop.place(x=800, y=450)

            #Step by Step simulation button
            btn_step = Button(window, text = "Step by Step Simulation",  height=2, bg= "#9EE6AA")
            btn_step.place(x=730, y=500)

            #Insert Label Instruction
            lblP3 = Label(window, text="Insert Instruction", width=28, height=2, bg= "#9EE6AA")
            lblP3.place(x=700, y=550)

            entry_isntruction = Entry(window, width = 30, bg= "#9EE6AA")
            entry_isntruction.place(x=720, y=600)

            btn_insert = Button(window, text = "Add", height=2, bg= "#9EE6AA")
            btn_insert.place(x=800, y=630)


            #---------------------------------------------------------------------------------

            #lblP3 = Label(window, text="Alertas", width=30, height=2)
            #lblP3.grid(row=13, column=9)
            
            """
            lbl = Label(window, text="", width=10, height=4)
            lbl.grid(row=0, column=0)
            lblE = Label(window, text="Ejecutando", width=30, height=2)
            lblE.grid(row=1, column=0)
            lblU = Label(window, text="Última ejecución", width=30, height=2)
            lblU.grid(row=2, column=0)
            """

            #BLOCKS INFORMATION SECTION 

            #BLOCK 0 INFORMATION
            lbl_block0_1 = Label(window, text="Block 0", width=10, height=1, bg = "#bce784")
            lbl_block0_1.place(x=5, y=40)
            lbl_block0_2 = Label(window, text="Bit State", width=10, height=1,bg = "#bce784")
            lbl_block0_2.place(x=5, y=60)
            lbl_block0_3 = Label(window, text="Address", width=10, height=1,bg = "#bce784")
            lbl_block0_3.place(x=5, y=80)
            lbl_block0_4 = Label(window, text="Value", width=10, height=1, bg = "#bce784")
            lbl_block0_4.place(x=5, y=100)

            #BLOCK 1 INFORMATION
            lbl_block1_1 = Label(window, text="Block 1", width=10, height=1,bg = "#525174")
            lbl_block1_1.place(x=5, y=140)
            lbl_block1_2 = Label(window, text="Bit State", width=10, height=1,bg = "#525174")
            lbl_block1_2.place(x=5, y=160)
            lbl_block1_3 = Label(window, text="Address", width=10, height=1,bg = "#525174")
            lbl_block1_3.place(x=5, y=180)
            lbl_block1_4 = Label(window, text="Value", width=10,height=1, bg = "#525174")
            lbl_block1_4.place(x=5, y=200)

            #BLOCK 2 INFORMATION
            lbl_block2_1 = Label(window, text="Block 2", width=10, height=1, bg = "#348aa7")
            lbl_block2_1.place(x=5, y=240)
            lbl_block2_2 = Label(window, text="Bit State", width=10, height=1, bg = "#348aa7")
            lbl_block2_2.place(x=5, y=260)
            lbl_block2_3 = Label(window, text="Address", width=10, height=1, bg = "#348aa7")
            lbl_block2_3.place(x=5, y=280)
            lbl_block2_4 = Label(window, text="Value", width=10, height=1, bg = "#348aa7")
            lbl_block2_4.place(x=5, y=300)

            #BLOCK 3 INFORMATION
            lbl_block3_1 = Label(window, text="Block 3", width=10, height=1, bg = "#5dd39e")
            lbl_block3_1.place(x=5, y=340)
            lbl_block3_2 = Label(window, text="Bit Satate", width=10, height=1, bg = "#5dd39e")
            lbl_block3_2.place(x=5, y=360)
            lbl_block3_3 = Label(window, text="Address", width=10, height=1,  bg = "#5dd39e")
            lbl_block3_3.place(x=5, y=380)
            lbl_block3_4 = Label(window, text="Value", width=10, height=1, bg = "#5dd39e")
            lbl_block3_4.place(x=5, y=400)

            #LABEL BUS 
            lbl_bus = Label(window,  width=1000, height=1, bg = "red")
            lbl_bus.place(x=0, y= 425)

            lbl_bus = Label(window, text="Shared bus", width=20, height=1, bg = "red")
            lbl_bus.place(x=390, y= 425)

            #MAIN MEMORY SECTION 

            #Main Memory Cells
            lbl_mainmen = Label(window, text="Main Memory Blocks", height=1, bg = "cyan")
            lbl_mainmen.place(x=390, y=450)

            lbl_cell0 = Label(window, text="0b000", bg = "#FFE373")
            lbl_cell0.place(x=360, y=480)

            lbl_cell1 = Label(window, text="0b001", bg = "#FFE373")
            lbl_cell1.place(x=360, y=500)

            lbl_cell2 = Label(window, text="0b010", bg = "#FFE373")
            lbl_cell2.place(x=360, y=520)

            lbl_cell3 = Label(window, text="0b011", bg = "#FFE373")
            lbl_cell3.place(x=360, y=540)

            lbl_cell4 = Label(window, text="0b100", bg = "#FFE373")
            lbl_cell4.place(x=360, y=560)

            lbl_cell5 = Label(window, text="0b101", bg = "#FFE373")
            lbl_cell5.place(x=360, y=580)

            lbl_cell6 = Label(window, text="0b110", bg = "#FFE373")
            lbl_cell6.place(x=360, y=600)

            lbl_cell7 = Label(window, text="0b111", bg = "#FFE373")
            lbl_cell7.place(x=360, y=620)


            #Memmory Blocks
            lbl_allocate0 = Label(window, text="000", bg = "#FFE373")
            lbl_allocate0.place(x=420, y=480)

            lbl_allocate1 = Label(window, text="000" , bg = "#FFE373")
            lbl_allocate1.place(x=420, y=500)

            lbl_allocate2 = Label(window, text="000", bg = "#FFE373")
            lbl_allocate2.place(x=420, y=520)

            lbl_allocate3 = Label(window, text="000", bg = "#FFE373")
            lbl_allocate3.place(x=420, y=540)

            lbl_allocate4 = Label(window, text="000", bg = "#FFE373")
            lbl_allocate4.place(x=420, y=560)

            lbl_allocate5 = Label(window, text="000", bg = "#FFE373")
            lbl_allocate5.place(x=420, y=580)

            lbl_allocate6 = Label(window, text="000", bg = "#FFE373")
            lbl_allocate6.place(x=420, y=600)

            lbl_allocate7 = Label(window, text="000", bg = "#FFE373")
            lbl_allocate7.place(x=420, y=620)


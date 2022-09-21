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


        #INITIALIZED P0 

        #VALUE
        self.P0_BLOCK1_V= StringVar()
        self.P0_BLOCK1_V.set("----------")
        self.P0_BLOCK2_V= StringVar()
        self.P0_BLOCK2_V.set("----------")
        self.P0_BLOCK3_V= StringVar()
        self.P0_BLOCK3_V.set("----------")
        self.P0_BLOCK4_V= StringVar()
        self.P0_BLOCK4_V.set("----------")

        #ADDRESS
        self.P0_BLOCK1_A= StringVar()
        self.P0_BLOCK1_A.set("----------")
        self.P0_BLOCK2_A= StringVar()
        self.P0_BLOCK2_A.set("----------")
        self.P0_BLOCK3_A= StringVar()
        self.P0_BLOCK3_A.set("----------")
        self.P0_BLOCK4_A= StringVar()
        self.P0_BLOCK4_A.set("----------")

        #STATE BIT
        self.P0_BLOCK1_S= StringVar()
        self.P0_BLOCK1_S.set("----------")
        self.P0_BLOCK2_S= StringVar()
        self.P0_BLOCK2_S.set("----------")
        self.P0_BLOCK3_S= StringVar()
        self.P0_BLOCK3_S.set("----------")
        self.P0_BLOCK4_S= StringVar()
        self.P0_BLOCK4_S.set("----------")


        #INITIALIZED P1

        #VALUE
        self.P1_BLOCK1_V= StringVar()
        self.P1_BLOCK1_V.set("----------")
        self.P1_BLOCK2_V= StringVar()
        self.P1_BLOCK2_V.set("----------")
        self.P1_BLOCK3_V= StringVar()
        self.P1_BLOCK3_V.set("----------")
        self.P1_BLOCK4_V= StringVar()
        self.P1_BLOCK4_V.set("----------")

        #ADDRESS
        self.P1_BLOCK1_A= StringVar()
        self.P1_BLOCK1_A.set("----------")
        self.P1_BLOCK2_A= StringVar()
        self.P1_BLOCK2_A.set("----------")
        self.P1_BLOCK3_A= StringVar()
        self.P1_BLOCK3_A.set("----------")
        self.P1_BLOCK4_A= StringVar()
        self.P1_BLOCK4_A.set("----------")

        #STATE BIT
        self.P1_BLOCK1_S= StringVar()
        self.P1_BLOCK1_S.set("----------")
        self.P1_BLOCK2_S= StringVar()
        self.P1_BLOCK2_S.set("----------")
        self.P1_BLOCK3_S= StringVar()
        self.P1_BLOCK3_S.set("----------")
        self.P1_BLOCK4_S= StringVar()
        self.P1_BLOCK4_S.set("----------")


        #INITIALIZED P2

        #VALUE
        self.P2_BLOCK1_V= StringVar()
        self.P2_BLOCK1_V.set("----------")
        self.P2_BLOCK2_V= StringVar()
        self.P2_BLOCK2_V.set("----------")
        self.P2_BLOCK3_V= StringVar()
        self.P2_BLOCK3_V.set("----------")
        self.P2_BLOCK4_V= StringVar()
        self.P2_BLOCK4_V.set("----------")

        #ADDRESS
        self.P2_BLOCK1_A= StringVar()
        self.P2_BLOCK1_A.set("----------")
        self.P2_BLOCK2_A= StringVar()
        self.P2_BLOCK2_A.set("----------")
        self.P2_BLOCK3_A= StringVar()
        self.P2_BLOCK3_A.set("----------")
        self.P2_BLOCK4_A= StringVar()
        self.P2_BLOCK4_A.set("----------")

        #STATE BIT
        self.P2_BLOCK1_S= StringVar()
        self.P2_BLOCK1_S.set("----------")
        self.P2_BLOCK2_S= StringVar()
        self.P2_BLOCK2_S.set("----------")
        self.P2_BLOCK3_S= StringVar()
        self.P2_BLOCK3_S.set("----------")
        self.P2_BLOCK4_S= StringVar()
        self.P2_BLOCK4_S.set("----------")

        #INITIALIZED  P3

        #VALUE
        self.P3_BLOCK1_V= StringVar()
        self.P3_BLOCK1_V.set("----------")
        self.P3_BLOCK2_V= StringVar()
        self.P3_BLOCK2_V.set("----------")
        self.P3_BLOCK3_V= StringVar()
        self.P3_BLOCK3_V.set("----------")
        self.P3_BLOCK4_V= StringVar()
        self.P3_BLOCK4_V.set("----------")

        #ADDRESS
        self.P3_BLOCK1_A= StringVar()
        self.P3_BLOCK1_A.set("----------")
        self.P3_BLOCK2_A= StringVar()
        self.P3_BLOCK2_A.set("----------")
        self.P3_BLOCK3_A= StringVar()
        self.P3_BLOCK3_A.set("----------")
        self.P3_BLOCK4_A= StringVar()
        self.P3_BLOCK4_A.set("----------")

        #STATE BIT
        self.P3_BLOCK1_S= StringVar()
        self.P3_BLOCK1_S.set("----------")
        self.P3_BLOCK2_S= StringVar()
        self.P3_BLOCK2_S.set("----------")
        self.P3_BLOCK3_S= StringVar()
        self.P3_BLOCK3_S.set("----------")
        self.P3_BLOCK4_S= StringVar()
        self.P3_BLOCK4_S.set("----------")

        #MEMORY CELLS
        self.CELL0 = StringVar()
        self.CELL0.set("----------")
        self.CELL1 = StringVar()
        self.CELL1.set("----------")
        self.CELL2 = StringVar()
        self.CELL2.set("----------")
        self.CELL3 = StringVar()
        self.CELL3.set("----------")
        self.CELL4 = StringVar()
        self.CELL4.set("----------")
        self.CELL5 = StringVar()
        self.CELL5.set("----------")
        self.CELL6 = StringVar()
        self.CELL6.set("----------")
        self.CELL7 = StringVar()
        self.CELL7.set("----------")


        self.Window_Design()
        self.Thread_Processors()



    #PROTOCOL PROCESS SECTION
    #In this section Start, Stop and Step by Step functions are intialized

    def START_SIMULATION(self):
      self.processors[0].runThread(False)
      self.processors[1].runThread(False)
      self.processors[2].runThread(False)
      self.processors[3].runThread(False)

    def STOP_SIMULATION(self):
      self.processors[0].stopThread()
      self.processors[1].stopThread()
      self.processors[2].stopThread()
      self.processors[3].stopThread()


    def STEP_STEP_SIMULATION(self):
      self.processors[0].runThread(True)
      self.processors[1].runThread(True)
      self.processors[2].runThread(True)
      self.processors[3].runThread(True)
      

    def Window_Design(self):

            window = self.root

            #Background canvas and color 
            backgorund = Canvas(window, width= 1000, height= 700, bg = "#FFE373")
            backgorund.place(x= 0, y = 0)


            """
            p0AInstLabel = Label(self.root, textvariable=self.P0AInst)
            p0AInstLabel.grid(row=1, column=2)

            p0LInstLabel = Label(self.root, textvariable=self.P0LInst)
            p0LInstLabel.grid(row=2, column=2)
            """




            #CONTROL SECTION 

            #Label Processor 0
            lbl_procesor0 = Label(window, text="Processor 0", width=15, height=2, bg = "#CE4912")
            lbl_procesor0.place(x=200, y=0)

            
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
            btn_start = Button(window, text = "Start Simulation", command= self.START_SIMULATION,  height=2, bg= "#9EE6AA")
            btn_start.place(x=700, y=450)

            #Stop simulation button
            btn_stop = Button(window, text = "Stop Simulation",  command= self.STOP_SIMULATION, height=2, bg= "#9EE6AA")
            btn_stop.place(x=800, y=450)

            #Step by Step simulation button
            btn_step = Button(window, text = "Step by Step Simulation", command=self.STEP_STEP_SIMULATION,  height=2, bg= "#9EE6AA")
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


            #Processor 0
            p0B0DL = Label(self.root, textvariable=self.P0_BLOCK1_S, height=1, bg = "#CE4912")
            p0B0DL.place(x=200, y=60)

            p0B1DL = Label(self.root, textvariable=self.P0_BLOCK1_A, height=1, bg = "#CE4912")
            p0B1DL.place(x=200, y=80)

            p0B2DL = Label(self.root, textvariable=self.P0_BLOCK1_V, height=1, bg = "#CE4912")
            p0B2DL.place(x=200, y=100)

            #Processor 1
            p1B0DL = Label(self.root, textvariable=self.P1_BLOCK1_S, height=1, bg = "#F36B1C")
            p1B0DL.place(x=350, y=60)

            p1B1DL = Label(self.root, textvariable=self.P1_BLOCK1_A, height=1, bg = "#F36B1C")
            p1B1DL.place(x=350, y=80)

            p1B2DL = Label(self.root, textvariable=self.P1_BLOCK1_V, height=1, bg = "#F36B1C")
            p1B2DL.place(x=350, y=100)

            #Processor 2
            p2B0DL = Label(self.root, textvariable=self.P2_BLOCK1_S, height=1, bg = "#0B6AB0")
            p2B0DL.place(x=500, y=60)

            p2B1DL = Label(self.root, textvariable=self.P2_BLOCK1_A, height=1, bg = "#0B6AB0")
            p2B1DL.place(x=500, y=80)

            p2B2DL = Label(self.root, textvariable=self.P2_BLOCK1_V, height=1, bg = "#0B6AB0")
            p2B2DL.place(x=500, y=100)

            #Processor 3
            p2B0DL = Label(self.root, textvariable=self.P3_BLOCK1_S, height=1, bg = "#F8D605")
            p2B0DL.place(x=650, y=60)

            p3B1DL = Label(self.root, textvariable=self.P3_BLOCK1_A, height=1, bg = "#F8D605")
            p3B1DL.place(x=650, y=80)

            p3B2DL = Label(self.root, textvariable=self.P3_BLOCK1_V, height=1, bg = "#F8D605")
            p3B2DL.place(x=650, y=100)
            


            #BLOCK 1 INFORMATION
            lbl_block1_1 = Label(window, text="Block 1", width=10, height=1,bg = "#525174")
            lbl_block1_1.place(x=5, y=140)
            lbl_block1_2 = Label(window, text="Bit State", width=10, height=1,bg = "#525174")
            lbl_block1_2.place(x=5, y=160)
            lbl_block1_3 = Label(window, text="Address", width=10, height=1,bg = "#525174")
            lbl_block1_3.place(x=5, y=180)
            lbl_block1_4 = Label(window, text="Value", width=10,height=1, bg = "#525174")
            lbl_block1_4.place(x=5, y=200)

            #Processor 0
            p0B0DL = Label(self.root, textvariable=self.P0_BLOCK2_S, height=1, bg = "#CE4912")
            p0B0DL.place(x=200, y=160)

            p0B1DL = Label(self.root, textvariable=self.P0_BLOCK2_A, height=1, bg = "#CE4912")
            p0B1DL.place(x=200, y=180)

            p0B2DL = Label(self.root, textvariable=self.P0_BLOCK2_V, height=1, bg = "#CE4912")
            p0B2DL.place(x=200, y=200)

            #Processor 1
            p1B0DL = Label(self.root, textvariable=self.P1_BLOCK2_S, height=1, bg = "#F36B1C")
            p1B0DL.place(x=350, y=160)

            p1B1DL = Label(self.root, textvariable=self.P1_BLOCK2_A, height=1, bg = "#F36B1C")
            p1B1DL.place(x=350, y=180)

            p1B2DL = Label(self.root, textvariable=self.P1_BLOCK2_V, height=1, bg = "#F36B1C")
            p1B2DL.place(x=350, y=200)

            #Processor 2
            p2B0DL = Label(self.root, textvariable=self.P2_BLOCK2_S, height=1, bg = "#0B6AB0")
            p2B0DL.place(x=500, y=160)

            p2B1DL = Label(self.root, textvariable=self.P2_BLOCK2_A, height=1, bg = "#0B6AB0")
            p2B1DL.place(x=500, y=180)

            p2B2DL = Label(self.root, textvariable=self.P2_BLOCK2_V, height=1, bg = "#0B6AB0")
            p2B2DL.place(x=500, y=200)

            #Processor 3
            p2B0DL = Label(self.root, textvariable=self.P3_BLOCK2_S, height=1, bg = "#F8D605")
            p2B0DL.place(x=650, y=160)

            p3B1DL = Label(self.root, textvariable=self.P3_BLOCK2_A, height=1, bg = "#F8D605")
            p3B1DL.place(x=650, y=180)

            p3B2DL = Label(self.root, textvariable=self.P3_BLOCK2_V, height=1, bg = "#F8D605")
            p3B2DL.place(x=650, y=200)

            #BLOCK 2 INFORMATION
            lbl_block2_1 = Label(window, text="Block 2", width=10, height=1, bg = "#348aa7")
            lbl_block2_1.place(x=5, y=240)
            lbl_block2_2 = Label(window, text="Bit State", width=10, height=1, bg = "#348aa7")
            lbl_block2_2.place(x=5, y=260)
            lbl_block2_3 = Label(window, text="Address", width=10, height=1, bg = "#348aa7")
            lbl_block2_3.place(x=5, y=280)
            lbl_block2_4 = Label(window, text="Value", width=10, height=1, bg = "#348aa7")
            lbl_block2_4.place(x=5, y=300)


            #Processor 0
            p0B0DL = Label(self.root, textvariable=self.P0_BLOCK3_S, height=1, bg = "#CE4912")
            p0B0DL.place(x=200, y=260)

            p0B1DL = Label(self.root, textvariable=self.P0_BLOCK3_A, height=1, bg = "#CE4912")
            p0B1DL.place(x=200, y=280)

            p0B2DL = Label(self.root, textvariable=self.P0_BLOCK3_V, height=1, bg = "#CE4912")
            p0B2DL.place(x=200, y=300)

            #Processor 1
            p1B0DL = Label(self.root, textvariable=self.P1_BLOCK3_S, height=1, bg = "#F36B1C")
            p1B0DL.place(x=350, y=260)

            p1B1DL = Label(self.root, textvariable=self.P1_BLOCK3_A, height=1, bg = "#F36B1C")
            p1B1DL.place(x=350, y=280)

            p1B2DL = Label(self.root, textvariable=self.P1_BLOCK3_V, height=1, bg = "#F36B1C")
            p1B2DL.place(x=350, y=300)

            #Processor 2
            p2B0DL = Label(self.root, textvariable=self.P2_BLOCK3_S, height=1, bg = "#0B6AB0")
            p2B0DL.place(x=500, y=260)

            p2B1DL = Label(self.root, textvariable=self.P2_BLOCK3_A, height=1, bg = "#0B6AB0")
            p2B1DL.place(x=500, y=280)

            p2B2DL = Label(self.root, textvariable=self.P2_BLOCK3_V, height=1, bg = "#0B6AB0")
            p2B2DL.place(x=500, y=300)

            #Processor 3
            p2B0DL = Label(self.root, textvariable=self.P3_BLOCK3_S, height=1, bg = "#F8D605")
            p2B0DL.place(x=650, y=260)

            p3B1DL = Label(self.root, textvariable=self.P3_BLOCK3_A, height=1, bg = "#F8D605")
            p3B1DL.place(x=650, y=280)

            p3B2DL = Label(self.root, textvariable=self.P3_BLOCK3_V, height=1, bg = "#F8D605")
            p3B2DL.place(x=650, y=300)


            #BLOCK 3 INFORMATION
            lbl_block3_1 = Label(window, text="Block 3", width=10, height=1, bg = "#5dd39e")
            lbl_block3_1.place(x=5, y=340)
            lbl_block3_2 = Label(window, text="Bit Satate", width=10, height=1, bg = "#5dd39e")
            lbl_block3_2.place(x=5, y=360)
            lbl_block3_3 = Label(window, text="Address", width=10, height=1,  bg = "#5dd39e")
            lbl_block3_3.place(x=5, y=380)
            lbl_block3_4 = Label(window, text="Value", width=10, height=1, bg = "#5dd39e")
            lbl_block3_4.place(x=5, y=400)


            #Processor 0
            p0B0DL = Label(self.root, textvariable=self.P0_BLOCK4_S, height=1, bg = "#CE4912")
            p0B0DL.place(x=200, y=360)

            p0B1DL = Label(self.root, textvariable=self.P0_BLOCK4_A, height=1, bg = "#CE4912")
            p0B1DL.place(x=200, y=380)

            p0B2DL = Label(self.root, textvariable=self.P0_BLOCK4_V, height=1, bg = "#CE4912")
            p0B2DL.place(x=200, y=400)

            #Processor 1
            p1B0DL = Label(self.root, textvariable=self.P1_BLOCK4_S, height=1, bg = "#F36B1C")
            p1B0DL.place(x=350, y=360)

            p1B1DL = Label(self.root, textvariable=self.P1_BLOCK4_A, height=1, bg = "#F36B1C")
            p1B1DL.place(x=350, y=380)

            p1B2DL = Label(self.root, textvariable=self.P1_BLOCK4_V, height=1, bg = "#F36B1C")
            p1B2DL.place(x=350, y=400)

            #Processor 2
            p2B0DL = Label(self.root, textvariable=self.P2_BLOCK4_S, height=1, bg = "#0B6AB0")
            p2B0DL.place(x=500, y=360)

            p2B1DL = Label(self.root, textvariable=self.P2_BLOCK4_A, height=1, bg = "#0B6AB0")
            p2B1DL.place(x=500, y=380)

            p2B2DL = Label(self.root, textvariable=self.P2_BLOCK4_V, height=1, bg = "#0B6AB0")
            p2B2DL.place(x=500, y=400)

            #Processor 3
            p2B0DL = Label(self.root, textvariable=self.P3_BLOCK4_S, height=1, bg = "#F8D605")
            p2B0DL.place(x=650, y=360)

            p3B1DL = Label(self.root, textvariable=self.P3_BLOCK4_A, height=1, bg = "#F8D605")
            p3B1DL.place(x=650, y=380)

            p3B2DL = Label(self.root, textvariable=self.P3_BLOCK4_V, height=1, bg = "#F8D605")
            p3B2DL.place(x=650, y=400)



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
            lbl_allocate0 = Label(window,  bg = "#FFE373",  textvariable=self.CELL0)
            lbl_allocate0.place(x=420, y=480)

            lbl_allocate1 = Label(window,  bg = "#FFE373",  textvariable=self.CELL1)
            lbl_allocate1.place(x=420, y=500)

            lbl_allocate2 = Label(window,  bg = "#FFE373",  textvariable=self.CELL2)
            lbl_allocate2.place(x=420, y=520)

            lbl_allocate3 = Label(window, bg = "#FFE373",  textvariable=self.CELL3)
            lbl_allocate3.place(x=420, y=540)

            lbl_allocate4 = Label(window,  bg = "#FFE373",  textvariable=self.CELL4)
            lbl_allocate4.place(x=420, y=560)

            lbl_allocate5 = Label(window,  bg = "#FFE373",  textvariable=self.CELL5)
            lbl_allocate5.place(x=420, y=580)

            lbl_allocate6 = Label(window,  bg = "#FFE373",  textvariable=self.CELL6)
            lbl_allocate6.place(x=420, y=600)

            lbl_allocate7 = Label(window,  bg = "#FFE373", textvariable=self.CELL7)
            lbl_allocate7.place(x=420, y=620)

    #Set all processor to the threading 
    def Thread_Processors(self):

      bus_ = self.bus
      p0 = Processor(0, bus_)
      p1 = Processor(1, bus_)
      p2 = Processor(2, bus_)
      p3 = Processor(3, bus_)
      self.processors = [p0,p1,p2,p3]
      self.bus.processors = self.processors

      UIThread = threading.Thread(target=self.updateUI, daemon=True)
      UIThread.start()


    def updateUI(self ):
        

      while 1:
        #self.P0AInst.set(self.processors[0].instRunning)
        #self.P0LInst.set(self.processors[0].lastInst)
        
        self.P0_BLOCK1_S.set(self.processors[0].control.cache.getBlock(0).bitState)
        self.P0_BLOCK2_S.set(self.processors[0].control.cache.getBlock(1).bitState)
        self.P0_BLOCK3_S.set(self.processors[0].control.cache.getBlock(2).bitState)
        self.P0_BLOCK4_S.set(self.processors[0].control.cache.getBlock(3).bitState)
        
        self.P0_BLOCK1_V.set(hex(self.processors[0].control.cache.getBlock(0).data)[2:])
        self.P0_BLOCK2_V.set(hex(self.processors[0].control.cache.getBlock(1).getData())[2:])
        self.P0_BLOCK3_V.set(hex(self.processors[0].control.cache.getBlock(2).getData())[2:])
        self.P0_BLOCK4_V.set(hex(self.processors[0].control.cache.getBlock(3).getData())[2:])
        
        self.P0_BLOCK1_A.set(bin(self.processors[0].control.cache.getBlock(0).memoryAddress)[2:])
        self.P0_BLOCK2_A.set(bin(self.processors[0].control.cache.getBlock(1).memoryAddress)[2:])
        self.P0_BLOCK3_A.set(bin(self.processors[0].control.cache.getBlock(2).memoryAddress)[2:])
        self.P0_BLOCK4_A.set(bin(self.processors[0].control.cache.getBlock(3).memoryAddress)[2:])
        
        #self.P1AInst.set(self.processors[1].instRunning)
        #self.P1LInst.set(self.processors[1].lastInst)
        self.P1_BLOCK1_S.set(self.processors[1].control.cache.getBlock(0).bitState)
        self.P1_BLOCK2_S.set(self.processors[1].control.cache.getBlock(1).bitState)
        self.P1_BLOCK3_S.set(self.processors[1].control.cache.getBlock(2).bitState)
        self.P1_BLOCK4_S.set(self.processors[1].control.cache.getBlock(3).bitState)

        self.P1_BLOCK1_V.set(hex(self.processors[1].control.cache.getBlock(0).data)[2:])
        self.P1_BLOCK2_V.set(hex(self.processors[1].control.cache.getBlock(1).getData())[2:])
        self.P1_BLOCK3_V.set(hex(self.processors[1].control.cache.getBlock(2).getData())[2:])
        self.P1_BLOCK4_V.set(hex(self.processors[1].control.cache.getBlock(3).getData())[2:])

        self.P1_BLOCK1_A.set(bin(self.processors[1].control.cache.getBlock(0).memoryAddress)[2:])
        self.P1_BLOCK2_A.set(bin(self.processors[1].control.cache.getBlock(1).memoryAddress)[2:])
        self.P1_BLOCK3_A.set(bin(self.processors[1].control.cache.getBlock(2).memoryAddress)[2:])
        self.P1_BLOCK4_A.set(bin(self.processors[1].control.cache.getBlock(3).memoryAddress)[2:])
        
        #self.P2AInst.set(self.processors[2].instRunning)
        #self.P2LInst.set(self.processors[2].lastInst)
        self.P2_BLOCK1_S.set(self.processors[2].control.cache.getBlock(0).bitState)
        self.P2_BLOCK2_S.set(self.processors[2].control.cache.getBlock(1).bitState)
        self.P2_BLOCK3_S.set(self.processors[2].control.cache.getBlock(2).bitState)
        self.P2_BLOCK4_S.set(self.processors[2].control.cache.getBlock(3).bitState)

        self.P2_BLOCK1_V.set(hex(self.processors[2].control.cache.getBlock(0).data)[2:])
        self.P2_BLOCK2_V.set(hex(self.processors[2].control.cache.getBlock(1).getData())[2:])
        self.P2_BLOCK3_V.set(hex(self.processors[2].control.cache.getBlock(2).getData())[2:])
        self.P2_BLOCK4_V.set(hex(self.processors[2].control.cache.getBlock(3).getData())[2:])

        self.P2_BLOCK1_A.set(bin(self.processors[2].control.cache.getBlock(0).memoryAddress)[2:])
        self.P2_BLOCK2_A.set(bin(self.processors[2].control.cache.getBlock(1).memoryAddress)[2:])
        self.P2_BLOCK3_A.set(bin(self.processors[2].control.cache.getBlock(2).memoryAddress)[2:])
        self.P2_BLOCK4_A.set(bin(self.processors[2].control.cache.getBlock(3).memoryAddress)[2:])
        
        #self.P3AInst.set(self.processors[3].instRunning)
        #self.P3LInst.set(self.processors[3].lastInst)
        self.P3_BLOCK1_S.set(self.processors[3].control.cache.getBlock(0).bitState)
        self.P3_BLOCK2_S.set(self.processors[3].control.cache.getBlock(1).bitState)
        self.P3_BLOCK3_S.set(self.processors[3].control.cache.getBlock(2).bitState)
        self.P3_BLOCK4_S.set(self.processors[3].control.cache.getBlock(3).bitState)

        self.P3_BLOCK1_V.set(hex(self.processors[3].control.cache.getBlock(0).data)[2:])
        self.P3_BLOCK2_V.set(hex(self.processors[3].control.cache.getBlock(1).getData())[2:])
        self.P3_BLOCK3_V.set(hex(self.processors[3].control.cache.getBlock(2).getData())[2:])
        self.P3_BLOCK4_V.set(hex(self.processors[3].control.cache.getBlock(3).getData())[2:])
        
        self.P3_BLOCK1_A.set(bin(self.processors[3].control.cache.getBlock(0).memoryAddress)[2:])
        self.P3_BLOCK2_A.set(bin(self.processors[3].control.cache.getBlock(1).memoryAddress)[2:])
        self.P3_BLOCK3_A.set(bin(self.processors[3].control.cache.getBlock(2).memoryAddress)[2:])
        self.P3_BLOCK4_A.set(bin(self.processors[3].control.cache.getBlock(3).memoryAddress)[2:])
      

        self.CELL0.set(hex(self.memory.read(0))[2:])
        self.CELL1.set(hex(self.memory.read(1))[2:])
        self.CELL2.set(hex(self.memory.read(2))[2:])
        self.CELL3.set(hex(self.memory.read(3))[2:])
        self.CELL4.set(hex(self.memory.read(4))[2:])
        self.CELL5.set(hex(self.memory.read(5))[2:])
        self.CELL6.set(hex(self.memory.read(6))[2:])
        self.CELL7.set(hex(self.memory.read(7))[2:])
 
        time.sleep(0.1)


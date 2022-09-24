from tkinter import *
from  tkinter import ttk
import tkinter
from threading import *
from Functions import *

# main window
class GUI(tkinter.Tk):

    def __init__(root):

        #Initialize processors and design features 


        # create Processors
        root.processor_0 = CPU(0)   #Processor 0 instance
        root.processor_1 = CPU(1)   #Processor 1 instance
        root.processor_2 = CPU(2)   #Processor 2 instance
        root.processor_3 = CPU(3)   #Processor 3 instance

        root.Array_list = [root.processor_0, root.processor_1, root.processor_2, root.processor_3]  #create CPUs array
        root.mainMemory = MainMemory()                                #create main memory
        root.bus = Bus(root.Array_list, root.mainMemory)                #create bus

        root.stopFlag = 1    # Stop Signal
        
        #MAIN WINDOW CONFIGURATION 
        tkinter.Tk.__init__(root)
        root.title("MESI PROTOCOL SIMULATOR")
        root.geometry("1300x700")
        root.resizable(True,True)
        root.configure(bg = "#FCEE91")
        
        #WINDOW ELEMENTS 
        
        # Create an instance of Style widget
        style = ttk.Style()
        style.theme_use("clam")
        ttk.Style().configure("Treeview.Heading",background = "#bce784",foreground="Black")

        # cpu tittle frame
        CpuLayout = Frame(root)
        CpuLayout.place(anchor = "center", relx = 0.5, rely = 0.17)
        ColumnName = ("Tittle")


        """
        ---------------------------------------------- CONTAINER FIRST PROCESSOR ----------------------------------------
        
        """
        # treeview processor_0 title
        CpuLayout.processor_0Title = ttk.Treeview(CpuLayout, columns = ColumnName, show = "headings", height = 0, selectmode = "none")

        CpuLayout.processor_0Title.column("#0", width = 0, stretch = NO)
        CpuLayout.processor_0Title.column("Tittle", anchor = CENTER, width = 310, stretch = NO)

        CpuLayout.processor_0Title.heading("#0", text = "", anchor = CENTER)
        CpuLayout.processor_0Title.heading("Tittle", text = "Processor 0", anchor = CENTER)

        CpuLayout.processor_0Title.pack(padx = 10, pady = 0, side = LEFT)

        controller0 = root.processor_0.getController()   #Initialize controller processor 0
        cache0 = controller0.getCache()           #Set cachce processor 0
        blocks0 = cache0.getBlocks()              #Set block information for each isntance 

        values0 = []
        
        #Create the first instances for the blocks and its values 
        for block in blocks0:
            number = "B" + str(block.getNumber())
            state = block.getState()
            memoryDirection = "0b" + "{0:04b}".format(block.getMemoryDirection())
            value = "0x" + "{0:016x}".format(block.getValue())

            item = (number, state, memoryDirection, value)

            values0.append(item)

        #CPU FRAME 
        root.layout = Frame(root)
        root.layout.place(anchor = "center", relx = 0.5, rely = 0.27)
        cpuColumns = ("Block", "State", "Direction", "Value")   #CPU values according to it columns 


        root.layout.Container0 = ttk.Treeview(root.layout, columns = cpuColumns, show = "headings", height = 4, selectmode = "none")

        #Coloumns Set Configuration
        root.layout.Container0.column("#0", width = 0, stretch = NO)
        root.layout.Container0.column("Block", anchor = CENTER, width = 50, stretch = NO)
        root.layout.Container0.column("State", anchor = CENTER, width = 50, stretch = NO)
        root.layout.Container0.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        root.layout.Container0.column("Value", anchor = CENTER, width = 130, stretch = NO)

        root.layout.Container0.heading("#0", text = "", anchor = CENTER)
        root.layout.Container0.heading("Block", text = "Block", anchor = CENTER)
        root.layout.Container0.heading("State", text = "State", anchor = CENTER)
        root.layout.Container0.heading("Direction", text = "Direction", anchor = CENTER)
        root.layout.Container0.heading("Value", text = "Value", anchor = CENTER)

        root.layout.Container0.insert(parent = "", index = "end", iid = 0, text = "", values = values0[0], tags = ['t1'])
        root.layout.Container0.insert(parent = "", index = "end", iid = 1, text = "", values = values0[1], tags = ['t2'])
        root.layout.Container0.insert(parent = "", index = "end", iid = 2, text = "", values = values0[2], tags = ['t3'])
        root.layout.Container0.insert(parent = "", index = "end", iid = 3, text = "", values = values0[3], tags = ['t4'])

        root.layout.Container0.tag_configure('t1', background = "#CE4912")
        root.layout.Container0.tag_configure('t2', background = "#CE4912")
        root.layout.Container0.tag_configure('t3', background = "#CE4912")
        root.layout.Container0.tag_configure('t4', background = "#CE4912")

        root.layout.Container0.pack(padx = 10, pady = 0, side = LEFT)


        """
        -------------------------------------END FIRST CONTAINER PROCESSOR 0---------------------------------------------
        """





        """"
        --------------------------------------- CONTAINER SECOND PROCESSOR ---------------------------------------------
        """

        # treeview processor_1 title
        CpuLayout.processor_1Title = ttk.Treeview(CpuLayout, columns = ColumnName, show = "headings", height = 0, selectmode = "none")

        CpuLayout.processor_1Title.column("#0", width = 0, stretch = NO)
        CpuLayout.processor_1Title.column("Tittle", anchor = CENTER, width = 310, stretch = NO)

        CpuLayout.processor_1Title.heading("#0", text = "", anchor = CENTER)
        CpuLayout.processor_1Title.heading("Tittle", text = "Processor 1", anchor = CENTER)

        CpuLayout.processor_1Title.pack(padx = 10, pady = 0, side = LEFT)

        #CONTAINER PROCESSOR 1
        controller1 = root.processor_1.getController()
        cache1 = controller1.getCache()
        blocks1 = cache1.getBlocks()

        values1 = []

        for block in blocks1:
            number = "B" + str(block.getNumber())
            state = block.getState()
            memoryDirection = "0b" + "{0:04b}".format(block.getMemoryDirection())
            value = "0x" + "{0:016x}".format(block.getValue())

            item = (number, state, memoryDirection, value)

            values1.append(item)

        # treeview processor_1
        root.layout.Container1 = ttk.Treeview(root.layout, columns = cpuColumns, show = "headings", height = 4, selectmode = "none")

        #Coloumns Set Configuration
        root.layout.Container1.column("#0", width = 0, stretch = NO)
        root.layout.Container1.column("Block", anchor = CENTER, width = 50, stretch = NO)
        root.layout.Container1.column("State", anchor = CENTER, width = 50, stretch = NO)
        root.layout.Container1.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        root.layout.Container1.column("Value", anchor = CENTER, width = 130, stretch = NO)

        root.layout.Container1.heading("#0", text = "", anchor = CENTER)
        root.layout.Container1.heading("Block", text = "Block", anchor = CENTER)
        root.layout.Container1.heading("State", text = "State", anchor = CENTER)
        root.layout.Container1.heading("Direction", text = "Direction", anchor = CENTER)
        root.layout.Container1.heading("Value", text = "Value", anchor = CENTER)

        root.layout.Container1.insert(parent = "", index = "end", iid = 0, text = "", values = values1[0],tags=['b1'])
        root.layout.Container1.insert(parent = "", index = "end", iid = 1, text = "", values = values1[1],tags=['b2'])
        root.layout.Container1.insert(parent = "", index = "end", iid = 2, text = "", values = values1[2],tags=['b3'])
        root.layout.Container1.insert(parent = "", index = "end", iid = 3, text = "", values = values1[3],tags=['b4'])

        root.layout.Container1.tag_configure('b1', background = "#F36B1C")
        root.layout.Container1.tag_configure('b2', background = "#F36B1C")
        root.layout.Container1.tag_configure('b3', background = "#F36B1C")
        root.layout.Container1.tag_configure('b4', background = "#F36B1C")

        root.layout.Container1.pack(padx = 10, pady = 0, side = LEFT)

        """
        -------------------------------------END SECOND CONTAINER PROCESSOR 1---------------------------------------------
        """




        """"
        --------------------------------------- CONTAINER THIRD PROCESSOR ---------------------------------------------
        """


        # treeview processor_2 title
        CpuLayout.processor_2Title = ttk.Treeview(CpuLayout, columns = ColumnName, show = "headings", height = 0, selectmode = "none")

        CpuLayout.processor_2Title.column("#0", width = 0, stretch = NO)
        CpuLayout.processor_2Title.column("Tittle", anchor = CENTER, width = 310, stretch = NO)

        CpuLayout.processor_2Title.heading("#0", text = "", anchor = CENTER)
        CpuLayout.processor_2Title.heading("Tittle", text = "Processor 2", anchor = CENTER)

        CpuLayout.processor_2Title.pack(padx = 10, pady = 0, side = LEFT)

        controller2 = root.processor_2.getController()
        cache2 = controller2.getCache()
        blocks2 = cache2.getBlocks()

        values2 = []

        for block in blocks2:
            number = "B" + str(block.getNumber())
            state = block.getState()
            memoryDirection = "0b" + "{0:04b}".format(block.getMemoryDirection())
            value = "0x" + "{0:016x}".format(block.getValue())

            item = (number, state, memoryDirection, value)

            values2.append(item)

        # treeview processor_2
        root.layout.Container2 = ttk.Treeview(root.layout, columns = cpuColumns, show = "headings", height = 4, selectmode = "none")

        #Coloumns Set Configuration
        root.layout.Container2.column("#0", width = 0, stretch = NO)
        root.layout.Container2.column("Block", anchor = CENTER, width = 50, stretch = NO)
        root.layout.Container2.column("State", anchor = CENTER, width = 50, stretch = NO)
        root.layout.Container2.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        root.layout.Container2.column("Value", anchor = CENTER, width = 130, stretch = NO)

        root.layout.Container2.heading("#0", text = "", anchor = CENTER)
        root.layout.Container2.heading("Block", text = "Block", anchor = CENTER)
        root.layout.Container2.heading("State", text = "State", anchor = CENTER)
        root.layout.Container2.heading("Direction", text = "Direction", anchor = CENTER)
        root.layout.Container2.heading("Value", text = "Value", anchor = CENTER)

        root.layout.Container2.insert(parent = "", index = "end", iid = 0, text = "", values = values2[0], tags = ['a1'])
        root.layout.Container2.insert(parent = "", index = "end", iid = 1, text = "", values = values2[1], tags = ['a2'])
        root.layout.Container2.insert(parent = "", index = "end", iid = 2, text = "", values = values2[2], tags = ['a3'])
        root.layout.Container2.insert(parent = "", index = "end", iid = 3, text = "", values = values2[3], tags = ['a4'])

        root.layout.Container2.tag_configure('a1', background = "#0B6AB0")
        root.layout.Container2.tag_configure('a2', background = "#0B6AB0")
        root.layout.Container2.tag_configure('a3', background = "#0B6AB0")
        root.layout.Container2.tag_configure('a4', background = "#0B6AB0")

        root.layout.Container2.pack(padx = 10, pady = 0, side = LEFT)

        """
        -------------------------------------END THIRD CONTAINER PROCESSOR 2---------------------------------------------
        """



        """"
        --------------------------------------- CONTAINER FOURTH PROCESSOR ---------------------------------------------
        """

        # treeview processor_3 title
        CpuLayout.processor_3Title = ttk.Treeview(CpuLayout, columns = ColumnName, show = "headings", height = 0, selectmode = "none")

        CpuLayout.processor_3Title.column("#0", width = 0, stretch = NO)
        CpuLayout.processor_3Title.column("Tittle", anchor = CENTER, width = 310, stretch = NO)

        CpuLayout.processor_3Title.heading("#0", text = "", anchor = CENTER)
        CpuLayout.processor_3Title.heading("Tittle", text = "Processor 3", anchor = CENTER)

        CpuLayout.processor_3Title.pack(padx = 10, pady = 0, side = LEFT)

       
        controller3 = root.processor_3.getController()
        cache3 = controller3.getCache()
        blocks3 = cache3.getBlocks()

        values3 = []

        for block in blocks3:
            number = "B" + str(block.getNumber())
            state = block.getState()
            memoryDirection = "0b" + "{0:04b}".format(block.getMemoryDirection())
            value = "0x" + "{0:016x}".format(block.getValue())

            item = (number, state, memoryDirection, value)

            values3.append(item)

        # treeview processor_3
        root.layout.Container3 = ttk.Treeview(root.layout, columns = cpuColumns, show = "headings", height = 4, selectmode = "none")

        #Coloumns Set Configuration
        root.layout.Container3.column("#0", width = 0, stretch = NO)
        root.layout.Container3.column("Block", anchor = CENTER, width = 50, stretch = NO)
        root.layout.Container3.column("State", anchor = CENTER, width = 50, stretch = NO)
        root.layout.Container3.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        root.layout.Container3.column("Value", anchor = CENTER, width = 130, stretch = NO)

        root.layout.Container3.heading("#0", text = "", anchor = CENTER)
        root.layout.Container3.heading("Block", text = "Block", anchor = CENTER)
        root.layout.Container3.heading("State", text = "State", anchor = CENTER)
        root.layout.Container3.heading("Direction", text = "Direction", anchor = CENTER)
        root.layout.Container3.heading("Value", text = "Value", anchor = CENTER)

        root.layout.Container3.insert(parent = "", index = "end", iid = 0, text = "", values = values3[0], tags=['d1'])
        root.layout.Container3.insert(parent = "", index = "end", iid = 1, text = "", values = values3[1], tags=['d2'])
        root.layout.Container3.insert(parent = "", index = "end", iid = 2, text = "", values = values3[2], tags=['d3'])
        root.layout.Container3.insert(parent = "", index = "end", iid = 3, text = "", values = values3[3], tags=['d4'])

        root.layout.Container3.tag_configure('d1', background = "#F8D605")
        root.layout.Container3.tag_configure('d2', background = "#F8D605")
        root.layout.Container3.tag_configure('d3', background = "#F8D605")
        root.layout.Container3.tag_configure('d4', background = "#F8D605")

        root.layout.Container3.pack(padx = 10, pady = 0, side = LEFT)

        """
        -------------------------------------END FOURTH CONTAINER PROCESSOR ---------------------------------------------
        """


        """
        -------------------------------------------BUS SECTION-------------------------------------------------
        """
        # bus 

        bus_label_ = Label(bg = "red", width= 1312, height= 2, text="BUS", fg="black")
        bus_label_.place(x=600, y = 270)

        bus_label = Label(bg = "red", width= 1312, height= 2, text="BUS", fg="black")
        bus_label.place(x=0, y = 270)

        

        """
        -------------------------------------------END BUS SECTION--------------------------------------------
        """

        """
        -------------------------------------------MAIN MEMORY SECTION-------------------------------------------------
        """ 

        # main memory frame
        root.Memlayout = Frame(root)
        root.Memlayout.place(anchor = "center", relx = 0.5, rely = 0.65)

        mainMemoryColumns = ("Direction", "Value")

        dictionary = root.mainMemory.getDictionary()

        keys = dictionary.keys()

        keyArray = []

        for key in keys:

            keyArray.append(key)

        # treeview main memory
        root.Memlayout.MMContainer = ttk.Treeview(root.Memlayout, columns = mainMemoryColumns, show = "headings", height = 8, selectmode = "none")

        root.Memlayout.MMContainer.column("#0", width = 0, stretch = NO)
        root.Memlayout.MMContainer.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        root.Memlayout.MMContainer.column("Value", anchor = CENTER, width = 130, stretch = NO)

        root.Memlayout.MMContainer.heading("#0", text = "", anchor = CENTER)
        root.Memlayout.MMContainer.heading("Direction", text = "Direction", anchor = CENTER)
        root.Memlayout.MMContainer.heading("Value", text = "Value", anchor = CENTER)

        root.Memlayout.MMContainer.insert(parent = "", index = "end", iid = 0, text = "", values = ("0b" + "{0:04b}".format(keyArray[0]), "0x" + "{0:016x}".format(dictionary[keyArray[0]])), tags=['b1'])
        root.Memlayout.MMContainer.insert(parent = "", index = "end", iid = 1, text = "", values = ("0b" + "{0:04b}".format(keyArray[1]), "0x" + "{0:016x}".format(dictionary[keyArray[1]])), tags=['b2'])
        root.Memlayout.MMContainer.insert(parent = "", index = "end", iid = 2, text = "", values = ("0b" + "{0:04b}".format(keyArray[2]), "0x" + "{0:016x}".format(dictionary[keyArray[2]])), tags=['b3'])
        root.Memlayout.MMContainer.insert(parent = "", index = "end", iid = 3, text = "", values = ("0b" + "{0:04b}".format(keyArray[3]), "0x" + "{0:016x}".format(dictionary[keyArray[3]])), tags=['b4'])
        root.Memlayout.MMContainer.insert(parent = "", index = "end", iid = 4, text = "", values = ("0b" + "{0:04b}".format(keyArray[4]), "0x" + "{0:016x}".format(dictionary[keyArray[4]])), tags=['b5'])
        root.Memlayout.MMContainer.insert(parent = "", index = "end", iid = 5, text = "", values = ("0b" + "{0:04b}".format(keyArray[5]), "0x" + "{0:016x}".format(dictionary[keyArray[5]])), tags=['b6'])
        root.Memlayout.MMContainer.insert(parent = "", index = "end", iid = 6, text = "", values = ("0b" + "{0:04b}".format(keyArray[6]), "0x" + "{0:016x}".format(dictionary[keyArray[6]])), tags=['b7'])
        root.Memlayout.MMContainer.insert(parent = "", index = "end", iid = 7, text = "", values = ("0b" + "{0:04b}".format(keyArray[7]), "0x" + "{0:016x}".format(dictionary[keyArray[7]])), tags=['b8'])

        #Color memory blocks
        root.Memlayout.MMContainer.tag_configure('b1', background = "#D2B4DE")
        root.Memlayout.MMContainer.tag_configure('b2', background = "#FFB5FB")
        root.Memlayout.MMContainer.tag_configure('b3', background = "#F1C40F")
        root.Memlayout.MMContainer.tag_configure('b4', background = "#82E0AA")
        root.Memlayout.MMContainer.tag_configure('b5', background = "#3498DB")
        root.Memlayout.MMContainer.tag_configure('b6', background = "#EC7063")
        root.Memlayout.MMContainer.tag_configure('b7', background = "#8DFF33")
        root.Memlayout.MMContainer.tag_configure('b8', background = "#F9E79F")
        
        root.Memlayout.MMContainer.pack(side = BOTTOM)


        #---------------------------------------LAST INSTRUCCON-----------------------------------------------------
        # last instruction tittle frame
        lastInstructionTittleFrame = Frame(root)
        lastInstructionTittleFrame.place(anchor = "center", relx = 0.168, rely = 0.535)

        # last instruction tittle column
        lastInstructionTittleColumn = ("Tittle")

        # treeview last instruction
        lastInstructionTittleFrame.lastInstructionTittle = ttk.Treeview(lastInstructionTittleFrame, columns = lastInstructionTittleColumn, show = "headings", height = 0, selectmode = "none")

        lastInstructionTittleFrame.lastInstructionTittle.column("#0", width = 0, stretch = NO)
        lastInstructionTittleFrame.lastInstructionTittle.column("Tittle", anchor = CENTER, width = 420, stretch = NO)
        
        lastInstructionTittleFrame.lastInstructionTittle.heading("#0", text = "", anchor = CENTER)
        lastInstructionTittleFrame.lastInstructionTittle.heading("Tittle", text = "Last instruction Executed", anchor = CENTER)

        lastInstructionTittleFrame.lastInstructionTittle.pack(padx = 10, pady = 0, side = LEFT)

        # last instruction frame
        root.li_layout = Frame(root)
        root.li_layout.place(anchor = "center", relx = 0.168, rely = 0.636)

        instructionColumns = ("CPU", "Instruction", "Read Miss", "Write Miss")

        # treeview instruction
        root.li_layout.InstructionContainer = ttk.Treeview(root.li_layout, columns = instructionColumns, show = "headings", height = 4, selectmode = "none")

        root.li_layout.InstructionContainer.column("#0", width = 0, stretch = NO)
        root.li_layout.InstructionContainer.column("CPU", anchor = CENTER, width = 40, stretch = NO)
        root.li_layout.InstructionContainer.column("Instruction", anchor = CENTER, width = 220, stretch = NO)
        root.li_layout.InstructionContainer.column("Read Miss", anchor = CENTER, width = 80, stretch = NO)
        root.li_layout.InstructionContainer.column("Write Miss", anchor = CENTER, width = 80, stretch = NO)

        root.li_layout.InstructionContainer.heading("#0", text = "", anchor = CENTER)
        root.li_layout.InstructionContainer.heading("CPU", text = "CPU", anchor = CENTER)
        root.li_layout.InstructionContainer.heading("Instruction", text = "Instruction", anchor = CENTER)
        root.li_layout.InstructionContainer.heading("Read Miss", text = "Read Miss", anchor = CENTER)
        root.li_layout.InstructionContainer.heading("Write Miss", text = "Write Miss", anchor = CENTER)

        root.li_layout.InstructionContainer.insert(parent = "", index = "end", iid = 0, text = "", values = ("N0", None, "0", "0"),tags = ['j1'])
        root.li_layout.InstructionContainer.insert(parent = "", index = "end", iid = 1, text = "", values = ("N1", None, "0", "0"),tags = ['j2'])
        root.li_layout.InstructionContainer.insert(parent = "", index = "end", iid = 2, text = "", values = ("N2", None, "0", "0"),tags = ['j3'])
        root.li_layout.InstructionContainer.insert(parent = "", index = "end", iid = 3, text = "", values = ("N3", None, "0", "0"),tags = ['j4'])

        root.li_layout.InstructionContainer.tag_configure('j1', background = "#D71E3A")
        root.li_layout.InstructionContainer.tag_configure('j2', background = "#D71E3A")
        root.li_layout.InstructionContainer.tag_configure('j3', background = "#D71E3A")
        root.li_layout.InstructionContainer.tag_configure('j4', background = "#D71E3A")


        root.li_layout.InstructionContainer.pack(side = LEFT)

        # current instruction tittle frame
        currentInstructionTittleFrame = Frame(root)
        currentInstructionTittleFrame.place(anchor = "center", relx = 0.168, rely = 0.77)

        # last instruction tittle column
        currentInstructionTittleColumn = ("Tittle")

        # treeview last instruction
        currentInstructionTittleFrame.currentInstructionTittle = ttk.Treeview(currentInstructionTittleFrame, columns = currentInstructionTittleColumn, show = "headings", height = 0, selectmode = "none")

        currentInstructionTittleFrame.currentInstructionTittle.column("#0", width = 0, stretch = NO)
        currentInstructionTittleFrame.currentInstructionTittle.column("Tittle", anchor = CENTER, width = 420, stretch = NO)
        
        currentInstructionTittleFrame.currentInstructionTittle.heading("#0", text = "", anchor = CENTER)
        currentInstructionTittleFrame.currentInstructionTittle.heading("Tittle", text = "Current Intruction Executing", anchor = CENTER)

        currentInstructionTittleFrame.currentInstructionTittle.pack(padx = 10, pady = 0, side = LEFT)

        # current instruction frame
        root.ci_layout = Frame(root)
        root.ci_layout.place(anchor = "center", relx = 0.168, rely = 0.87)

        # treeview instruction
        root.ci_layout.InstructionContainer = ttk.Treeview(root.ci_layout, columns = instructionColumns, show = "headings", height = 4, selectmode = "none")

        root.ci_layout.InstructionContainer.column("#0", width = 0, stretch = NO)
        root.ci_layout.InstructionContainer.column("CPU", anchor = CENTER, width = 40, stretch = NO)
        root.ci_layout.InstructionContainer.column("Instruction", anchor = CENTER, width = 220, stretch = NO)
        root.ci_layout.InstructionContainer.column("Read Miss", anchor = CENTER, width = 80, stretch = NO)
        root.ci_layout.InstructionContainer.column("Write Miss", anchor = CENTER, width = 80, stretch = NO)

        root.ci_layout.InstructionContainer.heading("#0", text = "", anchor = CENTER)
        root.ci_layout.InstructionContainer.heading("CPU", text = "CPU", anchor = CENTER)
        root.ci_layout.InstructionContainer.heading("Instruction", text = "Instruction", anchor = CENTER)
        root.ci_layout.InstructionContainer.heading("Read Miss", text = "Read Miss", anchor = CENTER)
        root.ci_layout.InstructionContainer.heading("Write Miss", text = "Write Miss", anchor = CENTER)

        root.ci_layout.InstructionContainer.insert(parent = "", index = "end", iid = 0, text = "", values = ("N0", None, "0", "0"), tags=['g1'])
        root.ci_layout.InstructionContainer.insert(parent = "", index = "end", iid = 1, text = "", values = ("N1", None, "0", "0"), tags=['g2'])
        root.ci_layout.InstructionContainer.insert(parent = "", index = "end", iid = 2, text = "", values = ("N2", None, "0", "0"), tags=['g3'])
        root.ci_layout.InstructionContainer.insert(parent = "", index = "end", iid = 3, text = "", values = ("N3", None, "0", "0"), tags=['g4'])

        root.ci_layout.InstructionContainer.tag_configure('g1', background = "#8C4966")
        root.ci_layout.InstructionContainer.tag_configure('g2', background = "#8C4966")
        root.ci_layout.InstructionContainer.tag_configure('g3', background = "#8C4966")
        root.ci_layout.InstructionContainer.tag_configure('g4', background = "#8C4966")

        root.ci_layout.InstructionContainer.pack(side = LEFT)

        buttonFrame = Frame(root)
        buttonFrame.place(anchor = "center", relx = 0.7985, rely = 0.539)

        # step by step button
        buttonFrame.stepByStepButton = Button(buttonFrame, text = "Step by Step", activebackground = "#FF8000", fg = "white", bg = "#1E1ED7", font = ("Italic", 13), width = 10, heigh = 1, command = root.stepByStep)
        buttonFrame.stepByStepButton.pack(padx = 10, pady = 0, side = LEFT)

        # continuos execution button
        buttonFrame.continuosExecutionButton = Button(buttonFrame, text = "START", activebackground = "#FF8000", fg = "white", bg = "#1E1ED7", font = ("Italic", 13), width = 20, heigh = 1, command = root.continuosExecution)
        buttonFrame.continuosExecutionButton.pack(padx = 10, pady = 0, side = LEFT)

        # stop button
        buttonFrame.stopButton = Button(buttonFrame, text = "STOP", activebackground = "#FF8000", fg = "white", bg = "#1E1ED7", font = ("Italic", 13), width = 10, heigh = 1, command = root.stop)
        buttonFrame.stopButton.pack(padx = 10, pady = 0, side = LEFT)

        # insert instruction tittle frame
        inst_layout = Frame(root)
        inst_layout.place(anchor = "center", relx = 0.795, rely = 0.625)

        # CPU label
        inst_layout.cpuLabel = Label(inst_layout, text = "Processor", fg =  "#1E1ED7", font = ("Italic", 14), bg = "#FCEE91")
        inst_layout.cpuLabel.pack(padx = 10, pady = 0, side = LEFT)
        
        # operation label
        inst_layout.operationLabel = Label(inst_layout, text = " Operation", fg =  "#1E1ED7", font = ("Italic", 14), bg = "#FCEE91")
        inst_layout.operationLabel.pack(padx = 10, pady = 0, side = LEFT)

        # direction label
        inst_layout.directionLabel = Label(inst_layout, text = "  Dir", fg =  "#1E1ED7", font = ("Italic", 14), bg = "#FCEE91")
        inst_layout.directionLabel.pack(padx = 10, pady = 0, side = LEFT)

        # value label
        inst_layout.valueLabel = Label(inst_layout, text = "     Value", fg =  "#1E1ED7", font = ("Italic", 14), bg = "#FCEE91")
        inst_layout.valueLabel.pack(padx = 10, pady = 0, side = LEFT)

        # insert instruction frame
        root.inst_instruction = Frame(root)
        root.inst_instruction.place(anchor = "center", relx = 0.79999, rely = 0.685)

        # CPU textBox
        root.inst_instruction.CpuTextBox = Entry(root.inst_instruction, width = 10, font = ("Italic", 13))
        root.inst_instruction.CpuTextBox.pack(padx = 10, pady = 0, side = LEFT)

        # operation textBox
        root.inst_instruction.operationTextBox = Entry(root.inst_instruction, width = 10, font = ("Italic", 13))
        root.inst_instruction.operationTextBox.pack(padx = 10, pady = 0, side = LEFT)

        # direction textBox
        root.inst_instruction.directionTextBox = Entry(root.inst_instruction, width = 10, font = ("Italic", 13))
        root.inst_instruction.directionTextBox.pack(padx = 10, pady = 0, side = LEFT)

        # value textBox
        root.inst_instruction.valueTextBox = Entry(root.inst_instruction, width = 10, font = ("Italic", 13))
        root.inst_instruction.valueTextBox.pack(padx = 10, pady = 0, side = LEFT)

        # load frame
        loadFrame = Frame(root)
        loadFrame.place(anchor = "center", relx = 0.7985, rely = 0.762)

        # load button
        loadFrame.loadButton = Button(loadFrame, text = "Add", activebackground = "#FF8000", fg = "white", bg = "#1E1ED7", font = ("Italic", 13), width = 20, heigh = 1, command = root.load)
        loadFrame.loadButton.pack(padx = 0, pady = 0, side = LEFT)


#---------------------------------------------------------------------------------------------------------------------------
#                                                           END GUI DESIGN
#-------------------------------------------------------------------------------------------------------------------------


    def ProcessoInformation(root):

        processor_cnt = 0
        block_pinter = 0

        for cpu in root.Array_list:

            controller = cpu.getController()
            cache = controller.getCache()
            blocks = cache.getBlocks()

            for block in blocks:

                number = "B" + str(block.getNumber())
                state = block.getState()
                memoryDirection = "0b" + "{0:04b}".format(block.getMemoryDirection())
                value = "0x" + "{0:016x}".format(block.getValue())
                blockValues = (number, state, memoryDirection, value)

                # block0
                if(block_pinter == 0):
                    # processor_0
                    if(processor_cnt == 0):
                        root.layout.Container0.item(block_pinter, text = "", values = blockValues)
                    # processor_1
                    elif(processor_cnt == 1):
                        root.layout.Container1.item(block_pinter, text = "", values = blockValues)
                    # processor_2
                    elif(processor_cnt == 2):
                        root.layout.Container2.item(block_pinter, text = "", values = blockValues)
                    # processor_3
                    else:
                        root.layout.Container3.item(block_pinter, text = "", values = blockValues)

                # block1
                elif(block_pinter == 1):
                    # procesor_0
                    if(processor_cnt == 0):
                        root.layout.Container0.item(block_pinter, text = "", values = blockValues)
                    # processor_1
                    elif(processor_cnt == 1):
                        root.layout.Container1.item(block_pinter, text = "", values = blockValues)
                    # processor_2
                    elif(processor_cnt == 2):
                        root.layout.Container2.item(block_pinter, text = "", values = blockValues)
                    # processor_3
                    else:
                        root.layout.Container3.item(block_pinter, text = "", values = blockValues)

                # block2
                elif(block_pinter == 3):
                    # processor_0
                    if(processor_cnt == 0):
                        root.layout.Container0.item(block_pinter, text = "", values = blockValues)
                    # processor_1
                    elif(processor_cnt == 1):
                        root.layout.Container1.item(block_pinter, text = "", values = blockValues)
                    # processor_2
                    elif(processor_cnt == 2):
                        root.layout.Container2.item(block_pinter, text = "", values = blockValues)
                    # processor_3
                    else:
                        root.layout.Container3.item(block_pinter, text = "", values = blockValues)

                # block3
                else:
                    # processor_0
                    if(processor_cnt == 0):
                        root.layout.Container0.item(block_pinter, text = "", values = blockValues)
                    # processor_1
                    elif(processor_cnt == 1):
                        root.layout.Container1.item(block_pinter, text = "", values = blockValues)
                    # processor_2
                    elif(processor_cnt == 2):
                        root.layout.Container2.item(block_pinter, text = "", values = blockValues)
                    # processor_3
                    else:
                        root.layout.Container3.item(block_pinter, text = "", values = blockValues)


                block_pinter += 1
            block_pinter = 0
            processor_cnt += 1

    def MainMemInformation(root):
        
        dictionary = root.mainMemory.getDictionary()
        keys = dictionary.keys()
        keyArray = []

        for key in keys:
            keyArray.append(key)
        index = 0

        for key in keyArray:
            mainMemoryValues = ("0b" + "{0:04b}".format(key), "0x" + "{0:016x}".format(dictionary[key]))
            root.Memlayout.MMContainer.item(index, text = "", values = mainMemoryValues)
            index += 1

    def LastInst(root):

        for index in range(0, 4):
            current = root.ci_layout.InstructionContainer.item(index)
            currentValues = tuple(current["values"])
            root.li_layout.InstructionContainer.item(index, text = "", values = currentValues)

    def CurrentInst(root):

        index = 0
        for cpu in root.Array_list:
            cpuNumber = "N" + str(cpu.getNumber())
            instruction = cpu.getCurrentInstruction()

            if(instruction is not None):
                operation = instruction.getOperation()
                # calc instruction
                if(operation == OPERATIONS[0]):
                    instruction = operation
                # not calc instruction
                else:
                    memoryDirection = instruction.getMemoryDirection()
                    # read instruction
                    if(operation == OPERATIONS[1]):
                        instruction = operation + "  0b" + "{0:04b}".format(memoryDirection)
                    # write instruction
                    else:
                        value = instruction.getValue()
                        instruction = operation + "  0b" + "{0:04b}".format(memoryDirection) + "; " + "0x" + "{0:016x}".format(value)

                controller = cpu.getController()
                readMiss = controller.getReadMiss()
                writeMiss = controller.getWriteMiss()
                instructionValues = (cpuNumber, instruction, readMiss, writeMiss)
                root.ci_layout.InstructionContainer.item(index, text = "", values = instructionValues)
                index += 1

    def EnableThread(root, cpu):

        if(cpu.getCurrentInstruction() is not None):
            root.LastInst()

        # not loaded instruction
        if(cpu.getLoaded() == 0):
            cpu.generateInstruction()          
            sleep(TIMER)

        # loaded instruction
        else:
            cpu.setLoaded(0)
        cpu.executeInstruction(root.bus)        
        root.CurrentInst()
        sleep(TIMER)       
        root.ProcessoInformation()
        root.MainMemInformation()

    def stepByStep(root):
        
        thread0 = Thread(target = root.EnableThread, args = (root.processor_0,))
        thread1 = Thread(target = root.EnableThread, args = (root.processor_1,))
        thread2 = Thread(target = root.EnableThread, args = (root.processor_2,))
        thread3 = Thread(target = root.EnableThread, args = (root.processor_3,))

        # start threads
        thread0.start()
        thread1.start()
        thread2.start()
        thread3.start()

    def Start(root):

        root.stopFlag = 0

        while(root.stopFlag == 0):

            # create threads
            thread0 = Thread(target = root.EnableThread, args = (root.processor_0,))
            thread1 = Thread(target = root.EnableThread, args = (root.processor_1,))
            thread2 = Thread(target = root.EnableThread, args = (root.processor_2,))
            thread3 = Thread(target = root.EnableThread, args = (root.processor_3,))

            # start threads
            thread0.start()
            thread1.start()
            thread2.start()
            thread3.start()

            sleep(TIMER * 2)

        print("stopd")

    def continuosExecution(root):

        # create thread
        Start = Thread(target = root.Start)
        # start thread
        Start.start()

    def stop(root):
        
        root.stopFlag = 1

    def load(root):

        if(root.stopFlag == 1):
        
            # get gata
            cpuNumber = root.inst_instruction.CpuTextBox.get()
            operation = root.inst_instruction.operationTextBox.get()
            memoryDirection = root.inst_instruction.directionTextBox.get()
            value = root.inst_instruction.valueTextBox.get()

            if(cpuNumber != "" and operation != ""):
                cpuNumber = int(cpuNumber)
                cpu = root.Array_list[cpuNumber]
                cpu.setLoaded(1)
                loadInstruction = Instruction(cpuNumber, operation)

                if(memoryDirection != ""):
                    memoryDirection = int(memoryDirection, 2)
                    loadInstruction.setMemoryDirection(memoryDirection)

                if(value != ""):
                    value = int(value, 16)
                    loadInstruction.setValue(value)

                cpu.setCurrentInstruction(loadInstruction)

                # clear textBoxes
                root.inst_instruction.CpuTextBox.delete(0, END)
                root.inst_instruction.operationTextBox.delete(0, END)
                root.inst_instruction.directionTextBox.delete(0, END)
                root.inst_instruction.valueTextBox.delete(0, END)

# window loop
GUI().mainloop()

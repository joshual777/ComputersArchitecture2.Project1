from tkinter import *
from  tkinter import ttk
import tkinter
from threading import *
from models import *

# main window
class Window(tkinter.Tk):

    def __init__(root):

        # create CPUs
        root.cpu0 = CPU(0)
        root.cpu1 = CPU(1)
        root.cpu2 = CPU(2)
        root.cpu3 = CPU(3)

        # create CPUs array
        root.cpuArray = [root.cpu0, root.cpu1, root.cpu2, root.cpu3]

        # create main memory
        root.mainMemory = MainMemory()

        # create bus
        root.bus = Bus(root.cpuArray, root.mainMemory)

        # pause flag
        root.pauseFlag = 1

        tkinter.Tk.__init__(root)

        # window title
        root.title("Proyecto 1")
        
        # size
        root.geometry("1350x700")

        # disable resizing
        root.resizable(False,False)

        # title
        root.title = Label(root, text = "Modelo de Protocolo para Coherencia de Caché en Sistemas Multiprocesador", fg = '#4285f4', font = ("Italic", 28))
        root.title.place(x = 35, y = 27)

        # Create an instance of Style widget
        style = ttk.Style()
        style.theme_use("clam")

        # cpu tittle frame
        cpuTittleFrame = Frame(root)
        cpuTittleFrame.place(anchor = "center", relx = 0.5, rely = 0.17)

        # cpu tittle column
        cpuTittleColumn = ("Tittle")

        # treeview cpu0 title
        cpuTittleFrame.cpu0Title = ttk.Treeview(cpuTittleFrame, columns = cpuTittleColumn, show = "headings", height = 0, selectmode = "none")

        cpuTittleFrame.cpu0Title.column("#0", width = 0, stretch = NO)
        cpuTittleFrame.cpu0Title.column("Tittle", anchor = CENTER, width = 310, stretch = NO)

        cpuTittleFrame.cpu0Title.heading("#0", text = "", anchor = CENTER)
        cpuTittleFrame.cpu0Title.heading("Tittle", text = "N0", anchor = W)

        cpuTittleFrame.cpu0Title.pack(padx = 10, pady = 0, side = LEFT)

        # treeview cpu1 title
        cpuTittleFrame.cpu1Title = ttk.Treeview(cpuTittleFrame, columns = cpuTittleColumn, show = "headings", height = 0, selectmode = "none")

        cpuTittleFrame.cpu1Title.column("#0", width = 0, stretch = NO)
        cpuTittleFrame.cpu1Title.column("Tittle", anchor = CENTER, width = 310, stretch = NO)

        cpuTittleFrame.cpu1Title.heading("#0", text = "", anchor = CENTER)
        cpuTittleFrame.cpu1Title.heading("Tittle", text = "N1", anchor = W)

        cpuTittleFrame.cpu1Title.pack(padx = 10, pady = 0, side = LEFT)

        # treeview cpu2 title
        cpuTittleFrame.cpu2Title = ttk.Treeview(cpuTittleFrame, columns = cpuTittleColumn, show = "headings", height = 0, selectmode = "none")

        cpuTittleFrame.cpu2Title.column("#0", width = 0, stretch = NO)
        cpuTittleFrame.cpu2Title.column("Tittle", anchor = CENTER, width = 310, stretch = NO)

        cpuTittleFrame.cpu2Title.heading("#0", text = "", anchor = CENTER)
        cpuTittleFrame.cpu2Title.heading("Tittle", text = "N2", anchor = W)

        cpuTittleFrame.cpu2Title.pack(padx = 10, pady = 0, side = LEFT)

        # treeview cpu3 title
        cpuTittleFrame.cpu3Title = ttk.Treeview(cpuTittleFrame, columns = cpuTittleColumn, show = "headings", height = 0, selectmode = "none")

        cpuTittleFrame.cpu3Title.column("#0", width = 0, stretch = NO)
        cpuTittleFrame.cpu3Title.column("Tittle", anchor = CENTER, width = 310, stretch = NO)

        cpuTittleFrame.cpu3Title.heading("#0", text = "", anchor = CENTER)
        cpuTittleFrame.cpu3Title.heading("Tittle", text = "N3", anchor = W)

        cpuTittleFrame.cpu3Title.pack(padx = 10, pady = 0, side = LEFT)

        controller0 = root.cpu0.getController()
        cache0 = controller0.getCache()
        blocks0 = cache0.getBlocks()

        values0 = []

        for block in blocks0:
            number = "B" + str(block.getNumber())
            state = block.getState()
            memoryDirection = "0b" + "{0:04b}".format(block.getMemoryDirection())
            value = "0x" + "{0:016x}".format(block.getValue())

            item = (number, state, memoryDirection, value)

            values0.append(item)

        # cpu frame
        root.cpuFrame = Frame(root)
        root.cpuFrame.place(anchor = "center", relx = 0.5, rely = 0.27)

        # cpu columns
        cpuColumns = ("Block", "State", "Direction", "Value")

        # treeview cpu0
        root.cpuFrame.cpu0Treeview = ttk.Treeview(root.cpuFrame, columns = cpuColumns, show = "headings", height = 4, selectmode = "none")

        root.cpuFrame.cpu0Treeview.column("#0", width = 0, stretch = NO)
        root.cpuFrame.cpu0Treeview.column("Block", anchor = CENTER, width = 50, stretch = NO)
        root.cpuFrame.cpu0Treeview.column("State", anchor = CENTER, width = 50, stretch = NO)
        root.cpuFrame.cpu0Treeview.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        root.cpuFrame.cpu0Treeview.column("Value", anchor = CENTER, width = 130, stretch = NO)

        root.cpuFrame.cpu0Treeview.heading("#0", text = "", anchor = CENTER)
        root.cpuFrame.cpu0Treeview.heading("Block", text = "Block", anchor = CENTER)
        root.cpuFrame.cpu0Treeview.heading("State", text = "State", anchor = CENTER)
        root.cpuFrame.cpu0Treeview.heading("Direction", text = "Direction", anchor = CENTER)
        root.cpuFrame.cpu0Treeview.heading("Value", text = "Value", anchor = CENTER)

        root.cpuFrame.cpu0Treeview.insert(parent = "", index = "end", iid = 0, text = "", values = values0[0])
        root.cpuFrame.cpu0Treeview.insert(parent = "", index = "end", iid = 1, text = "", values = values0[1])
        root.cpuFrame.cpu0Treeview.insert(parent = "", index = "end", iid = 2, text = "", values = values0[2])
        root.cpuFrame.cpu0Treeview.insert(parent = "", index = "end", iid = 3, text = "", values = values0[3])

        root.cpuFrame.cpu0Treeview.pack(padx = 10, pady = 0, side = LEFT)

        controller1 = root.cpu1.getController()
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

        # treeview cpu1
        root.cpuFrame.cpu1Treeview = ttk.Treeview(root.cpuFrame, columns = cpuColumns, show = "headings", height = 4, selectmode = "none")

        root.cpuFrame.cpu1Treeview.column("#0", width = 0, stretch = NO)
        root.cpuFrame.cpu1Treeview.column("Block", anchor = CENTER, width = 50, stretch = NO)
        root.cpuFrame.cpu1Treeview.column("State", anchor = CENTER, width = 50, stretch = NO)
        root.cpuFrame.cpu1Treeview.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        root.cpuFrame.cpu1Treeview.column("Value", anchor = CENTER, width = 130, stretch = NO)

        root.cpuFrame.cpu1Treeview.heading("#0", text = "", anchor = CENTER)
        root.cpuFrame.cpu1Treeview.heading("Block", text = "Block", anchor = CENTER)
        root.cpuFrame.cpu1Treeview.heading("State", text = "State", anchor = CENTER)
        root.cpuFrame.cpu1Treeview.heading("Direction", text = "Direction", anchor = CENTER)
        root.cpuFrame.cpu1Treeview.heading("Value", text = "Value", anchor = CENTER)

        root.cpuFrame.cpu1Treeview.insert(parent = "", index = "end", iid = 0, text = "", values = values1[0])
        root.cpuFrame.cpu1Treeview.insert(parent = "", index = "end", iid = 1, text = "", values = values1[1])
        root.cpuFrame.cpu1Treeview.insert(parent = "", index = "end", iid = 2, text = "", values = values1[2])
        root.cpuFrame.cpu1Treeview.insert(parent = "", index = "end", iid = 3, text = "", values = values1[3])

        root.cpuFrame.cpu1Treeview.pack(padx = 10, pady = 0, side = LEFT)

        controller2 = root.cpu2.getController()
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

        # treeview cpu2
        root.cpuFrame.cpu2Treeview = ttk.Treeview(root.cpuFrame, columns = cpuColumns, show = "headings", height = 4, selectmode = "none")

        root.cpuFrame.cpu2Treeview.column("#0", width = 0, stretch = NO)
        root.cpuFrame.cpu2Treeview.column("Block", anchor = CENTER, width = 50, stretch = NO)
        root.cpuFrame.cpu2Treeview.column("State", anchor = CENTER, width = 50, stretch = NO)
        root.cpuFrame.cpu2Treeview.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        root.cpuFrame.cpu2Treeview.column("Value", anchor = CENTER, width = 130, stretch = NO)

        root.cpuFrame.cpu2Treeview.heading("#0", text = "", anchor = CENTER)
        root.cpuFrame.cpu2Treeview.heading("Block", text = "Block", anchor = CENTER)
        root.cpuFrame.cpu2Treeview.heading("State", text = "State", anchor = CENTER)
        root.cpuFrame.cpu2Treeview.heading("Direction", text = "Direction", anchor = CENTER)
        root.cpuFrame.cpu2Treeview.heading("Value", text = "Value", anchor = CENTER)

        root.cpuFrame.cpu2Treeview.insert(parent = "", index = "end", iid = 0, text = "", values = values2[0])
        root.cpuFrame.cpu2Treeview.insert(parent = "", index = "end", iid = 1, text = "", values = values2[1])
        root.cpuFrame.cpu2Treeview.insert(parent = "", index = "end", iid = 2, text = "", values = values2[2])
        root.cpuFrame.cpu2Treeview.insert(parent = "", index = "end", iid = 3, text = "", values = values2[3])

        root.cpuFrame.cpu2Treeview.pack(padx = 10, pady = 0, side = LEFT)

        controller3 = root.cpu3.getController()
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

        # treeview cpu3
        root.cpuFrame.cpu3Treeview = ttk.Treeview(root.cpuFrame, columns = cpuColumns, show = "headings", height = 4, selectmode = "none")

        root.cpuFrame.cpu3Treeview.column("#0", width = 0, stretch = NO)
        root.cpuFrame.cpu3Treeview.column("Block", anchor = CENTER, width = 50, stretch = NO)
        root.cpuFrame.cpu3Treeview.column("State", anchor = CENTER, width = 50, stretch = NO)
        root.cpuFrame.cpu3Treeview.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        root.cpuFrame.cpu3Treeview.column("Value", anchor = CENTER, width = 130, stretch = NO)

        root.cpuFrame.cpu3Treeview.heading("#0", text = "", anchor = CENTER)
        root.cpuFrame.cpu3Treeview.heading("Block", text = "Block", anchor = CENTER)
        root.cpuFrame.cpu3Treeview.heading("State", text = "State", anchor = CENTER)
        root.cpuFrame.cpu3Treeview.heading("Direction", text = "Direction", anchor = CENTER)
        root.cpuFrame.cpu3Treeview.heading("Value", text = "Value", anchor = CENTER)

        root.cpuFrame.cpu3Treeview.insert(parent = "", index = "end", iid = 0, text = "", values = values3[0])
        root.cpuFrame.cpu3Treeview.insert(parent = "", index = "end", iid = 1, text = "", values = values3[1])
        root.cpuFrame.cpu3Treeview.insert(parent = "", index = "end", iid = 2, text = "", values = values3[2])
        root.cpuFrame.cpu3Treeview.insert(parent = "", index = "end", iid = 3, text = "", values = values3[3])

        root.cpuFrame.cpu3Treeview.pack(padx = 10, pady = 0, side = LEFT)

        # bus frame
        busFrame = Frame(root)
        busFrame.place(anchor = "center", relx = 0.5, rely = 0.43)

        busColumns = ("Bus")

        # treeview main memory
        busFrame.busTreeview = ttk.Treeview(busFrame, columns = busColumns, show = "headings", height = 2, selectmode = "none")

        busFrame.busTreeview.column("#0", width = 0, stretch = NO)
        busFrame.busTreeview.column("Bus", anchor = CENTER, width = 1312, stretch = NO)

        busFrame.busTreeview.heading("#0", text = "", anchor = CENTER)
        busFrame.busTreeview.heading("Bus", text = "", anchor = CENTER)

        busFrame.busTreeview.insert(parent = "", index = "end", iid = 0, text = "", values = ("Bus"))

        busFrame.busTreeview.pack(padx = 0, pady = 0, side = BOTTOM)

        # main memory frame
        root.mainMemoryFrame = Frame(root)
        root.mainMemoryFrame.place(anchor = "center", relx = 0.5, rely = 0.65)

        mainMemoryColumns = ("Direction", "Value")

        dictionary = root.mainMemory.getDictionary()

        keys = dictionary.keys()

        keyArray = []

        for key in keys:

            keyArray.append(key)

        # treeview main memory
        root.mainMemoryFrame.mainMemoryTreeview = ttk.Treeview(root.mainMemoryFrame, columns = mainMemoryColumns, show = "headings", height = 8, selectmode = "none")

        root.mainMemoryFrame.mainMemoryTreeview.column("#0", width = 0, stretch = NO)
        root.mainMemoryFrame.mainMemoryTreeview.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        root.mainMemoryFrame.mainMemoryTreeview.column("Value", anchor = CENTER, width = 130, stretch = NO)

        root.mainMemoryFrame.mainMemoryTreeview.heading("#0", text = "", anchor = CENTER)
        root.mainMemoryFrame.mainMemoryTreeview.heading("Direction", text = "Direction", anchor = CENTER)
        root.mainMemoryFrame.mainMemoryTreeview.heading("Value", text = "Value", anchor = CENTER)

        root.mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 0, text = "", values = ("0b" + "{0:04b}".format(keyArray[0]), "0x" + "{0:016x}".format(dictionary[keyArray[0]])))
        root.mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 1, text = "", values = ("0b" + "{0:04b}".format(keyArray[1]), "0x" + "{0:016x}".format(dictionary[keyArray[1]])))
        root.mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 2, text = "", values = ("0b" + "{0:04b}".format(keyArray[2]), "0x" + "{0:016x}".format(dictionary[keyArray[2]])))
        root.mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 3, text = "", values = ("0b" + "{0:04b}".format(keyArray[3]), "0x" + "{0:016x}".format(dictionary[keyArray[3]])))
        root.mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 4, text = "", values = ("0b" + "{0:04b}".format(keyArray[4]), "0x" + "{0:016x}".format(dictionary[keyArray[4]])))
        root.mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 5, text = "", values = ("0b" + "{0:04b}".format(keyArray[5]), "0x" + "{0:016x}".format(dictionary[keyArray[5]])))
        root.mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 6, text = "", values = ("0b" + "{0:04b}".format(keyArray[6]), "0x" + "{0:016x}".format(dictionary[keyArray[6]])))
        root.mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 7, text = "", values = ("0b" + "{0:04b}".format(keyArray[7]), "0x" + "{0:016x}".format(dictionary[keyArray[7]])))

        root.mainMemoryFrame.mainMemoryTreeview.pack(side = BOTTOM)

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
        lastInstructionTittleFrame.lastInstructionTittle.heading("Tittle", text = "Last instructions", anchor = W)

        lastInstructionTittleFrame.lastInstructionTittle.pack(padx = 10, pady = 0, side = LEFT)

        # last instruction frame
        root.lastInstructionFrame = Frame(root)
        root.lastInstructionFrame.place(anchor = "center", relx = 0.168, rely = 0.636)

        instructionColumns = ("CPU", "Instruction", "Read Miss", "Write Miss")

        # treeview instruction
        root.lastInstructionFrame.instructionTreeview = ttk.Treeview(root.lastInstructionFrame, columns = instructionColumns, show = "headings", height = 4, selectmode = "none")

        root.lastInstructionFrame.instructionTreeview.column("#0", width = 0, stretch = NO)
        root.lastInstructionFrame.instructionTreeview.column("CPU", anchor = CENTER, width = 40, stretch = NO)
        root.lastInstructionFrame.instructionTreeview.column("Instruction", anchor = CENTER, width = 220, stretch = NO)
        root.lastInstructionFrame.instructionTreeview.column("Read Miss", anchor = CENTER, width = 80, stretch = NO)
        root.lastInstructionFrame.instructionTreeview.column("Write Miss", anchor = CENTER, width = 80, stretch = NO)

        root.lastInstructionFrame.instructionTreeview.heading("#0", text = "", anchor = CENTER)
        root.lastInstructionFrame.instructionTreeview.heading("CPU", text = "CPU", anchor = CENTER)
        root.lastInstructionFrame.instructionTreeview.heading("Instruction", text = "Instruction", anchor = CENTER)
        root.lastInstructionFrame.instructionTreeview.heading("Read Miss", text = "Read Miss", anchor = CENTER)
        root.lastInstructionFrame.instructionTreeview.heading("Write Miss", text = "Write Miss", anchor = CENTER)

        root.lastInstructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 0, text = "", values = ("N0", None, "0", "0"))
        root.lastInstructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 1, text = "", values = ("N1", None, "0", "0"))
        root.lastInstructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 2, text = "", values = ("N2", None, "0", "0"))
        root.lastInstructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 3, text = "", values = ("N3", None, "0", "0"))

        root.lastInstructionFrame.instructionTreeview.pack(side = LEFT)

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
        currentInstructionTittleFrame.currentInstructionTittle.heading("Tittle", text = "Current instructions", anchor = W)

        currentInstructionTittleFrame.currentInstructionTittle.pack(padx = 10, pady = 0, side = LEFT)

        # current instruction frame
        root.currentInstructionFrame = Frame(root)
        root.currentInstructionFrame.place(anchor = "center", relx = 0.168, rely = 0.87)

        # treeview instruction
        root.currentInstructionFrame.instructionTreeview = ttk.Treeview(root.currentInstructionFrame, columns = instructionColumns, show = "headings", height = 4, selectmode = "none")

        root.currentInstructionFrame.instructionTreeview.column("#0", width = 0, stretch = NO)
        root.currentInstructionFrame.instructionTreeview.column("CPU", anchor = CENTER, width = 40, stretch = NO)
        root.currentInstructionFrame.instructionTreeview.column("Instruction", anchor = CENTER, width = 220, stretch = NO)
        root.currentInstructionFrame.instructionTreeview.column("Read Miss", anchor = CENTER, width = 80, stretch = NO)
        root.currentInstructionFrame.instructionTreeview.column("Write Miss", anchor = CENTER, width = 80, stretch = NO)

        root.currentInstructionFrame.instructionTreeview.heading("#0", text = "", anchor = CENTER)
        root.currentInstructionFrame.instructionTreeview.heading("CPU", text = "CPU", anchor = CENTER)
        root.currentInstructionFrame.instructionTreeview.heading("Instruction", text = "Instruction", anchor = CENTER)
        root.currentInstructionFrame.instructionTreeview.heading("Read Miss", text = "Read Miss", anchor = CENTER)
        root.currentInstructionFrame.instructionTreeview.heading("Write Miss", text = "Write Miss", anchor = CENTER)

        root.currentInstructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 0, text = "", values = ("N0", None, "0", "0"))
        root.currentInstructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 1, text = "", values = ("N1", None, "0", "0"))
        root.currentInstructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 2, text = "", values = ("N2", None, "0", "0"))
        root.currentInstructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 3, text = "", values = ("N3", None, "0", "0"))

        root.currentInstructionFrame.instructionTreeview.pack(side = LEFT)

        # button frame
        buttonFrame = Frame(root)
        buttonFrame.place(anchor = "center", relx = 0.7985, rely = 0.539)

        # step by step button
        buttonFrame.stepByStepButton = Button(buttonFrame, text = "Step by Step", activebackground = "#FF8000", fg = "white", bg = "#4285f4", font = ("Italic", 13), width = 10, heigh = 1, command = root.stepByStep)
        buttonFrame.stepByStepButton.pack(padx = 10, pady = 0, side = LEFT)

        # continuos execution button
        buttonFrame.continuosExecutionButton = Button(buttonFrame, text = "Continuos Execution", activebackground = "#FF8000", fg = "white", bg = "#4285f4", font = ("Italic", 13), width = 20, heigh = 1, command = root.continuosExecution)
        buttonFrame.continuosExecutionButton.pack(padx = 10, pady = 0, side = LEFT)

        # pause button
        buttonFrame.pauseButton = Button(buttonFrame, text = "Pause", activebackground = "#FF8000", fg = "white", bg = "#4285f4", font = ("Italic", 13), width = 10, heigh = 1, command = root.pause)
        buttonFrame.pauseButton.pack(padx = 10, pady = 0, side = LEFT)

        # insert instruction tittle frame
        insertInstructionTittleFrame = Frame(root)
        insertInstructionTittleFrame.place(anchor = "center", relx = 0.795, rely = 0.625)

        # CPU label
        insertInstructionTittleFrame.cpuLabel = Label(insertInstructionTittleFrame, text = "CPU\n(number)", fg =  "#4285f4", font = ("Italic", 14))
        insertInstructionTittleFrame.cpuLabel.pack(padx = 10, pady = 0, side = LEFT)
        
        # operation label
        insertInstructionTittleFrame.operationLabel = Label(insertInstructionTittleFrame, text = " Operation\n (capital)", fg =  "#4285f4", font = ("Italic", 14))
        insertInstructionTittleFrame.operationLabel.pack(padx = 10, pady = 0, side = LEFT)

        # direction label
        insertInstructionTittleFrame.directionLabel = Label(insertInstructionTittleFrame, text = "  Direction\n  (bin)", fg =  "#4285f4", font = ("Italic", 14))
        insertInstructionTittleFrame.directionLabel.pack(padx = 10, pady = 0, side = LEFT)

        # value label
        insertInstructionTittleFrame.valueLabel = Label(insertInstructionTittleFrame, text = "     Value\n     (hex)", fg =  "#4285f4", font = ("Italic", 14))
        insertInstructionTittleFrame.valueLabel.pack(padx = 10, pady = 0, side = LEFT)

        # insert instruction frame
        root.insertInstructionFrame = Frame(root)
        root.insertInstructionFrame.place(anchor = "center", relx = 0.79999, rely = 0.685)

        # CPU textBox
        root.insertInstructionFrame.CpuTextBox = Entry(root.insertInstructionFrame, width = 10, font = ("Italic", 13))
        root.insertInstructionFrame.CpuTextBox.pack(padx = 10, pady = 0, side = LEFT)

        # operation textBox
        root.insertInstructionFrame.operationTextBox = Entry(root.insertInstructionFrame, width = 10, font = ("Italic", 13))
        root.insertInstructionFrame.operationTextBox.pack(padx = 10, pady = 0, side = LEFT)

        # direction textBox
        root.insertInstructionFrame.directionTextBox = Entry(root.insertInstructionFrame, width = 10, font = ("Italic", 13))
        root.insertInstructionFrame.directionTextBox.pack(padx = 10, pady = 0, side = LEFT)

        # value textBox
        root.insertInstructionFrame.valueTextBox = Entry(root.insertInstructionFrame, width = 10, font = ("Italic", 13))
        root.insertInstructionFrame.valueTextBox.pack(padx = 10, pady = 0, side = LEFT)

        # load frame
        loadFrame = Frame(root)
        loadFrame.place(anchor = "center", relx = 0.7985, rely = 0.762)

        # load button
        loadFrame.loadButton = Button(loadFrame, text = "Load", activebackground = "#FF8000", fg = "white", bg = "#4285f4", font = ("Italic", 13), width = 20, heigh = 1, command = root.load)
        loadFrame.loadButton.pack(padx = 0, pady = 0, side = LEFT)

    def updateCpuInformation(root):

        cpuIndex = 0

        blockIndex = 0

        for cpu in root.cpuArray:

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
                if(blockIndex == 0):

                    # cpu0
                    if(cpuIndex == 0):

                        root.cpuFrame.cpu0Treeview.item(blockIndex, text = "", values = blockValues)

                    # cpu1
                    elif(cpuIndex == 1):

                        root.cpuFrame.cpu1Treeview.item(blockIndex, text = "", values = blockValues)

                    # cpu2
                    elif(cpuIndex == 2):

                        root.cpuFrame.cpu2Treeview.item(blockIndex, text = "", values = blockValues)

                    # cpu3
                    else:

                        root.cpuFrame.cpu3Treeview.item(blockIndex, text = "", values = blockValues)

                # block1
                elif(blockIndex == 1):

                    # cpu0
                    if(cpuIndex == 0):

                        root.cpuFrame.cpu0Treeview.item(blockIndex, text = "", values = blockValues)

                    # cpu1
                    elif(cpuIndex == 1):

                        root.cpuFrame.cpu1Treeview.item(blockIndex, text = "", values = blockValues)

                    # cpu2
                    elif(cpuIndex == 2):

                        root.cpuFrame.cpu2Treeview.item(blockIndex, text = "", values = blockValues)

                    # cpu3
                    else:

                        root.cpuFrame.cpu3Treeview.item(blockIndex, text = "", values = blockValues)

                # block2
                elif(blockIndex == 3):

                    # cpu0
                    if(cpuIndex == 0):

                        root.cpuFrame.cpu0Treeview.item(blockIndex, text = "", values = blockValues)

                    # cpu1
                    elif(cpuIndex == 1):

                        root.cpuFrame.cpu1Treeview.item(blockIndex, text = "", values = blockValues)

                    # cpu2
                    elif(cpuIndex == 2):

                        root.cpuFrame.cpu2Treeview.item(blockIndex, text = "", values = blockValues)

                    # cpu3
                    else:

                        root.cpuFrame.cpu3Treeview.item(blockIndex, text = "", values = blockValues)

                # block3
                else:

                    # cpu0
                    if(cpuIndex == 0):

                        root.cpuFrame.cpu0Treeview.item(blockIndex, text = "", values = blockValues)

                    # cpu1
                    elif(cpuIndex == 1):

                        root.cpuFrame.cpu1Treeview.item(blockIndex, text = "", values = blockValues)

                    # cpu2
                    elif(cpuIndex == 2):

                        root.cpuFrame.cpu2Treeview.item(blockIndex, text = "", values = blockValues)

                    # cpu3
                    else:

                        root.cpuFrame.cpu3Treeview.item(blockIndex, text = "", values = blockValues)

                blockIndex += 1

            blockIndex = 0

            cpuIndex += 1

    def updateMainMemoryInformation(root):
        
        dictionary = root.mainMemory.getDictionary()

        keys = dictionary.keys()

        keyArray = []

        for key in keys:

            keyArray.append(key)

        index = 0

        for key in keyArray:

            mainMemoryValues = ("0b" + "{0:04b}".format(key), "0x" + "{0:016x}".format(dictionary[key]))

            root.mainMemoryFrame.mainMemoryTreeview.item(index, text = "", values = mainMemoryValues)

            index += 1

    def updateLastInstruction(root):

        for index in range(0, 4):

            current = root.currentInstructionFrame.instructionTreeview.item(index)

            currentValues = tuple(current["values"])

            root.lastInstructionFrame.instructionTreeview.item(index, text = "", values = currentValues)

    def updateCurrentInstruction(root):

        index = 0

        for cpu in root.cpuArray:

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

                root.currentInstructionFrame.instructionTreeview.item(index, text = "", values = instructionValues)

                index += 1

    def threadFunction(root, cpu):

        if(cpu.getCurrentInstruction() is not None):

            root.updateLastInstruction()

        # not loaded instruction
        if(cpu.getLoaded() == 0):
    
            cpu.generateInstruction()          

            sleep(TIMER)

        # loaded instruction
        else:

            cpu.setLoaded(0)

        cpu.executeInstruction(root.bus)        

        root.updateCurrentInstruction()

        sleep(TIMER)       

        root.updateCpuInformation()

        root.updateMainMemoryInformation()

    def stepByStep(root):
        
        thread0 = Thread(target = root.threadFunction, args = (root.cpu0,))
        thread1 = Thread(target = root.threadFunction, args = (root.cpu1,))
        thread2 = Thread(target = root.threadFunction, args = (root.cpu2,))
        thread3 = Thread(target = root.threadFunction, args = (root.cpu3,))

        # start threads
        thread0.start()
        thread1.start()
        thread2.start()
        thread3.start()

    def continuosExecutionThread(root):

        root.pauseFlag = 0

        while(root.pauseFlag == 0):

            # create threads
            thread0 = Thread(target = root.threadFunction, args = (root.cpu0,))
            thread1 = Thread(target = root.threadFunction, args = (root.cpu1,))
            thread2 = Thread(target = root.threadFunction, args = (root.cpu2,))
            thread3 = Thread(target = root.threadFunction, args = (root.cpu3,))

            # start threads
            thread0.start()
            thread1.start()
            thread2.start()
            thread3.start()

            sleep(TIMER * 2)

        print("Paused")

    def continuosExecution(root):

        # create thread
        continuosExecutionThread = Thread(target = root.continuosExecutionThread)

        # start thread
        continuosExecutionThread.start()

    def pause(root):
        
        root.pauseFlag = 1

    def load(root):

        if(root.pauseFlag == 1):
        
            # get data
            cpuNumber = root.insertInstructionFrame.CpuTextBox.get()
            operation = root.insertInstructionFrame.operationTextBox.get()
            memoryDirection = root.insertInstructionFrame.directionTextBox.get()
            value = root.insertInstructionFrame.valueTextBox.get()

            if(cpuNumber != "" and operation != ""):

                cpuNumber = int(cpuNumber)

                cpu = root.cpuArray[cpuNumber]

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
                root.insertInstructionFrame.CpuTextBox.delete(0, END)
                root.insertInstructionFrame.operationTextBox.delete(0, END)
                root.insertInstructionFrame.directionTextBox.delete(0, END)
                root.insertInstructionFrame.valueTextBox.delete(0, END)

# window loop
Window().mainloop()

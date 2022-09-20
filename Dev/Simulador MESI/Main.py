from SharedBus import MemoryBus
from Memory import Memory
from Processor import Processor
from L1_Cache_Module import L1_Block
import time
from GUI import Design
from tkinter import *

if __name__ == "__main__":
	root = Tk()
	ui = Design(root)
	root.mainloop()

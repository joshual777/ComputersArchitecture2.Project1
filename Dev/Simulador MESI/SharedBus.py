"""
								MAIN MEMORY MODEL

                            SHARED BUS MAIN MEMORY MODEL 

        -It is connected to the main memory and it is connected to the CPUs
        -It is one to the whole system
"""

import threading
import time
from Memory import Memory

#Class to model the shared bus that is in de main memory model
class MemoryBus:

	def  __init__(self, memory):
		self.lock = threading.Lock()  #Activate the thread to manage the automatic process
		self.memory = memory
		self.processors = []
	
    #Function to manage the thread in the main process
	def sharedAddressP(self, address, cpu):
		cpus = []
		
        #Search the process 
		for processor in self.processors:
			if processor.id != cpu and processor.control.getCorresBlock(address):
				cpus.append(processor)
		return cpus

    #Block the process if there is a mistake in the read/write process			
	def lockMe(self):
		self.lock.acquire()
	
    #Release the process if the block flag was solved
	def unlockMe(self):
		self.lock.release()
	
    #Read the memory in the main memory according to its dress
	def readMemory(self, address):
		data = self.memory.read(address)
		return data
	
    #Write the memory in the main memory according to its dress
	def writeMemory(self, address, data):
		self.memory.write(address, data)

    #MESI PROTOCOL IMPLEMENTATION5	
	def changeStates(self, address, processorsShared, change):
		for processor in processorsShared:
            #Get the read/write information
			block = processor.control.cache.getL1BlockByAddress(address)
			match change:
                #Shared FLAG
				case 0:
					block.setBitState("S") 
                #Invalid FLAG
				case 1:
					block.setBitState("I") 






"""
								MAIN MEMORY MODEL

                         SHARED 8 SPACES MAIN MEMORY MODEL

        -It has eight different spaces: 000, 001, 010, 011, 100, 101, 110, 111
        -It is connected to the CPUs by a main bus 
        -It must display the states content
        -It will manage by a frequency,  using the time library 
"""

import time

#Class to model the main memory and the write and read functions link to each of them
class Memory: 

    #It will create a list with eight spaces to each memory cell
	def  __init__(self):
		self.positions = []
		for i in range(8):
			self.positions += [0]   

    #The write function to the cell memory
	def write(self, address, data):
		time.sleep(1)
		self.positions[address] = data
		
    #The read function to the cell memory
	def read(self, address):
		time.sleep(1)
		return self.positions[address]

    #Print the conent in the memory 
	def printMem(self):
		for i in range(8):
			print(str(i) + "=" +str(self.positions[i]))
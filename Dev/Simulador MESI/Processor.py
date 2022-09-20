""" 
                                PROCESSOR SYSTEM MODEL

            It will create an instance of each processor to operate in a parallel way, each
            processor will have an specific instruction generated randomly, this for each one.
            There will be three kind of instructions, read, write and calc (which consumes time).
"""
import threading
import InstructionGeneration
import time

#This class models the processor and the modules it has 
class Processor:

    #Set the instructions parameters to the each processor
	def  __init__(self, id, bus):

		self.id = id                                #Processor ID
		self.running  = False                       #Check if the selectes processor is running
		self.instRunning  = "---"                   #Check the specific instruction
		self.lastInst  = ""                         #Chech the last executed instruction
		self.control  = Controller(self.id, bus)    #Set the control 
		
	#Funtion to execute the selected instruction 
	def exc(self):
        #This will activate the clock associate to the processor
		while self.running:
			self.thread_clock()
	
    #Function to stop the clock associate to the processor
	def exc_step(self):
		self.thread_clock()
	
    #Fuction to manage the clock according to the selected instruction
	def thread_clock(self):
		self.lastInst = self.instRunning
		inst = InstructionGeneration.genInstruction()
		print(str(self.id) + "=" + inst)
		initial = inst[0]
        #Read instruction
		if initial == "R":
			self.control.read(int(inst[5:8], 2))
        #Write instruction
		elif initial == "W":
			self.control.write(int(inst[6:9], 2), int(inst[10:],16))
        #Calc instruction
		elif initial == "C":
			print("CALC")
		else:
			print("ERROR: Generated Instruction")

	#Activate the thread	
	def runThread(self, isStep):
		if self.running:
			print(str(self.id) + " Executing \n")
		else: 
			if isStep:
				hilo = threading.Thread(target=self.exc_step)
			else:
				self.running = True
				hilo = threading.Thread(target=self.exc)
			hilo.start()

    #Stop the thread		
	def stopThread(self):
		if self.running:
			self.running = False
		else: 
			print(str(self.id) + " STOP \n")	

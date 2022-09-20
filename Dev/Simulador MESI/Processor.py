""" 
                                PROCESSOR SYSTEM MODEL

            It will create an instance of each processor to operate in a parallel way, each
            processor will have an specific instruction generated randomly, this for each one.
            There will be three kind of instructions, read, write and calc (which consumes time).
"""
import threading
import time
import InstructionGeneration
from ControllerProtocol import Controller

#This class models the processor and the modules it has 
class Processor:

    #Set the instructions parameters to the each processor
	def  __init__(self, id, bus):

		self.id = id                                #Processor ID
		self.running  = False                       #Check if the selectes processor is running
		self.instRunning  = "---"                   #Check the specific instruction
		self.lastInst  = ""                         #Chech the last executed instruction
		self.control  = Controller(self.id, bus)    #Set the control 

    #Function to execute the frequency in the whole system	
	def exc(self):
		while self.running:
			self.thread_clock()
			time.sleep(3)
	
    #Execute the process step by step
	def exc_step(self):
		self.thread_clock()

    #Function to manage the tiem in the clock	
	def thread_clock(self):
		self.lastInst = self.instRunning
		inst = InstructionGeneration.genInstruction()
		self.instRunning = inst
		print(str(self.id) + "=" + inst)
		initial = inst[0]

        #Read process instance instruction
		if initial == "R":
			self.control.read(int(inst[5:8], 2))
        
        #Write process instance instruction
		elif initial == "W":
			self.control.write(int(inst[6:9], 2), int(inst[10:],16)) #Generate the hexadecimal code
        
        #Calc process instance instruction
		elif initial == "C":
			print("CALC")
		else:
			print("ERROR: Instruction Generated")


    #Execute the threads in each processor	
	def runThread(self, isStep):
		if self.running:
			print(str(self.id) + " Executing \n")
		else: 
			if isStep:
				hilo = threading.Thread(target=self.exc_step, daemon=True)
			else:
				self.running = True
				hilo = threading.Thread(target=self.exc, daemon=True)
			hilo.start()

    #Stop the thread in the processors		
	def stopThread(self):
		if self.running:
			self.running = False
		else: 
			print(str(self.id) + " Stopped \n")	

"""
								CACHE MEMORY MODEL AND SYSTEM COHERENCE

										CACHE MEMORY INFORMATION

		Following the project design specification, each block requires specific information
		they can store 4 memory blocks and de the information is:

			-->  Number of bock
			-->  Coherence state by the project: M = modified, S = shared, I= invalid, E = exclusive
			-->  Memory address
			-->  Hexadecimal 16 lenght data
"""
#CLASS TO MANAGE THE INFO ABOUT THE CACHE AND ITS PARAMETERS 
class L1_Info:

	#The atributes are initialized
	def  __init__(self, id):
		self.Number = id   		#Number of block
		self.bitState = "I"			#State of the block according to the MESI Protocol
		self.memoryAddress = 0		#Memory address in the process
		self.data = 0				#Hexadecimal data in the process


	#This function will get the number block and set the value of the block
	def getNumber(self):
				return self.id

	def setNumber(self, Number):
				self.id = id


	#This function will get the state block and set the state of the block according to the MESI protocol
	def getBitState(self):
				return self.bitState

	def setBitState(self, state):
				self.bitState = state


	##This function will get the address block and set the address of the block
	def getAddress(self):
				return self.memoryAddress

	def setAddress(self, address):
				self.memoryAddress = address


	#This function will get the hexadecimal data block and set the hexadecimal data of the block
	def getData(self):
				return self.data

	def setData(self, data):
				self.data = data


	#Monitory function just in case, this will help to the GUI
	def printBlock(self):
				print("ID " + str(self.id) + "  State " + str(self.bitState)+ "  Address " + str(self.memoryAddress) +"  Data " + str(self.data)  )
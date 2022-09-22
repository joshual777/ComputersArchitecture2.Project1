import time

from SharedBus import MemoryBus
from L1_Cache_Module import L1_Block

class Controller:

	def  __init__(self, processorId, bus):
		self.cache  = L1_Block()
		self.memoryBus  = bus
		self.processor  = processorId


	def printCache(self):
		print("\n P" + str(self.processor))
		self.cache.getBlock(0).printBlock()
		self.cache.getBlock(1).printBlock()
		self.cache.getBlock(2).printBlock()
		self.cache.getBlock(3).printBlock()

	def read(self,address):	

												hitBlock  = self.getCorresBlock(address)
												if hitBlock:
																print(str(self.processor) + " Read Hit \n")
												else:
																print(str(self.processor) + "= Read miss\n")
																
																self.memoryBus.lockMe()
																processorsShared = self.memoryBus.sharedAddressP(address, self.processor)
																if len(processorsShared) != 0:
																				p = processorsShared[0]
																				block = p.control.getCorresBlock(address)
																				if block.bitState == "M":
																								self.memoryBus.writeMemory(block.memoryAddress, block.data)
																				blockWrite = self.cache.write(address, block.getData(), "S")
																				self.memoryBus.changeStates(address, processorsShared, 0)
																				
																				
																else:
																				data = self.memoryBus.readMemory(address)
																				blockWrite  = self.cache.write(address, data, "E")
																				
																if blockWrite.bitState == "M" and blockWrite.memoryAddress != address:
																				self.memoryBus.writeMemory(blockWrite.memoryAddress, blockWrite.data)
																elif blockWrite.bitState == "S" and blockWrite.memoryAddress != address:
																				shared = self.memoryBus.sharedAddressP(blockWrite.memoryAddress, self.processor)
																				if len(shared) == 1:
																								shared[0].control.getCorresBlock(blockWrite.memoryAddress).setBitState("E")
																				
																				
																self.memoryBus.unlockMe()
																					
	def getCorresBlock(self, address):
												if address == 0 or address == 4:
																				block = self.cache.getBlock(0)
												elif address == 1 or address == 5:
																				block = self.cache.l1Blocks[1]
												elif address == 2 or address == 6:
																				block = self.cache.l1Blocks[2]
												elif address == 3 or address == 7:
																				block = self.cache.l1Blocks[3]
												else:
																print("Direccion incorrecta")
				
												if block.memoryAddress == address and block.getBitState() != "I":
																return block
												else:
																return False
			



								

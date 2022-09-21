"""
								CACHE MEMORY MODEL AND SYSTEM COHERENCE

                                        SYTEM MODEL AND COHERENCE

        -In the first instance the data is not allocated in the cache
        -Write and Read will generate "misses" in the cache
        -The initialization will be 0
        -One-way associativity correspondency implementation
"""
from Cache_Info_Parameters import L1_Info

class L1_Block:

    def __init__(self):
        self.L1_Blocks = [L1_Info("0"), L1_Info("1"), L1_Info("2"), L1_Info("3")] #Four block initialized

    #The function gets the number of cache block in the process
    def getBlockNumber(self, number):
        return self.L1_Blocks[number]  #Get the unique id

    #The function will get the address according to the execution process
    def getBlockAddress(self, address):
            resultB = L1_Info(0)
            for l1Block in self.L1_Blocks:
                if l1Block.memoryAddress == address:	
                    resultB = l1Block
            return resultB 


    #Write function into address memory allocations
    def Write_mem(self, address, data, bitSate):

        #One-way associativity correspondency implementation

        #Correspond attach to the first and fourth address in the main memory block
        if address == 0 or address == 4:
            block = L1_Info(0)
            block.setAddress(self.L1_Blocks[0].getAddress())
            block.setBitState(self.L1_Blocks[0].getBitState())
            block.setData(self.L1_Blocks[0].getData())
            self.L1_Blocks[0].setAddress(address)
            self.L1_Blocks[0].setBitState(bitSate)
            self.L1_Blocks[0].setData(data)
        
        #Correspond attach to the second and seventh address in the main memory block
        elif address == 1 or address == 5:
            block = L1_Info(1)
            block.setAddress(self.L1_Blocks[1].getAddress())
            block.setBitState(self.L1_Blocks[1].getBitState())
            block.setData(self.L1_Blocks[1].getData())
            self.L1_Blocks[1].setAddress(address)
            self.L1_Blocks[1].setBitState(bitSate)
            self.L1_Blocks[1].setData(data)

        #Correspond attach to the fourth and fifth address in the main memory block
        elif address == 2 or address == 6:
            block = L1_Info(2)
            block.setAddress(self.L1_Blocks[2].getAddress())
            block.setBitState(self.L1_Blocks[2].getBitState())
            block.setData(self.L1_Blocks[2].getData())
            self.L1_Blocks[2].setAddress(address)
            self.L1_Blocks[2].setBitState(bitSate)
            self.L1_Blocks[2].setData(data)

        #Correspond attach to the second and eighth address in the main memory block
        elif address == 3 or address == 7:
            block = L1_Info(3)
            block.setAddress(self.L1_Blocks[3].getAddress())
            block.setBitState(self.L1_Blocks[3].getBitState())
            block.setData(self.L1_Blocks[3].getData())
            self.L1_Blocks[3].setAddress(address)
            self.L1_Blocks[3].setBitState(bitSate)
            self.L1_Blocks[3].setData(data)      

        #Invalid direction
        else:
            block = L1_Info(0)
            print("Invalid Address")

        return block  

    def getBlock(self, id):
	    return self.L1_Blocks[id]
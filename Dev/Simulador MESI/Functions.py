from math import *
from random import *
from regulars import *
from threading import *
from time import *

"""
								MAIN MEMORY MODEL

                         SHARED 8 SPACES MAIN MEMORY MODEL

        -It has eight different spaces: 000, 001, 010, 011, 100, 101, 110, 111
        -It is connected to the CPUs by a main bus 
        -It must display the states content
        -It will manage by a frequency,  using the time library 
"""
class MainMemory:
    
    def __init__(self):        
        self.dictionary = {}

        self.startMemory()

    def getDictionary(self):
        return self.dictionary

    def setDictionary(self, dictionary):
        self.dictionary = dictionary

    """
    This function creates the main memory dictionary
    """
    def startMemory(self):        
        
        for i in MEMORY_BLOCKS_DIR:

            self.dictionary[i] = INITIAL_MAIN_MEMORY_VALUE


"""
								MAIN MEMORY MODEL

                            SHARED BUS MAIN MEMORY MODEL 

        -It is connected to the main memory and it is connected to the CPUs
        -It is one to the whole system
"""
class Bus:
    
    def __init__(self, cpuArray, mainMemory):
        self.cpuArray = cpuArray
        self.mainMemory = mainMemory
        self.lock = Lock()
    
    def getCpuArray(self):
        return self.cpuArray

    def setCpuArray(self, cpuArray):
        self.cpuArray = cpuArray

    def getMainMemory(self):
        return self.mainMemory

    def setMainMemory(self, mainMemory):
        self.mainMemory = mainMemory

    def getLock(self):
        return self.lock

    def setLock(self, lock):
        self.lock = lock

    def acquireLock(self):
        self.lock.acquire()

    def releaseLock(self):
        self.lock.release()


"""
                        INSTRUCTION  GENERATION FUNCTION

        The main purpose is to generate the instruction by no using a random library 
        this will use Binomial function in order to achieve that
"""
class Instruction:
    
    def __init__(self, cpuNumber, operation):
        self.cpuNumber = cpuNumber
        self.operation = operation
        self.memoryDirection = None
        self.value = None

    def getCpuNumber(self):
        return self.cpuNumber

    def setCpuNumber(self, cpuNumber):
        self.cpuNumber = cpuNumber

    def getOperation(self):
        return self.operation

    def setOperation(self, operation):
        self.operation = operation

    def getMemoryDirection(self):
        return self.memoryDirection

    def setMemoryDirection(self, memoryDirection):
        self.memoryDirection = memoryDirection

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

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
class Cache:
    
    def __init__(self):
        self.blocks = []

    def getBlocks(self):
        return self.blocks

    def setBlocks(self, blocks):
        self.blocks = blocks

"""
								CACHE MEMORY MODEL AND SYSTEM COHERENCE

                                        SYTEM MODEL AND COHERENCE

        -In the first instance the data is not allocated in the cache
        -Write and Read will generate "misses" in the cache
        -The initialization will be 0
        -One-way associativity correspondency implementation
"""
class CacheBlock:
    
    def __init__(self, number, state, memoryDirection, value):
        self.number = number
        self.state = state
        self.memoryDirection = memoryDirection
        self.value = value

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def getMemoryDirection(self):
        return self.memoryDirection

    def setMemoryDirection(self, memoryDirection):
        self.memoryDirection = memoryDirection

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value



class Controller:
    
    def __init__(self):
        self.cache = None
        self.readMiss = 0
        self.writeMiss = 0
    
    def getCache(self):
        return self.cache

    def setCache(self, cache):
        self.cache = cache

    def getReadMiss(self):
        return self.readMiss

    def setReadMiss(self, readMiss):
        self.readMiss = readMiss

    def getWriteMiss(self):
        return self.writeMiss

    def setWriteMiss(self, writeMiss):
        self.writeMiss = writeMiss

    def resetAlerts(self):
        self.readMiss = 0
        self.writeMiss = 0


    def invalidateCaches(self, instruction, bus):

        memoryDirection = instruction.getMemoryDirection()
        cpuArray = bus.getCpuArray()
        localCpu = cpuArray[instruction.getCpuNumber()]

        for cpu in cpuArray:

            # ignore local CPU cache
            if(cpu.getNumber() != localCpu.getNumber()):
                remoteController = cpu.getController()
                remoteCache = remoteController.getCache()
                remoteBlocks = remoteCache.getBlocks()

                for remoteBlock in remoteBlocks:
                    # memory direction match
                    if(remoteBlock.getMemoryDirection() == memoryDirection):
                        remoteBlock.setState(INVALID)


    def localRead(self, instruction):

        memoryDirection = instruction.getMemoryDirection()
        blocks = self.cache.blocks

        for block in blocks:

            # memory direction match
            if(block.getMemoryDirection() == memoryDirection):
                state = block.getState()

                # state M, E or S form protocol MESI
                if(state == MODIFIED or state == EXCLUSIVE or state == SHARED):
                    return HIT

                else:

                    self.readMiss = 1
                    return MISS
   
        self.readMiss = 1
        return MISS


    def localWrite(self, instruction, bus):

        memoryDirection = instruction.getMemoryDirection()
        value = instruction.getValue()
        blocks = self.cache.blocks
        for block in blocks:

            if(block.getMemoryDirection() == memoryDirection):
                block.setValue(value)
                block.setState(MODIFIED)
                self.invalidateCaches(instruction, bus)
                return HIT

        self.writeMiss = 1
        return MISS

    def localSearch(self, instruction, bus):

        # read operation
        if(instruction.getOperation() == OPERATIONS[READ_INDEX]):
            result = self.localRead(instruction)

        # write operation
        elif(instruction.getOperation() == OPERATIONS[WRITE_INDEX]):
            result = self.localWrite(instruction, bus)

        # calc instruction
        else:
            result = HIT

        return result

    def remoteRead(self, instruction, bus):
    
        bus.acquireLock()
        located = 0
        memoryDirection = instruction.getMemoryDirection()
        cpuArray = bus.getCpuArray()
        localCpu = cpuArray[instruction.getCpuNumber()]
        localController = localCpu.getController()
        localCache = localController.getCache()
        localBlocks = localCache.getBlocks()        

        for cpu in cpuArray:

            if(cpu.getNumber() != localCpu.getNumber()):
                remoteController = cpu.getController()
                remoteCache = remoteController.getCache()
                remoteBlocks = remoteCache.getBlocks()
                for remoteBlock in remoteBlocks:    

   
                    if(remoteBlock.getMemoryDirection() == memoryDirection):
                        state = remoteBlock.getState()
                        if(state != INVALID):
                            located = 1
                            localBlock = localBlocks[0]

                            for block in localBlocks:

                                if(block.getMemoryDirection() == memoryDirection):
                                    localBlock = block
                            value = remoteBlock.getValue()

                            # state M
                            if(state == MODIFIED):
                                sleep(TIMER * 2)
                                mainMemory = bus.getMainMemory()
                                dictionary = mainMemory.getDictionary()
                                dictionary[memoryDirection] = value

                            remoteBlock.setState(SHARED)                         
                            localBlock.setState(SHARED)
                            localBlock.setMemoryDirection(memoryDirection)
                            localBlock.setValue(value)

        # search in main memory
        if(located == 0):
            sleep(TIMER * 2)
            mainMemory = bus.getMainMemory()
            dictionary = mainMemory.getDictionary()           
            value = dictionary.get(memoryDirection)
            scache = memoryDirection % SETS
            localBlock = localBlocks[scache]
            localBlock.setMemoryDirection(memoryDirection)
            localBlock.setValue(value)
            localBlock.setState(EXCLUSIVE)

        bus.releaseLock()

    def remoteWrite(self, instruction, bus):
        
        # acquire lock
        bus.acquireLock()
        memoryDirection = instruction.getMemoryDirection()
        value = instruction.getValue()
        sleep(TIMER * 2)
        mainMemory = bus.getMainMemory()
        dictionary = mainMemory.getDictionary()
        dictionary[memoryDirection] = value
        scache = memoryDirection % SETS
        cpuArray = bus.getCpuArray()
        localCpu = cpuArray[instruction.getCpuNumber()]
        localController = localCpu.getController()
        localCache = localController.getCache()
        localBlocks = localCache.getBlocks()
        localBlock = localBlocks[scache]
        localBlock.setMemoryDirection(memoryDirection)
        localBlock.setValue(value)
        localBlock.setState(MODIFIED)
        self.invalidateCaches(instruction, bus)
        bus.releaseLock()

    def remoteSearch(self, instruction, bus):

        if(instruction.getOperation() == OPERATIONS[READ_INDEX]):
            self.remoteRead(instruction, bus)

        elif(instruction.getOperation() == OPERATIONS[WRITE_INDEX]):
            self.remoteWrite(instruction, bus)

""" 
                                PROCESSOR SYSTEM MODEL

            It will create an instance of each processor to operate in a parallel way, each
            processor will have an specific instruction generated randomly, this for each one.
            There will be three kind of instructions, read, write and calc (which consumes time).
"""
class CPU:
    
    def __init__(self, number):        
        self.number = number        
        self.currentInstruction = None
        self.controller = None
        self.loaded = 0

        self.assignResources()

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number

    def getCurrentInstruction(self):
        return self.currentInstruction

    def setCurrentInstruction(self, currentInstruction):
        self.currentInstruction = currentInstruction

    def getController(self):
        return self.controller

    def setController(self, controller):
        self.controller = controller

    def getLoaded(self):
        return self.loaded

    def setLoaded(self, loaded):
        self.loaded = loaded

    """
    This function calculates the poisson distribution based on
    m average number of events and x number of successes
    """
    def poissonDistribution(self):
        
        m = randint(PROBABILITY_MIN, PROBABILITY_MAX)
        x = randint(PROBABILITY_MIN, PROBABILITY_MAX)
        probability = ((pow(m, x) * exp(-m)) / factorial(x)) * 100
        return probability

    """
    This function returns an specific operation based on the poisson
    distribution
    """
    def getOperation(self, probability):

        if(probability >= 0 and probability < CALC_PROBABILITY):
            return OPERATIONS[CALC_INDEX]

        elif(probability >= CALC_PROBABILITY and probability < READ_PROBABILITY):
            return OPERATIONS[READ_INDEX]

        else:
            return OPERATIONS[WRITE_INDEX]
    def getMemoryDirection(self, probability):

        # memory direction 0000
        if(probability >= 0 and probability < MEMORY_BLOCKS_PROB[0]):

            return MEMORY_BLOCKS_DIR[0]

        # memory direction 0001
        elif(probability >= MEMORY_BLOCKS_PROB[0] and
            probability < MEMORY_BLOCKS_PROB[1]):

            return MEMORY_BLOCKS_DIR[1]

        # memory direction 0010
        elif(probability >= MEMORY_BLOCKS_PROB[1] and
            probability < MEMORY_BLOCKS_PROB[2]):

            return MEMORY_BLOCKS_DIR[2]

        # memory direction 0011
        elif(probability >= MEMORY_BLOCKS_PROB[2] and
            probability < MEMORY_BLOCKS_PROB[3]):

            return MEMORY_BLOCKS_DIR[3]

        # memory direction 0100
        elif(probability >= MEMORY_BLOCKS_PROB[3] and
            probability < MEMORY_BLOCKS_PROB[4]):

            return MEMORY_BLOCKS_DIR[4]

        # memory direction 0101
        elif(probability >= MEMORY_BLOCKS_PROB[4] and
            probability < MEMORY_BLOCKS_PROB[5]):

            return MEMORY_BLOCKS_DIR[5]

        # memory direction 0110
        elif(probability >= MEMORY_BLOCKS_PROB[5] and
            probability < MEMORY_BLOCKS_PROB[6]):

            return MEMORY_BLOCKS_DIR[6]

        # memory direction 0111
        else:

            return MEMORY_BLOCKS_DIR[7]

    def getValue(self):
        
        probability = trunc(self.poissonDistribution() * 10000)
        while(probability > VALUE_MAX):
            probability = trunc(self.poissonDistribution() * 10000)

        return probability


    def assignResources(self):
        
        controller = Controller()
        cache = Cache()

        for i in range(0, 4):

            cacheBlock = CacheBlock(i, INITIAL_CACHE_STATE, MEMORY_BLOCKS_DIR[0], INITIAL_CACHE_VALUE)
            cache.blocks.append(cacheBlock)


        controller.setCache(cache)      
        self.controller = controller


    def generateInstruction(self):        

        operation = self.getOperation(self.poissonDistribution())
        instruction = Instruction(self.number, operation)

        if(operation != OPERATIONS[CALC_INDEX]):
            
            memoryDirection = self.getMemoryDirection(self.poissonDistribution())
            instruction.setMemoryDirection(memoryDirection)

            if(operation == OPERATIONS[WRITE_INDEX]):
                value = self.getValue()
                instruction.setValue(value)
        
        self.currentInstruction = instruction


    def executeInstruction(self, bus):

        self.controller.resetAlerts()
        localSearch = self.controller.localSearch(self.currentInstruction, bus)
        if(localSearch == MISS):

            self.controller.remoteSearch(self.currentInstruction, bus)

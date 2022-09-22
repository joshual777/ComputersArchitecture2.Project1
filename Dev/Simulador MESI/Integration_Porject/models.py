# libraries
from math import *
from random import *
from constants import *
from threading import *
from time import *

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

class Cache:
    
    def __init__(self):
        self.blocks = []

    def getBlocks(self):
        return self.blocks

    def setBlocks(self, blocks):
        self.blocks = blocks

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

    """
    This function invalidates all caches due to a write
    """
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

    """
    This function checks if the cache has the requested block to read it
    """
    def localRead(self, instruction):

        memoryDirection = instruction.getMemoryDirection()

        blocks = self.cache.blocks

        for block in blocks:

            # memory direction match
            if(block.getMemoryDirection() == memoryDirection):

                state = block.getState()

                # state M, E or S
                if(state == MODIFIED or state == EXCLUSIVE or state == SHARED):

                    # hit
                    return HIT

                #state I
                else:

                    self.readMiss = 1

                    # miss
                    return MISS

        # no memory direction match       
        self.readMiss = 1

        # miss
        return MISS

    """
    This function checks if the cache has the requested block to write it
    """
    def localWrite(self, instruction, bus):

        memoryDirection = instruction.getMemoryDirection()

        value = instruction.getValue()

        blocks = self.cache.blocks

        for block in blocks:

            # memory direction match
            if(block.getMemoryDirection() == memoryDirection):

                block.setValue(value)

                block.setState(MODIFIED)

                self.invalidateCaches(instruction, bus)

                # hit
                return HIT

        # no memory direction match
        self.writeMiss = 1

        # miss
        return MISS

    """
    This functions identifies the current instruction to execute it in the local CPU
    """
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

    """
    This function checks if the other caches have the requested block to read it
    """
    def remoteRead(self, instruction, bus):
        
        # acquire lock
        bus.acquireLock()

        located = 0

        memoryDirection = instruction.getMemoryDirection()

        cpuArray = bus.getCpuArray()

        localCpu = cpuArray[instruction.getCpuNumber()]

        localController = localCpu.getController()

        localCache = localController.getCache()

        localBlocks = localCache.getBlocks()        

        for cpu in cpuArray:

            # ignore local CPU cache
            if(cpu.getNumber() != localCpu.getNumber()):

                remoteController = cpu.getController()

                remoteCache = remoteController.getCache()

                remoteBlocks = remoteCache.getBlocks()

                for remoteBlock in remoteBlocks:    

                    # memory direction match
                    if(remoteBlock.getMemoryDirection() == memoryDirection):

                        state = remoteBlock.getState()

                        # not state I
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

        # release lock
        bus.releaseLock()

    """
    This function writes the requested block in main memory and generate a write-back
    """
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

        # release lock
        bus.releaseLock()

    """
    This functions identifies the current instruction to execute it any remote CPU
    """
    def remoteSearch(self, instruction, bus):
        
        # read operation
        if(instruction.getOperation() == OPERATIONS[READ_INDEX]):

            self.remoteRead(instruction, bus)

        # write operation
        elif(instruction.getOperation() == OPERATIONS[WRITE_INDEX]):
    
            self.remoteWrite(instruction, bus)

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

    """
    This function returns an specific memory direction based on the
    poisson distribution
    """
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

    """
    This function generates a number of 16 bits based on poisson
    distribution
    """
    def getValue(self):
        
        probability = trunc(self.poissonDistribution() * 10000)

        while(probability > VALUE_MAX):
            
            probability = trunc(self.poissonDistribution() * 10000)

        return probability

    """
    This function assign controller and cache to the CPU
    """
    def assignResources(self):
        
        # create controller
        controller = Controller()

        # create cache
        cache = Cache()

        for i in range(0, 4):

            cacheBlock = CacheBlock(i, INITIAL_CACHE_STATE, MEMORY_BLOCKS_DIR[0], INITIAL_CACHE_VALUE)

            cache.blocks.append(cacheBlock)

        # assign cache to controller
        controller.setCache(cache)

        # assign controller to CPU        
        self.controller = controller

    """
    This function generates a new instruction for the received CPU
    """
    def generateInstruction(self):        
        
        operation = self.getOperation(self.poissonDistribution())

        instruction = Instruction(self.number, operation)

        # not calc operation
        if(operation != OPERATIONS[CALC_INDEX]):
            
            memoryDirection = self.getMemoryDirection(self.poissonDistribution())

            instruction.setMemoryDirection(memoryDirection)

            # write operation
            if(operation == OPERATIONS[WRITE_INDEX]):
            
                value = self.getValue()

                instruction.setValue(value)
        
        self.currentInstruction = instruction

    """
    This functions allows the CPU and controller to execute a new instruction 
    """
    def executeInstruction(self, bus):

        self.controller.resetAlerts()

        localSearch = self.controller.localSearch(self.currentInstruction, bus)

        # miss
        if(localSearch == MISS):

            self.controller.remoteSearch(self.currentInstruction, bus)

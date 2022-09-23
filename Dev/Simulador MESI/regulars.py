#List of functions 
OPERATIONS = ["CALC", "READ", "WRITE"]

#ID of each funtion in the tab
CALC_INDEX = 0
READ_INDEX = 1
WRITE_INDEX = 2

MEMORY_BLOCKS_DIR = [0, 1, 2, 3, 4, 5, 6, 7]

#Setting probabilty method 
MEMORY_BLOCKS_PROB = [5/2,  5,  15/2, 10, 25/2, 15, 35/2]

PROBABILITY_MIN = 1
PROBABILITY_MAX = 14

VALUE_MAX = 18446744073709551615

CALC_PROBABILITY = 20/3
READ_PROBABILITY = 40/3

#Default state
INITIAL_CACHE_STATE = "I"
INITIAL_CACHE_VALUE = 0

#Default memory intial point
INITIAL_MAIN_MEMORY_VALUE = 0

#Protocol MESI STATE
MODIFIED = "M"
EXCLUSIVE = "E"
SHARED = "S"
INVALID = "I"

#Miss and Hit cache 
HIT = 1
MISS = 0

SETS = 4

#Timer for execution
TIMER = 1

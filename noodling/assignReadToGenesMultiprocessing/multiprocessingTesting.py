"""
Marcus Viscardi April 1st, 2020

Messing around with multiprocessing for use in assignReadsToGenesX.py script(s)

Major test will be to compare the speeds of writing a bunch of csv lines to a file with:
    1. Multiprocessing, with each process writing to the csv on its own
    2. Multiprocessing, with each process writing to a list/dict/df, then that being writen to csv all at once
    3. Vectorizing (word? not sure), having the process act on the entire df to try and take advantage of the
        faster C backend of vectorized methods

Main plan will be to implement a toy method for each of the above then run it at a very high repitition
"""
from multiprocessing import Pool,Queue,Process
from itertools import product,repeat
import random,time
"""
import pandas as pd
import numpy as np

# Imports from assignReadsToGenes4.py >>>
import sys, os, collections, csv, common, re, time, pickle, copy, linecache
#import pandas
from logJosh import Tee

csv.field_size_limit(sys.maxsize)
# <<< Imports from assignReadsToGenes4.py
"""
#inputs is an array of tuples
outputFile = 'log.log.log'
queue = Queue()
def writing_process(total,BATCH_SIZE=10):
    writtenElements = 0
    memory = {} #unorderd
    output = [] #ordered
    while writtenElements != total:
        if queue.qsize() != 0:
            index,value = queue.get()
            if len(output) == index:
                output.append(str(value))
            else:
                memory[index] = str(value)
                
        try: #Try to add to the output in an ordered way.
            output.append(memory[len(output)])
            print(f"Appened {memory[len(output)]}",len(output))
        except KeyError:
            pass
        
        #write if I have a batch size of elements.
        if int(len(output)/BATCH_SIZE) > int(writtenElements/BATCH_SIZE) or total-writtenElements<BATCH_SIZE:
            elementsToWrite = output[writtenElements:]
            with open(outputFile,'a') as f:
                f.write('\n'.join(elementsToWrite))
                f.write('\n')
            writtenElements += len(elementsToWrite)
    
def single_process(index,number,power):
    for i in range(10**5):
        value = number**power
    queue.put((index,value))
    return value
    
def wil_multi(indexes,inputNumbers,power,CPU_CORES=4):
    writer = Process(target=writing_process,args=(len(indexes),))
    writer.start()
    with Pool(CPU_CORES) as p:
        results = p.starmap(single_process,zip(indexes,inputNumbers,repeat(power)))
        
    for number,power,result in zip(inputNumbers,repeat(inputPower),results):
        #print(f"Taking {number} to the power of {power} is {result}")
        pass
    

def multiprocessing_with_csv():
    def single_process_to_csv():
        pass
    pass


def multiprocessing_with_list():
    def single_process_to_list():
        pass
    pass


def vectorized_processing():
    pass


def main(number_of_repititions: int):
    pass


if __name__ == '__main__':
    #main(1)
    SIZE = 100
    
    #rewrite output file
    with open(outputFile,'w+') as f:
        f.write("")

    indexes = [i for i in range(SIZE)]
    inputNumbers = [i for i in range(SIZE)]
    inputPower = 2
    wil_multi(indexes,inputNumbers,inputPower)

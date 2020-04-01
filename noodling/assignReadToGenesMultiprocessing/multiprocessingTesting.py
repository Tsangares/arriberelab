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
import random,time,sys
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
    print("Writer initialized.")
    writtenElements = 0
    memory = {} #unorderd
    output = [] #ordered
    currentIndex = 0
    while writtenElements != total:
        if queue.qsize() != 0:
            index,value = queue.get()
            if currentIndex == index:
                output.append(str(value))
                print(f"Appened {value} at {currentIndex}.")
                currentIndex += 1
            else:
                memory[index] = str(value)
        try: #Try to add to the output in an ordered way.
            value = memory[currentIndex]
            output.append(value)
            print(f"Appened {value} at {currentIndex}.")
            del memory[currentIndex]
            currentIndex += 1
        except KeyError as e:
            pass
        #write if I have a batch size of elements.
        currentBatch = int((writtenElements + len(output))/BATCH_SIZE)
        lastBatch    = int(writtenElements/BATCH_SIZE)
        remainingElements = total-writtenElements
        if currentBatch > lastBatch or remainingElements<BATCH_SIZE:
            with open(outputFile,'a') as f:
                f.write('\n'.join(output))
                f.write('\n')
            writtenElements += len(output)
            output=[]
    
def single_process(index,number,power):
    for i in range(10**4):
        value = number**power
    queue.put((index,value))
    
def wil_multi(indexes,inputNumbers,power,CPU_CORES=4):
    writer = Process(target=writing_process,args=(len(indexes),))
    writer.start()
    with Pool(CPU_CORES) as p:
        results = p.starmap(single_process,zip(indexes,inputNumbers,repeat(power)))

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
    SIZE = 10**2
    #rewrite output file
    with open(outputFile,'w+') as f:
        f.write("")

    indexes = [i for i in range(SIZE)]
    inputNumbers = [i for i in range(SIZE)]
    inputPower = 2
    wil_multi(indexes,inputNumbers,inputPower)

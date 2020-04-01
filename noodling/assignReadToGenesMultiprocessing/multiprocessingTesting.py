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
from multiprocessing import Pool 
from itertools import product
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
def single_process(number,power):
    return number**power
def wil_multi(inputNumbers,inputPowers,CPU_CORES=4):
    with Pool(CPU_CORES) as p:
        results = p.starmap(single_process,zip(inputNumbers,inputPowers))
        
    for number,power,result in zip(inputNumbers,inputPowers,results):
        print(f"Taking {number} to the power of {power} is {result}")

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
    inputNumbers = [i for i in range(100)]
    inputPowers = [i for i in range(100)]
    wil_multi(inputNumbers,inputPowers)

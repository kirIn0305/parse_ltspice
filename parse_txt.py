# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

def get_fulldata(fname):
    data = []
    with open(fname,mode='r') as f:
        for num, l in enumerate(f.readlines()):
            l = l.rstrip('\n')
            data.append(l.split('\t'))
    
    return data

def get_header(fname):
    with open(fname,mode='r') as f:
        header = f.readline().rstrip('\n').split('\t')

    return header

def get_step(fname):
    step = []
    with open(fname,mode='r') as f:
        for num, l in enumerate(f.readlines()):
            check = "Step Information:" in l
            if check == True:
                step.append(num)

    return step

def get_parsedata(fname):
    data_step = []
    data = get_fulldata(fname)
    step = get_step(fname)
    if len(step) == 0:
        data_step.append(data[1:])
    else:
        # append last cordinate
        step.append(step[-1] + step[1] - step[0])
        for num in range(len(step) - 1):
            print(data[step[num]])
            start = step[num] + 1
            end = step[num+1] - 1
            print("data {0} to {1}".format(start, end))
            data_step.append(data[start : end])
            
    return convert_float(data_step)


def convert_float(datalist):
    tmplist=[]
    for data in datalist:
        tmpdata = np.array(data, dtype=float)
        tmplist.append(tmpdata)
    
    return tmplist


if __name__ == '__main__':
    get_parsedata("./sram_snmV1.txt")

    

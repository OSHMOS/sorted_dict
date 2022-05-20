from quickSort import *
from itertools import islice

def do_sort(input_file):
    data_file = open(input_file)
    A = []
    dct = {}
    for line in data_file.readlines():
        lpn = line.split()[0]
        A.append(lpn)
        if lpn in dct:
            dct[lpn] +=1
        else:
            dct[lpn] =1

    value = [dict.values()]
    quick_sort( value , 0 , len(dct)-1 )
    islice(dct.items(),10)
    print(dct.items())

if __name__ == "__main__":
    do_sort("C:/Users/User/OneDrive/바탕 화면/list/week11/linkbench_short.trc")
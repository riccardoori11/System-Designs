# How would we go about checking if there are duplicate files in a folder
# Naive approach is checking each folder 1 by 1 and comparing the bytes inside

import sys
import pathlib

def samebytes(file1,file2):

    left = open(file1,'rb').read()
    right = open(file2,'rb').read()

    return left == right

def find_duplicates(file):

    matches = []

    for i in file:
        for j in file:
            if samebytes(i,j):
                matches.append((i,j))
    
    return matches

if __name__ == '__main__':
    duplicates = find_duplicates(sys.argv[1:])
    for (left, right) in duplicates:
        print(left, right)



#Shows you the file in the directory texts with the suffix .txt
#p = pathlib.Path('texts')
#print(list(p.glob('**/*.txt')))







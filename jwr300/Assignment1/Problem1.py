#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 1, Problem 1
#Ror a given starting and end point, this calculates the maximum cycle length of the collatz conjecture

import sys

def main(argv):

    begin = int(sys.argv[1])
    end = int(sys.argv[2])
    tracker = end
    counter = 1 #set to 1 to include endpoints

    while tracker > begin:
        #if tracker is even, divide by 2
        if tracker % 2 == 0:
            tracker = tracker / 2
            counter += 1
        elif tracker % 2 == 1:
            tracker = 3 * tracker + 1
            counter += 1
            
    print str(begin) + " " + str(end) + " " + str(counter)


if __name__ == "__main__":
   main(sys.argv)




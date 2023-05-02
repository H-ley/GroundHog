#! /usr/bin/python3

from sys import argv
from predicition import groundhog

def display_help():
    print("SYNOPSIS")
    print("\t./groundhog period", end='\n\n')
    print("DESCRIPTION")
    print("\tperiod\tthe number of days defining a period")

if __name__ == "__main__":
    if (len(argv) == 1 or argv[1] == '-h'):
        display_help()
    else:
        groundhog(int(argv[1]))

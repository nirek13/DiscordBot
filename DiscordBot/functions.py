
import math
from multiprocessing.sharedctypes import Value

import time 
import sys
import csv
import random
import re
from pyparsing import Word
import operator
import random

def capitals():
    # importing csv module


# csv file name
        filename = "country-list.csv"
        capitols = []
        countries = []
# initializing the titles and rows list
        fields = []
        rows = []

# reading csv file
        with open(filename, 'r') as csvfile:
# creating a csv reader object
            csvreader = csv.reader(csvfile)
    
# extracting field names through first row
            fields = next(csvreader)

# extracting each data row one by one
            for row in csvreader:
                rows.append(row)
                capitols.append(row)
                countries.append(row)
# get total number of rows
        num = random.randint(0 , 248)
        country = countries[num]
        answer = input(f"what is the capital of {country[0]}:")
        return country







        




        



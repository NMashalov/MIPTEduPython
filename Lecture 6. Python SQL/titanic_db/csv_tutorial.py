import csv
import itertools
import pprint

with open('titanic.csv','r') as f:
    reader = csv.reader(f) 
    headers = next(reader, None)
    print('headers',headers)

    print("sample:")
    print((i for i in itertools.islice(reader, 3)))   
    
import csv
import sys


def compareFields(field1, field2, inputFiles=sys.argv[1:]):

    for inputFile in inputFiles:
        print inputFile
        
        reader = csv.reader(open(inputFile, 'rb'))
        for row in reader:
            if row[field1] > row[field2]:
                print 'Row %d: Field %i > Field %i' % (reader.line_num, field1, field2)

if __name__ == "__main__":
    compareFields(4, 8)
import sys

def columnExtractor(column, delimiter=",", inputFiles=sys.argv[1:]):
    for inputFile in inputFiles:
        outputFile = inputFile + "-columnExtracted"
        with open(inputFile, 'r') as src:
            with open(outputFile, 'w') as dest:
                for line in src:
                    dest.write(line.split(delimiter)[column] + "\n")

if __name__ == "__main__":
    columnExtractor(4, "`")
import glob
import os

inputFilesList = glob.glob('/workspace/*.csv')
outputDir = "./extractedLines/"
if not os.path.exists(outputDir):
    os.makedirs(outputDir)

# Specify the  with strings for filtering, set delimiter
strings = "stringsToExtract.csv"
stringsDelimiter = "\n"
# Create a list of strings from a delimited file (to iterate over them later)
listOfStrings = [line.split(stringsDelimiter)[0] for line in open(strings, 'r')]

for filePath in inputFilesList:
    output = os.path.join(outputDir, os.path.splitext(filePath)[0] + '-extracted.csv')
    
    with open(filePath, 'r') as src:
        with open(output, 'w') as dest:
            for line in src:
                if any(string in line for string in listOfStrings):
                    dest.write(line)
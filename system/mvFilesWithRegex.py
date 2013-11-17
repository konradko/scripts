import os
import glob
import re
import shutil


def mvFilesWithRegex(dirPath, regex, destDir):
    for filePath in glob.glob(dirPath):
        match = re.search(r'%s' % regex, filePath)
        if match:
            if not os.path.exists(destDir):
               os.makedirs(destDir)
            shutil.move(filePath, destDir)
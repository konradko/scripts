import os

def replaceInName(dirPath, mapping, prefix="", suffix=""):
	'''Dir must be path, mapping - a dict with string:replacemnt pairs, prefix and
	suffix are optional. Only one change per file per use'''
	for filename in os.listdir(dirPath):
		for key in mapping:
			if key in filename:
				new_name =  prefix + filename.replace(key, mapping[key]) + suffix
				os.rename(dirPath + filename, dirPath + new_name)
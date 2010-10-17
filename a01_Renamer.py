# Renamer.py
# class defining Renamer objects, as used by rn.py

import os

# TODO: implement error handling and checking for all setter methods
# TODO: use verbose regular expressions for better documentation

class Renamer():
	# TODO: create _DEBUG flag and implement it
	def __init__(self, fileList = (), dirPath = "", namingMask = {}, namingMaskString = "", 
			renamingMaskString = "", namingMaskVariableSeparator = "||", namingMaskVariableTag = "%", debug = False):
		# TODO: use setter functions for this init
		setFileList(fileList)
		setDirPath(dirPath)
		setNamingMask(namingMask)
		setNamingMaskString(namingMaskString)
		setRenamingMaskString(renamingMaskString)
		setRenamingMask(renamingMask)
		setNAMING_MASK_VARIABLE_SEPARATOR(namingMaskVariableSeparator)
		# BOOKMARK
		self.NAMING_MASK_VARIABLE_SEPARATOR = namingMaskVariableSeparator
		self.NAMING_MASK_VARIABLE_TAG	 = namingMaskVariableTag
		self._DEBUG = debug
	
	def parseNamingMaskString(self, namingMaskString):
		parselist = namingMaskString.split(self.NAMING_MASK_VARIABLE_SEPARATOR)
		for varstring in parselist:
			var, regex = varstring.split("=")
			var = var.strip()
			regex = regex.strip()
			self.namingMask[var] = regex
		if self._DEBUG:
			self.printNamingMask()

	def printNamingMask(self):
		print "Printing namingMask ..."
		for key in self.namingMask.keys():
			print key + ' = ' + self.namingMask[key]
	
	def setNamingMaskString(self, namingMaskString):
		self.namingMaskString = namingMaskString
		self.parseNamingMaskString(namingMaskString)

	def getNamingMaskString():
		return self.namingMaskString

	def setNamingMask(self, namingMask):
		self.namingMask = namingMask

	def getNamingMask():
		return self.namingMask

	def setRenamingMask(self, renamingMask):
		self.renamingMask = renamingMask
	
	def getRenamingMask():
		return self.renamingMask

	def getRenamingMaskString():
		return self.renamingMaskString

	def setRenamingMaskString(self, renamingMaskString):
		self.renamingMaskString = renamingMaskString

	def setFileList(self, fileList):
		self.fileList = fileList

	def getFileList():
		return self.fileList

	def setDirPath(self, dirPath):
		self.dirPath = dirPath
	
	def getDirPath():
		return self.dirPath

	def getNAMING_MASK_VARIABLE_SEPARATOR():
		return self.NAMING_MASK_VARIABLE_SEPARATOR

	def setNAMING_MASK_VARIABLE_SEPARATOR(self, namingMaskVariableSeparator):
		self.NAMING_MASK_VARIABLE_SEPARATOR = namingMaskVariableSeparator
	
	def getNAMING_MASK_VARIABLE_TAG():
		return self.NAMING_MASK_VARIABLE_TAG

	def setNAMING_MASK_VARIABLE_TAG(self, namingMaskVariableTag):
		self.NAMING_MASK_VARIABLE_TAG = namingMaskVariableTag

	# create dictionary of renamed files
	def 
	# use namingMask dictionary to parse file name mask into variables
	def parseFileNamingMask(self, filename):
		pass

	# TODO: implement appropriate error checking and handling
	#	for now, this assumes user knows what he is doing
	def renameFiles(self):
		print "renaming files ..."
		for file in self.fileList:
			os.rename(file, self.renamedFiles[file])


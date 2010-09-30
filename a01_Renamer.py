# Renamer.py
# class defining Renamer objects, as used by rn.py

# TODO: implement error handling and checking for all setter methods

class Renamer():
	# TODO: create _DEBUG flag and implement it
	def __init__(self, fileList = (), dirPath = "", nameMask = {}, nameMaskString = "", renamingMask = "", nameMaskVariableSeparator = "||", nameMaskVariableTag = "%", debug = False):
		self.fileList = fileList
		self.dirPath = dirPath
		self.nameMask = nameMask
		self.nameMaskString = nameMaskString
		self.renamingMask = renamingMask
		self.NAME_MASK_VARIABLE_SEPARATOR = nameMaskVariableSeparator
		self.NAME_MASK_VARIABLE_TAG	 = nameMaskVariableTag
		self._DEBUG = debug
	
	def parseNameMaskString(self, nameMaskString):
		parselist = nameMaskString.split(self.NAME_MASK_VARIABLE_SEPARATOR)
		for varstring in parselist:
			var, regex = varstring.split("=")
			var = var.strip()
			regex = regex.strip()
			self.nameMask[var] = regex
		if self._DEBUG:
			self.printNamingMask()

	def printNamingMask(self):
		print "Printing namingMask ..."
		for key in self.nameMask.keys():
			print key + ' = ' + self.nameMask[key]
	
	def setNameMaskString(self, nameMaskString):
		self.nameMaskString = nameMaskString
		self.parseNameMaskString(nameMaskString)

	def getNameMaskString():
		return self.nameMaskString

	def setNameMask(self, nameMask):
		self.nameMask = nameMask

	def getNameMask():
		return self.nameMask

	def setRenamingMask(self, renamingMask):
		self.renamingMask = renamingMask
	
	def getRenamingMask():
		return self.renamingMask

	def setFileList(self, fileList):
		self.fileList = fileList

	def getFileList():
		return self.fileList

	def setDirPath(self, dirPath):
		self.dirPath = dirPath
	
	def getDirPath():
		return self.dirPath

	def renameFiles(self):
		print "renaming files ..."
		pass


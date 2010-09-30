#!/usr/bin/python

# concepts for the app:
# naming mask = 	user-defined variables that identify substrings of interest
#									within the file name.  These variables are of the format
#									"%varname% = <regex matching string> || %varname2% = <regex>
# renaming mask = user-defined string containing naming mask variables and 
#									a filename mask for use in renaming


# imports
import sys
import os
import getopt
import Renamer

# define constants

# main program
def main(argv):
	# define command line option strings for getopts
	cmdLineShortOpts = 'hvd:n:m:r:f:'
	cmdLineLongOpts = ['help', 'debug', 'dir=', 'name_mask=', 'renaming_mask=', 'replace=', 'files=']
	
	# set debugging on
	global _DEBUG
	_DEBUG = True 
	
	# create Renamer object
	fileRenamer = Renamer.Renamer()

	# process command line options
	try:
		process_args(argv, cmdLineShortOpts, cmdLineLongOpts, fileRenamer)
	
	# TODO: change this to use argparse
	except getopt.GetoptError:
		usage()
		if _DEBUG:
			print "exiting due to GetoptError"
		sys.exit(2)

	# print the resulting naming mask variables of the Renamer object
	fileRenamer.printNamingMask()

# parse arguments
# 	help
#		debug
#		directory
#		naming_mask
#		replace_chars
#		rename_mask
#		file_list
def process_args(argv, cmdLineShortOpts, cmdLineLongOpts, fileRenamer):
	opts, args = getopt.getopt(argv, cmdLineShortOpts, cmdLineLongOpts)
	if _DEBUG:
		print 'printing opts...'
		for o in opts: print o

	# process command-line options
	for opt, arg in opts:
		if opt in ('v', '--debug'):
			# turn on debugging output
			# TODO: this should set the Renamer object's debug mode on
			pass
		elif opt in('-h', '--help'):
			# show usage help
			usage()
			sys.exit()
		elif opt in ('d', '--dir'):
			# set directory to first command line option
			fileRenamer.setDirPath(arg)
		elif opt in ('n', '--name_mask'):
			fileRenamer.setNameMaskString(arg)
		elif opt in ('m', '--renaming_mask'):
			fileRenamer.setRenamingMask(arg)
		elif opt in ('r', '--replace'):
			# replacestring = arg
			# TODO: implement string replacement in Renamer?
			pass
		elif opt in ('f', '--files'):
			# identify list of files to rename
			fileRenamer.setFileList(arg)
	
# get directory listing, if appropriate
# return a list of files in given directory
def getfiles(dir):
	if _DEBUG:
		print "in getfiles"
	return [f for f in os.listdir(dir) if os.path.isfile(os.listdir(dir))]

# identify file list
# present sample renamed file
# prompt for confirmation
# rename files
# log renaming actions to text file

# print command line usage
def usage():
	print "usage()"
	pass
	#print sys.argv[0] + "USAGE HERE"


if __name__ == '__main__':
	main(sys.argv[1:])

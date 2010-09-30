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

# define constants
NAMING_MASK_VARIABLE_SEPARATOR = '||'
NAMING_MASK_VARIABLE_TAG = '%'

# main program
def main(argv):
	# define command line option strings for getopts
	cmdLineShortOpts = 'hvd:n:m:r:f:'
	cmdLineLongOpts = ['help', 'debug', 'dir=', 'naming_mask=', 'renaming_mask=', 'replace=', 'files=']
	
	# set debugging on
	global _DEBUG
	_DEBUG = True 
	
	# process command line options
	try:
		namingMaskVars = process_args(argv, cmdLineShortOpts, cmdLineLongOpts)
	
	# TODO: change this to use argparse
	except getopt.GetoptError:
		usage()
		if _DEBUG:
			print "exiting due to GetoptError"
		sys.exit(2)

# parse arguments
# 	help
#		debug
#		directory
#		naming_mask
#		replace_chars
#		rename_mask
#		file_list
def process_args(argv, cmdLineShortOpts, cmdLineLongOpts):
	opts, args = getopt.getopt(argv, cmdLineShortOpts, cmdLineLongOpts)
	if _DEBUG:
		print 'printing opts'
		for o in opts: print o

	# process command-line options
	for opt, arg in opts:
		if opt in ('v', '--debug'):
			# turn on debugging output
			pass
		elif opt in('-h', '--help'):
			# show usage help
			usage()
			sys.exit()
		elif opt in ('d', '--dir'):
			# set directory to first command line option
			dirPath = arg
			if _DEBUG:
				print 'just set dirPath'
		elif opt in ('n', '--naming_mask'):
			# split the input regex string
			#parsestrings = split_input_regex_string(arg)
			searchdict = split_parse_string_variables(arg)
			if _DEBUG:
				print 'just split input parse string'
		elif opt in ('m', '--renaming_mask'):
			renamemask = arg
			if _DEBUG:
				print 'just set renamemask'
		elif opt in ('r', '--replace'):
			replacestring = arg
			if _DEBUG:
				print 'just set replacestring'
		elif opt in ('f', '--files'):
			# identify list of files to rename
			fileList = arg
			if _DEBUG:
				print 'printing files'
				#for file in fileList:
				#	print file
	if dirPath:
		# if a dir was passed as an arg, get a list of files in the dir
		fileList = getfiles(dirPath)
	elif not fileList:
		print 'a list of files to rename is required input'
		sys.exit(2)
	
	# return the dictionary of naming mask variables
	return searchdict

	


# get directory listing, if appropriate
# return a list of files in given directory
def getfiles(dir):
	if _DEBUG:
		print "in getfiles"
	return [f for f in os.listdir(dir) if os.path.isfile(os.listdir(dir))]

# parse string_identifiers
#def split_input_regex_string(instring):
#	if _DEBUG:
#		print 'splitting input regex string'
#		print instring.split(INPUT_REGEX_SPLIT_TOKEN)
#	return instring.split(INPUT_REGEX_SPLIT_TOKEN)

def split_parse_string_variables(inString):
	if _DEBUG:
		print inString.split(NAMING_MASK_VARIABLE_TAG)
	# split naming mask string into separate variables for processing
	parselist = inString.split(NAMING_MASK_VARIABLE_TAG)
	
	vardict = {}
	for instring in parselist:
		left, right = instring.split('=')
		left = left.strip()
		right = right.strip()
		vardict[left] = [right]
	if _DEBUG:
		print 'creating parse string variables'
		for k in vardict.keys():
			print vardict[k]
	return vardict

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

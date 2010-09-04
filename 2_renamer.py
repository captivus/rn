#!/usr/bin/python
import sys
import os
import getopt

# define constants
INPUT_REGEX_SPLIT_TOKEN = '||'
PARSE_STRING_VARIABLE_TOKEN = '%'

def main(argv):
	# define command line option strings for getopts
	cmdLineShortOpts = 'hvd:s:m:r:f:'
	cmdLineLongOpts = ['help', 'debug', 'dir=', 'search=', 'mask=', 'replace=', 'files=']
	global _DEBUG
	_DEBUG = False
	# process command line options
	try:
		opts, args = getopt.getopt(argv, cmdLineShortOpts, cmdLineLongOpts)
		print 'printing opts'
		for o in opts: print o
		
		# process command-line options
		for opt, arg in opts:
			if opt in ('v', '--debug'):
				# turn on debugging output
				_DEBUG = True 
				
			elif opt in('-h', '--help'):
				# show usage help
				usage()
				sys.exit()
			elif opt in ('d', '--dir'):
				# set directory to first command line option
				dirPath = arg
				if _DEBUG:
					print 'just set dirPath'
			elif opt in ('s', '--search'):
				# split the input regex string
				parsestrings = split_input_regex_string(arg)
				searchdict = split_parse_string_variables(parsestrings)
				if _DEBUG:
					print 'just split input parse string'
			elif opt in ('m', '--mask'):
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
	except getopt.GetoptError:
		usage()
		if _DEBUG:
			print "exiting due to GetoptError"
		sys.exit(2)

# return a list of files in given directory
def getfiles(dir):
	if _DEBUG:
		print "in getfiles"
	return [f for f in os.listdir(dir) if os.path.isfile(os.listdir(dir))]

# print command line usage
def usage():
	print "usage()"
	pass
	#print sys.argv[0] + "USAGE HERE"

def split_input_regex_string(instring):
	if _DEBUG:
		print 'splitting input regex string'
		print instring.split(INPUT_REGEX_SPLIT_TOKEN)
	return instring.split(INPUT_REGEX_SPLIT_TOKEN)

def split_parse_string_variables(inlist):
	vardict = {}
	for instring in inlist:
		left, right = instring.split('=')
		left = left.strip()
		right = right.strip()
		vardict[left] = [right]
	if _DEBUG:
		print 'creating parse string variables'
		for k in vardict.keys():
			print vardict[k]
	return vardict

if __name__ == '__main__':
	main(sys.argv[1:])

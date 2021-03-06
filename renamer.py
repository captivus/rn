#!/usr/bin/python
import sys
import os
import getopt

DEBUG = True

# TODO:  add help / usage output

def main(argv):
	# define command line option strings for getopts
	cmdLineShortOpts = ['hd:m:f:']
	cmdLineLongOpts = ['help', 'dir', 'mask', 'files']
	
	# process command line options
	try:
		opts, args = getopt.getopt(argv, cmdLineShortOpts, cmdLineLongOpts)
		# set directory to first command line option
		dirPath = args[0]
		if DEBUG:
			print "just set dirPath"
			for arg in args:
				print arg
		# set rename mask from command line
		if argv[1] != None:
			pass
		if argv[2:] != None:
			# set file list to second+ command line option(s)
			fileList = args[2:]
			if DEBUG:
					print 'printing files'
					for f in fileList:
						print f
	except getopt.GetoptError:
		usage()
		if DEBUG:
			print "exiting due to GetoptError"
		sys.exit(2)
	

# return a list of files in given directory
def getfiles(dir):
	if DEBUG:
		print "in getfiles"
	return [f for f in os.listdir(dir) if os.path.isfile(os.listdir(dir))]


# print command line usage
def usage():
	print "usage()"
	pass
	#print sys.argv[0] + "USAGE HERE"


if __name__ == '__main__':
	if DEBUG:
		print "starting main()"
	main(sys.argv)

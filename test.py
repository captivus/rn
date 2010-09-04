import sys
import getopt

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "","")
	except getopt.GetoptError:
		print 'Exiting due to error' + GetoptError
		sys.exit(2)

	for arg in args:
		print 'arg: ' + arg
	
	print getopt.getopt(argv, '','').keys

	if __name__ == main:
		main(sys.argv[1:])

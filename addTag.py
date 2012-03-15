#!/usr/bin/python

import sys

def main(*args):
	if(len(sys.argv)<3):
		print "Usage: %s tag file"%sys.argv[0]
		return 1
	
	return 0
if __name__ == "__main__":
	sys.exit(main(*sys.argv))

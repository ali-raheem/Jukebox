#!/usr/bin/python
import serial, os, sys, sqlite3

def play(code):
	try:
		c.execute('select cmd from tags where tag=?',(code,))
	except sqlite3.OperationalError:
		print "Run addTag.py with no commands to set up the db."
		sys.exit(1)
	result = c.fetchone()
	if(result):
		print result[0]
		os.system(result[0]+"&")
	else:
		print "Tag not found!"
def parse(code):
	code = code.split('-')[1]
	try:
		code = code.split('\r')[0]
	except IndexError:
		try:
			code = code.split('\n')[0]
		except IndexError:
			print "Probs not a code."
	return code

db_name = "db"
db = sqlite3.connect(db_name)
c = db.cursor()

s = serial.Serial("/dev/ttyACM0", 115200)
s.open()
def main():
	while 1:
		if(s.inWaiting()):
			code =  s.read(s.inWaiting())
			print "Read code",code,"..."
			code = parse(code)
			play(code)

if __name__ == "__main__":
        sys.exit(main())



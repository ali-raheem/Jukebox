#!/usr/bin/python
import serial, os, sys, sqlite3

s = serial.Serial("/dev/ttyACM0", 115200) # Change me to the device
dbName = "db"
db = sqlite3.connect(dbName)
c = db.cursor()
s.open()
lastTag = 0

def parse(code):
#Should return a plain string used as the SQL id.
	code = code.split('-')[1]
	try:
		code = code.split('\r')[0]
	except IndexError:
		try:
			code = code.split('\n')[0]
		except IndexError:
			print "Probs not a code."
	return code

def play(code):
	global lastTag
	try:
		c.execute('select cmd,name from tags where tag=?',(code,))
	except sqlite3.OperationalError:
		c.execute('create table tags (id INTEGER PRIMARY KEY, tag TEXT UNIQUE, name TEXT, cmd TEXT)')
		play(code)
	result = c.fetchone()
	if(result):
		cmd = result[0]
		name = result[1]
		lastTag = code
		print "Loading %s..."%name
		os.system(cmd+"&")
	else:
		print "Tag not found!"
		if(raw_input("Would you like to add it? [y/n]")!='y'):
			return 1
		name = raw_input("Give it a name: ")
		cmd = raw_input("What command should be run: ")
		c.execute("insert into tags values (NULL, ?, ?, ?)", (code, name, cmd, ))
		print "Added %s (%s) to run '%s'"%(name, code, cmd)
		db.commit()
		return 0

def main():
	while 1:
		if(s.inWaiting()):
			code =  s.read(s.inWaiting())
			code = parse(code)
			print "Read code %s..."%code
			if(code != lastTag):
				print code,lastTag
				play(code)
			s.flushOutput()
if __name__ == "__main__":
        sys.exit(main())



#!/usr/bin/python
import serial, os, sys, sqlite3, re

dbName = "db"
serialDevice = "/dev/serial/by-id/usb-Olimex_Ltd._CDC_Serial_Port_for_MOD-RFID125-USBSTICK_OL25B6F000138CD-if00"
regex = re.compile('([a-fA-F0-9])+')
lastTag = 0
s = 0
db = 0
c = 0

def init_serial():
	global s
	s = serial.Serial(serialDevice, 115200)
	s.open()

def init_db():
	global db
	global c
	db = sqlite3.connect(dbName)
	c = db.cursor()
	try:
		c.execute("select * from tags")
	except sqlite3.OperationalError:
		print "Creating database."
		c.execute('create table tags (id INTEGER PRIMARY KEY, tag TEXT UNIQUE, name TEXT, cmd TEXT)')
		db.commit()
	l = c.fetchall()
	print "%d tags known."%len(l)

def parse(code):
#Should return a plain string used as the SQL tag.
	global regex
	index = regex.search(code).span()
	return code[index[0]:index[1]]

def play(code):
	global lastTag
	c.execute('select cmd,name from tags where tag=?',(code,))
	result = c.fetchone()
	if(result):
		cmd = result[0]
		name = result[1]
		lastTag = code
		print "Loading %s..."%name
		os.system(cmd)
	else:
		print "Tag not found!"
		if(raw_input("Would you like to add it? [y/n] ")!='y'):
			return 1
		name = raw_input("Give it a name: ")
		cmd = raw_input("What command should be run: ")
		if(raw_input("So add %s (%s) to run '%s'(make sure this is escaped)? [y/n] "%(name,code,cmd))!='y'):
			return 1
		c.execute("insert into tags values (NULL, ?, ?, ?)", (code, name, cmd, ))
		print "Added %s (%s) to run '%s'"%(name, code, cmd)
		db.commit()
		return 0

def wait():
	while 1:
		if(s.inWaiting()):
			code =  s.read(s.inWaiting())
			code = parse(code)
			print "Read code %s..."%code
			if(code != lastTag):
				play(code)
			s.flushOutput()
def main():
	init_db()
	init_serial()
	wait()

if __name__ == "__main__":
        sys.exit(main())



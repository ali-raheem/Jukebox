#!/usr/bin/python

import sys, sqlite3

db_name = 'db'
def main(*args):
	db = sqlite3.connect(db_name)
	c = db.cursor()
	if(len(sys.argv)!=3):
		print "Usage: %s tag file"%sys.argv[0]
		print "Table stats"
		try:
			c.execute('select * from tags')
			print "Found %d commands."%c.rowcount
		except sqlite3.OperationalError:
			print "Creating database table."
			c.execute('create table tags (tag text, cmd text)')
		return 1
	tag = sys.argv[1]
	cmd = sys.argv[2]
	print "Adding",tag,"with command",cmd,"to db."
	try:
		c.execute("select cmd from tags where tag=?",(tag, ))
	except sqlite3.OperationalError:
                        print "Creating database table."
                        c.execute('create table tags (tag text, cmd text)')
	found = c.fetchone()
	if(found):
		print "Found tag",tag,"with cmd",found[0]
	else:
		c.execute("insert into tags values (?, ?)", (tag, cmd, ))

	db.commit()
	c.close()

	return 0
if __name__ == "__main__":
	sys.exit(main(*sys.argv))

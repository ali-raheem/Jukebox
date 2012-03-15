import serial
import os

def play(filename):
	print "Playing",filename
	os.system("xmms "+filename+"&")
#	os.system("xmms -session 0 -p&")
def parse(code):
	code = code.split('-')[1]
	try:
		code = code.split('\r')[0]
	except IndexError:
		try:
			code = code.split('\n')[0]
		except IndexError:
			print "Probs not a code."
	return dir+code+".pls"

dir = "playlists/"
s = serial.Serial("/dev/ttyACM0", 115200)
s.open()
while 1:
	if(s.inWaiting()):
		code =  s.read(s.inWaiting())
		print "Read code",code,"..."
		filename = parse(code)
		print "Looking for playlist",filename
		try:
			open(filename)
			play(filename)
		except IOError:
			print "Playlist not found!"

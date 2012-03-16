Jukebox
========

Jukebox is designed to take RFID data (or any data via a serial device) using this code it checks a database to find what command to run.

So you may tag a CD case and have jukebox load the album playlist.
Or you may use a barcode scanner and have it update a shopping list when yout ake stuff out of the fridge.

To use this code put a character source in a serial port, default port used is /dev/ttyACM0 alter parse() to handle
your data.

Make sure to escape commands you want run if they have spaces or special chars like !.

##Warning

If used as is this code may be unsafe! Since most people will run jukebox as root to access /dev/tty* devices 
yet anyone can alter the database. solution? add a rule to let your regular user access the device.(recommended)
make the db, jukebox and addtags root writeable only.(bad choice)

##TODO

# Make a nice gui?
# Make code safe
# Fix lastTag thingy

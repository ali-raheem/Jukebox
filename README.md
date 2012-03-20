Jukebox
=

Jukebox is designed to take RFID data (or any data via a serial device) using this code it checks a database to find what command to run.

- So you may tag a CD case and have jukebox load the album playlist.
- Use a barcode scanner and have it update a shopping list when yout ake stuff out of the fridge.
- My favourite, tag a picture and have it load the digital form or album!

To use this code put a character source in a serial port, default port used is /dev/ttyACM0 alter parse() to handle
your data. For example I drop the leading > and following \r my RFID reader sends.

Make sure to escape commands you want run if they have spaces or special chars like '!'.

###How to use

- Make sure to edit the udev rule file for your device to make suitably readable device. This rule file creates a mode 666 /dev/RFIDreader symlink.
- Run edit_db or jukebox to start adding tags to the db. My recommendation
1. Move edit_db and mode it so only root can run it,
2. Make sure db is someplace say /etc/jukebox/db where only root can write to it.
3. Move jukebox somewhere and mode it so only root can write to it but it can be used by anyone
4. run jukebox in background.

####TODO

- Make a script to simplify 'How to use'
- Make a nice gui?
- Fix lastTag thingy


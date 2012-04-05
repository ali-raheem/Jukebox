#!/bin/bash
<<END_GPL>>/dev/null
jukebox - translates serial data to commands.
    Copyright (C) 2012 Ali Raheem

    This program is part of jukebox.

    Jukebox is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Jukebox is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
END_GPL

mkdir /etc/jukebox
cp jukebox /usr/bin/jukebox
cp edit_db /usr/sbin/jukebox_edit_db

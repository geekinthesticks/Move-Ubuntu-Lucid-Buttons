Restoring Window Buttons to Their pre-Lucid Defaults.
=====================================================

There has been a lot of discussion about the default button positions
for windows in Ubuntu Lucid. Personally, I prefer the original
positions, with the buttons on the right hand side of the frame.

There are a number of methods of altering the button positions back to
the old position. Essentially all methods come down to editing a key
in gconf. I intend to install Lucid on a number of computers, some of
which may have multiple accounts. I don't want to be fiddling about
with gconf-editor on each computer and with each account. So I have
written a simple python script that will restore the button position
to their pre Lucid position. Just in case you want to set them back to
the default position for Lucid, the script will do this for you too.

Usage.
======

./move_buttons.py --option

Options:
  -h, --help     show this help message and exit
  -d, --default  Restore Lucid defaults.
  -r, --right    Position window controls to the right.

Licence.
========
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

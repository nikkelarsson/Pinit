#!/bin/bash

# Install pinit on you computer with this script.

# This script compiles, renames and moves the
# binary file to correct location.

# If you wish to change the install location,
# edit 'INSTALLATION'.

INSTALLATION='/usr/local/bin'

# First compile
echo 'Compiling...'
python3 -m nuitka --follow-imports main.py

# Then rename fresh binary to pinit from main.bin
echo 'Renaming from [main.bin] to [pinit]...'
mv main.bin pinit

# Third move/copy binary to good location
printf 'Moving [pinit] to %s...\n' $INSTALLATION
cp pinit $INSTALLATION

# Last do some cleanup
echo 'Doing quick cleanup...'
rm -rf main.build pinit
echo 'All done!'

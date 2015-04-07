#! /bin/bash

cd /Users/nicolas/Sites
echo "Deleting old files in Sites..."
rm -f *

echo "Copying new files from Assignment 4"
cd /Users/nicolas/Copy/School/2014-2015/WINTER\ 2015/COMP\ 206/Assignment\ 4/
cp * /Users/nicolas/Sites
echo "Done."
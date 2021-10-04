#!/bin/bash
HOME=/Users/ryancarter
cd /Users/ryancarter/Documents/Programs/WDOLDII/whatdayoflockdownisit/
/Library/Frameworks/Python.framework/Versions/3.7/bin/python3 update.py $1
git add *
git commit -m "daily update"
git push
echo "It's been pushed 😁"

#!/bin/bash
cd /Users/ryancarter/Documents/Programs/WDOLDII/whatdayoflockdownisit/
/Library/Frameworks/Python.framework/Versions/3.7/bin/python3 update.py
git add *
git commit -m "daily update"
git push

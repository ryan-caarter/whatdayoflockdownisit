#!/bin/bash
cd /Users/ryancarter/Documents/Programs/WDOLDII/whatdayoflockdownisit/
python3 update.py
git add *
git commit -m "daily update"
git push

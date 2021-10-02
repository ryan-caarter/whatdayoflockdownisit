#!/bin/bash
python3 update.py
git add *
git commit -m "daily update"
git push

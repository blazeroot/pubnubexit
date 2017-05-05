#!/usr/bin/env bash
#venv/bin/python3 expubnub.py >> run.txt
python expubnub.py >> run.txt
date >> run.txt
cat run.txt

#!/bin/sh
python3 web/manage.py runserver 192.168.45.123:8000
echo "Started Django web server"
python3 main/main.py
echo "Started main program"
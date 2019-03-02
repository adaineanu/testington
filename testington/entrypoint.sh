#!/bin/sh
python migration/migration.py
cd /app
gunicorn -b 0.0.0.0:8080 wsgi:app

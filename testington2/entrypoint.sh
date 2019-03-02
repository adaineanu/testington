#!/bin/bash
pg_createcluster $PG_MAJOR main
sed -i 's/peer/trust/g' etc/postgresql/11/main/pg_hba.conf
sed -i 's/md5/trust/g' etc/postgresql/11/main/pg_hba.conf
service postgresql start
python3 migration/migration.py
cd /app
gunicorn -b 0.0.0.0:8080 wsgi:app

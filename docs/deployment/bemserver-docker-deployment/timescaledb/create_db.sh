#!/usr/bin/env bash

dbname="bemserver"

echo "=== createdb '$dbname' with user '$POSTGRES_USER' ==="
createdb -U $POSTGRES_USER $dbname

echo "=== create extension ==="
psql -U $POSTGRES_USER -d $dbname -c "CREATE EXTENSION IF NOT EXISTS timescaledb"

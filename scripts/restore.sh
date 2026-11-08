#!/usr/bin/env bash
# Dùng: ./scripts/restore.sh db_backup/file.sql
set -e
source .env
docker compose exec -T db psql -U odoo -d postgres -c "DROP DATABASE IF EXISTS \"$DB_NAME\";" -c "CREATE DATABASE \"$DB_NAME\" OWNER odoo;"
docker compose exec -T db psql -U odoo -d "$DB_NAME" < "$1"
echo "Restore xong."

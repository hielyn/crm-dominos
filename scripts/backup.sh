#!/usr/bin/env bash
# Dùng: ./scripts/backup.sh  -> tạo db_backup/dominos_crm_YYYYMMDD.sql
set -e
source .env
docker compose exec -T db pg_dump -U odoo "$DB_NAME" > "db_backup/${DB_NAME}_$(date +%Y%m%d).sql"
echo "Backup xong."

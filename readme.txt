after runing docker-compose up -d
go into django container and run
python manage.py migrate
then browse localhost:8000/api/item

to add data:
provide word
provide wordtrans
provide category
Post


to check frontend:
localhost:3000

At the moment data entry is only possible through backend localhost:8000/api/item. 

### Database restore ( clean way ) 
First drop the database and restore from backup 
#Enter into postgres
psql -U myuser -d postgres

#Drop database 
psql -U myuser -c "DROP DATABASE mydatabase;"

#Create database 
psql -U myuser -d postgres -c "CREATE DATABASE mydatabase;"

#Now Restore from backup from host
cat ~/pg_backups/db_2026-02-20.sql | docker exec -i nemt-db-1 psql -U myuser -d mydatabase

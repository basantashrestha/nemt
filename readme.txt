Build 
docker compose -f build.yml build



To run: 
docker-compose up -d
then browse localhost:8000/api/item

to add data:
provide word
provide wordtrans
provide category
Post

Check at following add. Multistage build builds frontend and hosts it on nginx
http://localhost

At the moment data entry is only possible through backend localhost:8000/api/item. 

##Database backup script that can be set to cron
docker exec -t nemt-db-1 pg_dump -U myuser mydatabase > ~/pg_backups/db_$(date +\%F).sql

##Restore
cat ~/pg_backups/db_2026-02-20.sql | docker exec -i nemt-db-1 psql -U myuser -d mydatabase


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

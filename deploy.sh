#!/bin/sh
#touch /tmp/backend.txt
rsync -ah --info=progress2 /home/gitlab-runner/builds/UXytDbJa/0/gitlab-instance-4dac5a4a/nemt/nemt_backend/* /var/www/html/nemt/nemt_backend/
rsync -ah --info=progress2 /home/gitlab-runner/builds/UXytDbJa/0/gitlab-instance-4dac5a4a/nemt/reactfrontend/* /var/www/html/nemt/reactfrontend/
rsync -ah --info=progress2 /home/gitlab-runner/builds/UXytDbJa/0/gitlab-instance-4dac5a4a/nemt/docker-compose.yml /var/www/html/nemt/docker-compose.yml
docker-compose -f /var/www/html/nemt/docker-compose.yml down 

docker-compose -f /var/www/html/nemt/docker-compose.yml up -d 



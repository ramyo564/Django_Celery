docker exec -it django /bin/sh
winpty docker exec -it django //bin//sh
ubuntu - > cd /mnt/c

# Build docker
docker-compose up -d --build

python manage.py shell
from celery import group
from cworker.tasks import tp1, tp2, tp3, tp4
task_group = group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
task_group.apply_async()

task_chain = chain(tp1.s(), tp2.s(), tp3.s())
task_chain.apply_async()


# Remove all docker
docker stop $(docker ps -aq) && docker rm $(docker ps -aq) && docker rmi $(docker images -aq)


from dcelery.celery import t1,t2,t3
t2.apply_async(priority=5)
t1.apply_async(priority=6)
t3.apply_async(priority=9)
t2.apply_async(priority=5)
t1.apply_async(priority=6)
t3.apply_async(priority=9)

# Run on Django to inspect task
celery inspect active
celery inspect active_queues

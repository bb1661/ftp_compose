
# Superset
docker volume create superset_vol 
docker run -d -v superset_vol:/app --net=app_net  -p 80:8088 --name superset apache/superset


docker run -d \
-v $PWD/superset_vol/docker:/app/docker \
-v $PWD/superset_vol/superset:/app/superset \
-v $PWD/superset_vol/superset-frontend:/app/superset-frontend \
-v $PWD/superset_vol/superset_home:/app/superset_home \
-v $PWD/superset_vol/tests:/app/tests \
--net=app_net -p 80:8088 --name superset apache/superset

docker exec -it superset superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email admin@superset.com \
              --password admin
docker exec -it superset superset db upgrade
docker exec -it superset superset init
docker exec superset pip install clickhouse-connect  
docker restart superset

# Clickhouse
docker volume create clickhouse_vol
docker run --rm -d \
    --name clickhouse \
    --net=app_net\
    -v clickhouse_vol:/var/lib/clickhouse \
    clickhouse/clickhouse-server

docker run --rm -d \
    --name clickhouse \
    --net=app_net\
    -v clickhouse_vol:/var/lib/clickhouse \
    -p 9000:9000 -p 8123:8123 \
    clickhouse/clickhouse-server

# superset-clickhouse 


clickhousedb://clickhouse:8123
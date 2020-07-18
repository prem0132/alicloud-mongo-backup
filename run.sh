#!/usr/bin/env sh

docker build -t mongo-logical-backup-engine:alpha .

#Stop and remove existing container
docker ps -q -a --filter name=mongo-backup | xargs -r docker stop mongo-backup && docker rm mongo-backup

echo "$(date) $(hostname) starting mongo backup container"

# Run the mongo backup docker container
docker run --name mongo-backup \
  -e ALICLOUD_ACCESS_KEY=$ALICLOUD_ACCESS_KEY \
  -e ALICLOUD_SECRET_KEY=$ALICLOUD_SECRET_KEY \
  -e MongoID=$MongoID \
  -v $(pwd)/mongo.yaml:/app/mongo.yaml \
  -d --restart on-failure mongo-logical-backup-engine:alpha

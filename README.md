# mongo-python-backup

python script to automate backup of alicloud ApsaraDB for mongo

---

## Configuration Options

* Yaml

    You can add your config parameters in [`mongo.yaml`](mongo.yaml)

* Environment Variables

    You can also add your config via env variables

## Config params

* ALICLOUD_ACCESS_KEY
* ALICLOUD_SECRET_KEY
* Region -  Default (ap-southeast-5)
* MongoID
* BackupType - Default (Logical)

## Support

* VMs/docker/K8s

## Example

### OS

1. Populate mongo.yaml
2. Run `pip install -r requirements.txt`
3. Run `python main.py`

### Docker 

1. Run `docker build -t mongo-logical-backup-engine:alpha .`
2. Execute

```
docker run --name mongo-backup \
  -e ALICLOUD_ACCESS_KEY="****************" \
  -e ALICLOUD_SECRET_KEY="****************"" \
  -e MongoID="****************"" \
  -v $(pwd)/mongo.yaml:/app/mongo.yaml \
  -d --restart on-failure mongo-logical-backup-engine:alpha
```

### k8s

1. Populate `k8s/secret.yaml`
2. Push image to your repo and update image and schedule in `k8s/cron-job.yaml`
3. Run `kubectl apply -f k8s/`

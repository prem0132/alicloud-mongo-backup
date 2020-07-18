#!/usr/bin/env python
# coding=utf-8

import yaml
import os
from aliyunsdkcore.client import AcsClient
from aliyunsdkdds.request.v20151201.CreateBackupRequest import CreateBackupRequest

if __name__ == '__main__':
    with open('mongo.yaml') as f:
        my_conf = yaml.safe_load(f)

    client = AcsClient(
        os.environ.get('ALICLOUD_ACCESS_KEY') if os.environ.get(
            'ALICLOUD_ACCESS_KEY') else my_conf['ALICLOUD_ACCESS_KEY'],
        os.environ.get('ALICLOUD_SECRET_KEY') if os.environ.get(
            'ALICLOUD_SECRET_KEY') else my_conf['ALICLOUD_SECRET_KEY'],
        os.environ.get('Region') if os.environ.get(
            'Region') else my_conf['Region']
    )

    request = CreateBackupRequest()
    request.set_accept_format('json')

    request.set_DBInstanceId(
        os.environ.get('MongoID') if os.environ.get('MongoID') else my_conf['MongoID'])
    request.set_BackupMethod(
        os.environ.get('BackupType') if os.environ.get('BackupType') else my_conf['BackupType'])

    response = client.do_action_with_exception(request)
    print(str(response, encoding='utf-8'))
    print("done")

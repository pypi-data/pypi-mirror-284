# -*- coding: utf-8 -*-
# flake8: noqa

from sparkproxy import Auth
from sparkproxy import SparkProxyClient
from sparkproxy.config import SANDBOX_API_HOST
from utils import generate_order_id


supplier_no = 'test0001'
with open("key.pem", 'rb') as pem_file:
    private_key = pem_file.read()

client = SparkProxyClient(Auth(supplier_no=supplier_no, private_key=private_key))   #, host=DEV_API_HOST)

ret, info = client.list_traffic_usages(username="100015", start_time="", end_time="2024-07-08 23:59:59")
print(ret)
print(info)
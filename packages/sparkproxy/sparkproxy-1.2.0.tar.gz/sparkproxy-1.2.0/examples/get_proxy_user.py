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

# 获取订单&实例信息
userId = "100015"
ret, info = client.init_proxy_user(userId, "test")
print(ret)
print(info)

# resi-us.sparkproxy.com:11011:user-qa_sp668220e9aa76e35e6e561a4d-region-fr-sessid-65c70ada3a37:O9SXCvje6O7i
# resi-us.sparkproxy.com:11011:user-qa_sp668220e9aa76e35e6e561a4d-region-us-sessid-0680b7aaa4ba:A2AOMSqvMpBy
# resi-us.sparkproxy.com:11011:qa_sp668220e9aa76e35e6e561a4d:dPVpfYLpz7ho
# curl -x resi-us.sparkproxy.com:11011 -U "user-qa_sp668220e9aa76e35e6e561a4d-region-fr-sessid-65c70ada3a37:dPVpfYLpz7ho" ipinfo.io
# curl -x resi-us.sparkproxy.com:11011 -U "user-qa_sp668220e9aa76e35e6e561a4d-region-us-sessid-0680b7aaa4ba:dPVpfYLpz7ho" ipinfo.io


# ret, info = client.recharge_traffic(req_order_no=generate_order_id(), username=userId, traffic=10000, validity_days=30)
# print(ret)
# print(info)
from django.test import TestCase
from myapp.HB_api.xxt import jiami
import requests,json
# Create your tests here.
s = {
    "requestTm": "20160620190656",
    "jrnNo": "1231231231231",
    "qryCreditId": "12312312",
    "hbUsrNo": "123456",
    "mblNo": "18390525555",
    "usrIdName": "陈斌斌",
    "usrIdCard": "4301324324345342",
    "idCardFront": "",
    "idCardBack": "",
    "zipCode": "412007",
    "addressCode": "071",
    "address": "北京",
    "inCome": "002",
    "usrJob": "004",
    "contactName": "陈智智",
    "contactMblNo": "18873827382",
    "contactRelation": "004",
    "bankCardNo": "3292384298452",
    "bankCardName": "工商",
    "bankMblNo": "18873827382",
    "bankCode": "ICBC",
    "companyName": "个人公司",
    "companyAddress": "北京五环",
    "companyAddressCode": "071",
    "companyMblNo": "18873827382",
    "liveOrgNm": "",
    "liveOrgId": "",
    "liveScore": "",
    "livePicture": "",
    "schooling": "004",
    "appId": "HB",
    "socialIdentity": "001",
    "hbScore": "100",
    "creditTotScore": "100",
    "creditModScore": "100",
    "oprMblNo": "13677777777"}
a=requests.post('http://127.0.0.1:8000/post_api',data=
{'date':jiami(s)})

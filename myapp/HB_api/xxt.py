import hashlib, os,xxtea,binascii, json
from typing import Dict, Any
from urllib import parse


# key =  # Key must be a 16-byte string.
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


def dictPaixu(content):
    lis = {}
    for i in sorted(content):
        lis[i] = content[i]
    return parse.urlencode(lis)


def hxz(content):
    hsh = hashlib.sha1()
    hsh.update(content.encode(encoding='utf-8'))
    return hsh.hexdigest()


def jiami(content):  # xxtex加密
    l = dictPaixu(content)
    jie = json.dumps(content) + hxz(l)
    return xxtea.encrypt(jie,'abcxyz1234567890')


def jiemi(content):  # xxtex解密
    xxt = xxtea.decrypt(content,'abcxyz1234567890')
    mw = str(xxt[-40:], 'utf-8')
    js = json.loads(xxt[:-40])
    dic = dictPaixu(js)
    if mw == hxz(dic):
        return js
    else:
        False


if (__name__ == "__main__"):
    a = jiami(s)

    print(a)

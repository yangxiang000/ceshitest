from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15


# key = RSA.generate(2048)
# # 提取私钥
# private_key=key.export_key()
# file_out=open('private_key.pem','wb')
# file_out.write(private_key)
# # 提取公钥
# public_key=key.publickey().export_key()
# file_out=open('public_key.pem','wb')
# file_out.write(public_key)

def jiem(content):  # 解密
    private_key = open('private_key.pem').read()
    private = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(private)
    return cipher.decrypt(content)


def jiam(content):  # 加密
    public_key = open('public_key.pem').read()
    public = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(public)
    return cipher.encrypt(content)


def qm(content):  # 签名
    private_key = open('private_key.pem').read()
    digest = SHA256.new(content)
    private = RSA.import_key(private_key)
    return pkcs1_15.new(private).sign(digest)


def yq(content, signature):  # 验签
    public_key = open('public_key.pem').read()
    digest = SHA256.new(content)
    public = RSA.import_key(public_key)
    try:
        pkcs1_15.new(public).verify(digest, signature)
        print('签名有效')
    except(ValueError, TypeError):
        print('签名无效')

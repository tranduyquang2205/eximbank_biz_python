import json
import time
import base64
import hashlib
from datetime import datetime, timezone
import websocket
import requests
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
import base64
import random
import uuid
import requests
import json
    
# Your RSA key (Replace with the actual key)
key = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0+B5KsZ/Q4c252WDMHVf4TPtoWwfTiikKu7NGkGaleBWZbDTyql4Cxf6aTMrIyqfYShGCVFWhJgNSmAbqkzvRr9BJVbyTVXppbTbeCKplpFso6IoMBXMizq3P+5VyvS+YFhPrCzDv5iFvMgnmkjlRm3rUZ0Nd22UdIh1Rvb3A/AnnzHR1PEqyYaS4/kzHgwKO0H404QTTA8Js67pA/WC4Bv/6fnE/GXMwsoWzZXwPeofSBkXFNsj2nrXROUfDzUmUQaMZT4monOt1ihzyRiF7+yHk6jmtFNU8KgrX2rnkqtpSCl524zFR9fztZplq2VqvpuefQNuBy3y5Ss1EnY24wIDAQAB\n-----END PUBLIC KEY-----"
def get_key_site():
    url = "https://onlinebanking.eximbank.com.vn/api/IB/KHDN/security/getPermission"

    payload = json.dumps({})
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://onlinebanking.eximbank.com.vn',
    'Referer': 'https://onlinebanking.eximbank.com.vn/KHDN/account/login-corp?returnUrl=%2Fhome',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    'X-Token': '',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
def Ht(data):
    # Load the RSA key from the key string (in PEM format)
    key = f"-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmlqEStU8FviItSFGyZpNOS9HlNMIk5KG3BT5UWvAwyoAbbhfZZxXeCsVyC2t2+KM68O3+0L28XrsCowG1E/10thCkY+TCm9dlmAwHpjB+W1TQcoNnqydqVhWRBaHKoBmxd0fSsno1fJ6eYioi3S3Vrb0332GML5wq4zZ0u0jAh6uaMwcHfb5vk3+W5UnjTSk3WXUOq/fvinBvxNapcBEgFuChhhGZfKeS4Xu9cSreO24Dxdls2ReuyaXg58oACktjtQX/JopMMBKuRMc357f0gDMr2bPu1qrxoyKPqayTfcTOf8/1tI/b8Xhs21CG2T/Z1o981GGHcW6pNlvRhp/gQIDAQAB\n-----END PUBLIC KEY-----"
    rsa_key = RSA.import_key(key)

    # Encrypt the message using PKCS1 padding
    cipher = PKCS1_v1_5.new(rsa_key)

    ciphertext = cipher.encrypt(data.encode('utf-8'))

    # Encode the ciphertext as base64
    return base64.b64encode(ciphertext).decode('utf-8')
data = {
    "userId": "121650448",
    "passWord": "Khanh675@",
    "userType": "O",
    "captcha": None
}
i = {
    "applicationVersion": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    "deviceId": uuid.uuid4().hex,
    "platformOS": "Win32"
}
data = (Ht(json.dumps(data), key))


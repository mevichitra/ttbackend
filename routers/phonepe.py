import hashlib

import constants
import requests
import base64
import uuid
import json

def create_sha256_string(input_string):
    sha256_hash = hashlib.sha256(input_string.encode())
    encoded_string = sha256_hash.hexdigest()
    return encoded_string

def string_to_base64(input_string):
    encoded_string = base64.b64encode(input_string.encode())
    return encoded_string.decode()

def phonepePaymentURL(amount: int):

    orderID = "pp-"+str(uuid.uuid4())
    userID = "user-"+str(uuid.uuid4())
    merchantTransactionID = "MT"+str(uuid.uuid4())
    mobileNumber = "9999999998" # test mobile number
    email = "test@gmai.com"

    payload = {
        "amount": amount*100,
        "merchantId": constants.merchant_id,
        "merchantTransactionId": merchantTransactionID,
        "merchantUserId": userID,
        "redirectUrl": constants.webhook_url,
        "redirectMode": "POST",
        "callbackUrl": constants.webhook_url,
        "merchantOrderId": orderID,
        "mobileNumber": mobileNumber,
        "email": email,
        "message": "Payment for " + orderID,
        "paymentInstrument": {
            "type": "PAY_PAGE"
        }
    }
    json_data = json.dumps(payload)
    base64_request = string_to_base64(json_data)

    # X-VERIFY header -- SHA256(Base64 encoded payload + “/pg/v1/pay” + salt key) + ### + salt index
    finalXHeader = create_sha256_string(base64_request + "/pg/v1/pay" + constants.salt_key)+"###"+constants.salt_index

    req = {
        "request": base64_request
    }

    finalHeader = {
        "Content-Type": "application/json",
        "X-VERIFY": finalXHeader
        }

    response = requests.post(constants.payment_url, headers=finalHeader, json=req)
    if response.status_code == 200:
        return response.json()
    else:
        return "Something went wrong - " + response.text


res = phonepePaymentURL(100)

"""
SAMPLE RESPONSE
{'code': 'PAYMENT_INITIATED',
 'data': {'instrumentResponse': {'redirectInfo': {'method': 'GET',
                                                  'url': 'https://mercury-uat.phonepe.com/transact/simulator?token=1Ugbh6DMsGDPSl498ym6zhFQMg7Cm1VxrGE0SNANDWQUQXLMiVLI9ZdJoFAuOxvoqqTd2sqI'},
                                 'type': 'PAY_PAGE'},
          'merchantId': 'PGTESTPAYUAT86',
          'merchantTransactionId': 'MT3b415736-839f-446e-b30b-659b84a95337'},
 'message': 'Payment initiated',
 'success': True}
"""

# Directly access the data from the response dictionary
paymentURL = res.get("data", {}).get("instrumentResponse", {}).get("redirectInfo", {}).get("url", None)
transactionID = res.get("data", {}).get("merchantTransactionId", None)
print("transaction_id - ", transactionID)
print("payment_url - ", paymentURL)
print()
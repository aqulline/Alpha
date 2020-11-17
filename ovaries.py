import requests
import datetime
import base64 
  
from requests.auth import HTTPBasicAuth
 
            # consants 
BusinessShortCode = "174379"

PartyA = "255766354079"

lipa_na_mpesa_passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"

consumer_key = "RxokHb0vjJgHBJ9RRmN2Bfewjm6HqkfA"

consumer_secretes = "bQMGAHRaVtAE5yaK"

    # G E N E R A T O R S

def access_token_generator():
    mpesa_auth_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    data = (requests.get(mpesa_auth_url, auth = HTTPBasicAuth(consumer_key, consumer_secretes))).json()

    #print(data)
    access_token = data["access_token"]
    expire_date = data["expires_in"]
    return access_token



def Time_generator():
    unformatedtimekey = datetime.datetime.now()

    formatmatedtimekey = unformatedtimekey.strftime("%Y%m%d%H%M%S")

    return formatmatedtimekey

def Password_generator():
    password_to_encode = BusinessShortCode + lipa_na_mpesa_passkey + Time_generator()

    encoded_password = base64.b64encode(password_to_encode.encode())

    decoded_password = encoded_password.decode("utf-8")

    actual_password = decoded_password

    return actual_password

def lipa_na_mpesa():
    access_token = access_token_generator()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": BusinessShortCode,
        "Password": Password_generator(),
        "Timestamp": Time_generator(),
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "200",
        "PartyA": PartyA,
        "PartyB": BusinessShortCode,
        "PhoneNumber": PartyA,
        "CallBackURL": "https://fullstackdjango.com/callback/",
        "AccountReference": "1234567 ",
        "TransactionDesc": "buy maharagwe "
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

lipa_na_mpesa()


import requests
from requests.auth import HTTPBasicAuth
#import request
import responses
import json
#mpesa details
consumer_key = "RxokHb0vjJgHBJ9RRmN2Bfewjm6HqkfA"

consumer_secretes = "bQMGAHRaVtAE5yaK"
base_url = "http://197.250.101.167:891/"
def access_token_generator():
    mpesa_auth_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    data = (requests.get(mpesa_auth_url, auth = HTTPBasicAuth(consumer_key, consumer_secretes))).json()

    #print(data)
    access_token = data["access_token"]
    expire_date = data["expires_in"]
    return access_token
def register():
    mpesa_endpoint = "http://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token_generator()}
    req_body = {
            "Shortcode":"174379",
            "ResponseType":"Completed",
            "ConfirmationUrl":base_url + "/c2b/confirm",
            "ValidationUrl":base_url + "/c2b/validation"
        }
    response_data = requests.post(
        mpesa_endpoint,
        json=req_body,
        headers = headers
    )
    confirm()
    validation()
    return response_data.json()

def confirm():
    data = request.get_json()
    

    file = open("confirm.json", "a")
    file.write(data)
    file.close()

def validation():
    data = request.get_json()

    file = open("confirm.json", "a")
    file.write(data)
    file.close()


print(register())

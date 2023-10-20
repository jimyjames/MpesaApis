from flask import Flask,jsonify
import requests
from requests.auth import HTTPBasicAuth

app= Flask(__name__)
consumer_key='bj8hSqf4w8EE1UgK2R1UUowK8RHqhkyA'
consumer_secret='RikqRXfoIaO5YyLE'


@app.route('/accesstoken')
def access_token():
    data=get_access_token()
    return data







def get_access_token():
    mpesa_auth_url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    data=(requests.get(mpesa_auth_url, auth=HTTPBasicAuth(consumer_key,consumer_secret))).json()  
    return data['access_token']

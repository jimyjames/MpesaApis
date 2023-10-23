from flask import Flask,request
import requests 
from requests.auth import HTTPBasicAuth
import datetime,hashlib,base64

app= Flask(__name__)
consumer_key='bj8hSqf4w8EE1UgK2R1UUowK8RHqhkyA'
consumer_secret='RikqRXfoIaO5YyLE'

# route to handle getting the access token
@app.route('/accesstoken')
def access_token():
    data=get_access_token()
    return data


confirmationurl="172.16.54.166"
validationurl="172.16.54.166"

# route to handle registering urls
@app.route('/registerurl')
def reg_url():
    mpesa_endpoint="https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers={"Authorization":"Bearer %s" % get_access_token()}
    request_body={
        "ShortCode":"174379",
        "ResponseType":"completed",
        "ConfirmationURL": "https://peternjeru.co.ke/safdaraja/api/confirmation.php",
        "ValidationURL": "https://peternjeru.co.ke/safdaraja/api/validation.php"
    }
    response_data=requests.post(
        mpesa_endpoint, json=request_body,headers=headers
    )

    return response_data.json()





def get_access_token():
    mpesa_auth_url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    data=(requests.get(mpesa_auth_url, auth=HTTPBasicAuth(consumer_key,consumer_secret))).json() 
    shortcode=174349
    shortcodes="174349"

    LNM_Passkey="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    Time=datetime.datetime.now()
    tme="20160216165627"
    Timestamp=Time.strftime("%Y%m%d%H%M%S")
    password1=shortcodes+LNM_Passkey+Timestamp
    phonenumber="254769947593"
    password2=base64.b64encode(password1.encode()).decode()
 

    print(password2)
    print(Timestamp)
   
    return data['access_token']



@app.route('/c2b/confirm')
def confirm():
    data=request.get_json()
    file=open('confirm.json','a')
    file.write(data)
    file.close()


    
@app.route('/c2b/validation')
def validate():
    data=request.get_json()
    file=open('validate.json','a')
    file.write(data)
    file.close()


@app.route('/stkpush')
def stkpush():
    stkpush_url='https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    headers={
        "Authorization":"Bearer %s" % get_access_token()
    }
    shortcode=174379
    shortcodes="174379"

    LNM_Passkey="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    Time=datetime.datetime.now()
    tme="20160216165627"
    Timestamp=Time.strftime("%Y%m%d%H%M%S")
    password1="174379"+LNM_Passkey+Timestamp
    phonenumber="254769947593"
    password2=base64.b64encode(password1.encode('utf-8')).decode('utf-8')
    # password="MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTYwMjE2MTY1NjI3"
    password="MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjMxMDIzMTk0NTIw",
    

    request_body = {
    "BusinessShortCode":shortcodes,
    "Password": password2,
    "Timestamp": Timestamp,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 1,
    "PartyA": phonenumber,
    "PartyB": shortcodes,
    "PhoneNumber": phonenumber,
    "CallBackURL": "https://mydomain.com/path",
    "AccountReference": "CompanyXLTD",
    "TransactionDesc": "Payment of X" 
  }
    print(request_body)
    print(password)
    print(password1)
    print(password2)
    print(Timestamp)
    print(headers)
    response_data=requests.post(
       stkpush_url, json=request_body,headers=headers
    )

    return response_data.json()


@app.route('/callbackurl', methods=['POST'])
def callback():

        request_data = request.get_json()

        return request_data({})
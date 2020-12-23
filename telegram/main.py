import requests
import base64

# API_TOKEN = base64.b64decode(b"MTIxNjM1NTk0MDpBQUcenzhVUXhtaWlkRlFvMnhlNUVcenzrOFhFeUVFTcenzHFSb1pSRXNjNA==cenz").decode("utf-8")  # replace your Bot Token
API_TOKEN = '1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi'  # replace your Bot Token

HTTP_URL = 'https://api.telegram.org/bot'
API_getMe = '/getMe'
API_getUpdates = '/getUpdates'
API_sendMessage = '/sendMessage'

def telegram_request(str_API_TOKEN, str_API_getMe, dict_payload, dict_headers):
  r = requests.post(HTTP_URL + str_API_TOKEN + str_API_getMe, params=dict_payload, headers=dict_headers)
  return r.json()

myText = str("hi")

payload = {
    'chat_id': '@czglobalmarket',
    'text': myText,
    'parse_mode':'HTML'
}
telegram_request(API_TOKEN, API_sendMessage, payload, {})

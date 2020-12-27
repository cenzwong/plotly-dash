# https://core.telegram.org/bots/api

import requests
import base64

# API_TOKEN = base64.b64decode(b"MTIxNjM1NTk0MDpBQUcenzhVUXhtaWlkRlFvMnhlNUVcenzrOFhFeUVFTcenzHFSb1pSRXNjNA==cenz").decode("utf-8")  # replace your Bot Token
API_TOKEN = '1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi'  # replace your Bot Token

HTTP_URL = 'https://api.telegram.org/bot'
API_getMe = '/getMe'
API_getUpdates = '/getUpdates'
API_sendMessage = '/sendMessage'
API_sendPhoto = '/sendPhoto' # https://core.telegram.org/bots/api#sendphoto

newLine = str("\r\n")

def telegram_request(str_API_TOKEN, str_API_getMe, dict_payload, dict_headers):
  r = requests.post(HTTP_URL + str_API_TOKEN + str_API_getMe, params=dict_payload, headers=dict_headers)
  return r.json()

def telegram_sendPhotofromFile(str_API_TOKEN, str_API_getMe, dict_payload, dict_headers, str_path):
  photo = {'photo': open(str_path, 'rb')}
  r = requests.post(HTTP_URL + str_API_TOKEN + str_API_getMe, params=dict_payload, files=photo)
  return r.json()


# Example
## Code for sending Texy
myText = str("ThisText")+ newLine + str("ThatText")
payload = {
    'chat_id': '@djrbownfosnsoxnoenwofjronsowndo',
    'text': myText,
    'parse_mode':'HTML'
}
telegram_request(API_TOKEN, API_sendMessage, payload, {})
## Code for sending url photo
payload = {
    'chat_id': '@djrbownfosnsoxnoenwofjronsowndo',
    'photo': "https://api.time.com/wp-content/uploads/2019/08/better-smartphone-photos.jpg",
    # 'parse_mode':'HTML'
}
telegram_request(API_TOKEN, API_sendPhoto, payload, {})
## Code for sending local photo
fig.savefig("myFile.jpg")
payload = {
    'chat_id': '@djrbownfosnsoxnoenwofjronsowndo',
}
telegram_sendPhotofromFile(API_TOKEN, API_sendPhoto, payload, {}, "myFile.jpg")

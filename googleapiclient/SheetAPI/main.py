# !pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def getNewSheetID(creds, sheetTitle):
    service = build('sheets', 'v4', credentials=creds)
    spreadsheet = {
        'properties': {
            'title': sheetTitle
        }
    }
    spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                        fields='spreadsheetId').execute()
    print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))
    return spreadsheet.get('spreadsheetId')
    
def getSheetdata(creds, SheetID, SheetRange):
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SheetID,
                                range=SheetRange).execute()
    values = result.get('values', [])
    return values
    
def updateSheetData(creds, SheetID, SheetRange, values):
    body = {
        'values': values
    }
    value_input_option = 'USER_ENTERED' # 'RAW'
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption=value_input_option, body=body).execute()
    return result.get('updatedCells')
    
def appendSheetData(creds, SheetID, SheetRange, values):
    body = {
        'values': values
    }
    result = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption=value_input_option, body=body).execute()
    print('{0} cells appended.'.format(result \
                                           .get('updates') \
                                           .get('updatedCells')))
    return result.get('updates').get('updatedCells')    
    
# ========================
 # If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def getCred():
    global creds
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials1.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds
    
    
creds = None
creds = getCred()

spreadsheet_id = "1Z-e0Yhym0PwQHIMn3_VAyN_idqsOQ01f3gKipKjp7JwCENZ"
range_name = "Sheet1!A1:C"

data = getSheetdata(creds, spreadsheet_id, range_name)
data

appendSheetData(creds, spreadsheet_id, range_name, values)

getNewSheetID(creds, "SheetTest")
    
    
    

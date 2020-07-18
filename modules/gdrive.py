# from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
from datetime import datetime
from tzlocal import get_localzone

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']
tz = get_localzone()

#pickle_path = 'gdrive-creds/token.pickle'
#cred_path = 'gdrive-creds/credentials.json'


def backup_to_drive():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('gdrive-creds/token.pickle'):
        with open('gdrive-creds/token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('gdrive-creds/credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('gdrive-creds/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    today = datetime.now(tz).strftime("%I:%M%p on %B %d, %Y")
    file_name = ''.join(e for e in today if e.isalnum())

    file_metadata = {'name': file_name + '.jpg', 'parents': ['1RmyvXwRubdu8m8VzvUK1clAgNSRM1Clv']}

    media = MediaFileUpload(os.path.abspath("last_captured_image.jpg"), mimetype='image/jpeg')
    service.files().create(body=file_metadata, media_body=media, fields='id').execute()

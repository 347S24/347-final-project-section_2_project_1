import os
import pandas as pd
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import webbrowser
scopes=['https://www.googleapis.com/auth/photoslibrary.appendonly']
# url = "https://www.google.com"

# chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))

# webbrowser.get("chrome").open_new(url)

creds = None

if os.path.exists('_secrets_/token.json'):
    creds = Credentials.from_authorized_user_file('_secrets_/token.json', scopes)
        
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            '_secrets_/client_secret.json', scopes)
        creds = flow.run_local_server()
    print(creds)
    # Save the credentials for the next run
    with open('_secrets_/token.json', 'w') as token:
        token.write(creds.to_json())

from google.auth.transport.requests import AuthorizedSession
authed_session = AuthorizedSession(creds)

# read image from file
with open("images/Baby_duck_in_diaper.jpg", "rb") as f:
    image_contents = f.read()

# upload photo and get upload token
response = authed_session.post(
    "https://photoslibrary.googleapis.com/v1/uploads", 
    headers={},
    data=image_contents)
upload_token = response.text

# use batch create to add photo and description
response = authed_session.post(
        'https://photoslibrary.googleapis.com/v1/mediaItems:batchCreate', 
        headers = { 'content-type': 'application/json' },
        json={
            "newMediaItems": [{
                "description": "Test photo",
                "simpleMediaItem": {
                    "uploadToken": upload_token,
                    "fileName": "test.jpg"
                }
            }]
        }
)
print(response.text)
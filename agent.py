# agent.py
import os
print("🛠 Current working directory:", os.getcwd())

from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to the downloaded credentials file
SERVICE_ACCOUNT_FILE = "credentials.json"
SCOPES = ["https://www.googleapis.com/auth/calendar"]
CALENDAR_ID = "primary"  # or your calendar ID

# Authenticate
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build("calendar", "v3", credentials=creds)

def run_agent_logic(user_input: str) -> str:
    # Simple logic to book "tomorrow at 3 PM"
    if "tomorrow" in user_input.lower():
        start_time = datetime.now() + timedelta(days=1)
        start_time = start_time.replace(hour=15, minute=0, second=0, microsecond=0)
        end_time = start_time + timedelta(minutes=30)

        event = {
            "summary": "TailorTalk Appointment",
            "description": "Scheduled via conversational AI",
            "start": {"dateTime": start_time.isoformat(), "timeZone": "Asia/Kolkata"},
            "end": {"dateTime": end_time.isoformat(), "timeZone": "Asia/Kolkata"},
        }

        try:
            service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
            return f"✅ Booked your meeting for tomorrow at 3 PM!"
        except Exception as e:
            return f"❌ Failed to book meeting: {e}"

    return "Please mention a date like 'tomorrow' or 'next Friday'."

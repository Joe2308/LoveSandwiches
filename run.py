import gspread
google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credential.from_service_account_file("creds.json")
SCOPED_CREDS = creds.with scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")
sales = SHEET.worksheet("sales")
data = sales.get_all_values()
print(data)
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from options import RESULTS_SHEET_NAME, SPREADSHEET_NAME, QUESTIONS_SHEET_NAME, HEADER, NUM_OF_QUESTIONS

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "creds.json", scope)
client = gspread.authorize(creds)
spreadsheet = client.open(SPREADSHEET_NAME)


def add_results(insertRow):
    # Open the spreadhseet
    sheet = spreadsheet.worksheet(RESULTS_SHEET_NAME)

    # data = sheet.get_all_records()  # Get a list of all records

    # row = sheet.row_values(3)  sheet.col_values(1) # Get a specific row
    # cell = sheet.cell(1,2).value  # Get the value of a specific cell
    # Insert the list as a row at index 2 to account for header
    sheet.insert_row(insertRow, index=2)
    # sheet.update_cell(2,2, "CHANGED")  # Update one cell

    # numRows = sheet.row_count  # Get the number of rows in the sheet


def get_info():
    sheet = spreadsheet.worksheet(QUESTIONS_SHEET_NAME)
    data = sheet.get_all_records()
    return data

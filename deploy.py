from flask import Flask, request, jsonify
from os import getenv
from pprint import pprint
from datetime import datetime
from config import NUM_OF_QUESTIONS, HEADER, RESULTS_SHEET_NAME, SPREADSHEET_NAME, HEADER, NUM_OF_QUESTIONS, USER_EMAIL
from flask_cors import cross_origin
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# SET UP FLASK APP
app = Flask(__name__)

# API Routes
@app.route('/', methods=['POST'])
@cross_origin(['http://localhost:8080/', getenv('APP_HOST_ONE', None), getenv('APP_HOST_TWO', None)])
def update_results():
    results = []

    params = request.json
    for i in range(NUM_OF_QUESTIONS):
        key = 'q' + str(i + HEADER)
        results.append(params.get(key, None))
    results.append(params.get('result', None))

    now = datetime.now()
    dt_string = now.strftime("%Y%m%d %H:%M:%S")
    results.append(dt_string)

    # print(results)
    add_results(results)
    return 'Success'


@app.route('/', methods=['GET'])
def index():
    return ''


# GOOGLE SHEETS API
with app.app_context():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    # Get environment variables
    creds_json = {
        "type": getenv('type'),
        "project_id": getenv('project_id'),
        "private_key_id": getenv('private_key_id'),
        "private_key": getenv('private_key').replace('\\n', '\n'),
        "client_email": getenv('client_email'),
        "client_id": getenv('client_id'),
        "auth_uri": getenv('auth_uri'),
        "token_uri": getenv('token_uri'),
        "auth_provider_x509_cert_url": getenv('auth_provider_x509_cert_url'),
        "client_x509_cert_url": getenv('client_x509_cert_url')
    }
    creds = ServiceAccountCredentials.from_json_keyfile_dict(
        keyfile_dict=creds_json, scopes=scope)
    client = gspread.authorize(creds)
    try:
        spreadsheet = client.open(SPREADSHEET_NAME)
    except:
        client.create(SPREADSHEET_NAME)
        spreadsheet = client.open(SPREADSHEET_NAME)
        client.insert_permission(spreadsheet.id, USER_EMAIL, perm_type='user', role='owner')
    print("spreadsheet id: {}".format(spreadsheet.id))
    print("find spreadsheet at: https://docs.google.com/spreadsheets/d/{}".format(spreadsheet.id))

    def add_results(insertRow):
        sheet = spreadsheet.worksheet(RESULTS_SHEET_NAME)
        sheet.insert_row(insertRow, index=2)

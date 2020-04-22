from flask import Flask, request, jsonify
from sheets import add_results, get_info
from os import getenv
from pprint import pprint
from datetime import datetime
from options import NUM_OF_QUESTIONS, HEADER

app = Flask(__name__)

@app.route('/', methods=['POST'])
# @cross_origin(['http://127.0.0.1:5000/', getenv('LOCAL_HOST', None), getenv('APP_HOST', None)])
def update_results():
    results = []

    params = request.form
    for i in range(NUM_OF_QUESTIONS):
        key = 'q' + str(i + HEADER)
        results.append(params.get(key, None))

    now = datetime.now()
    dt_string = now.strftime("%Y%m%d %H:%M:%S")
    results.append(dt_string)

    print(results)
    add_results(results)
    return 'Success'

@app.route('/', methods=['GET'])
def get_questions():
    return jsonify(get_info())

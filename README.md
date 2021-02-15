# API Endpoint for Google Sheets

## Description

Collects quiz results from the [Circuit Breaker Personality Quiz](https://circuit-breaker-personality.herokuapp.com/) and stores them in Google Sheets.

To be set up together with the quiz site ([code](https://github.com/huishun98/trivia-quiz-client.git)).

## Language, Frameworks and Libraries

Built using Flask. Uses Google Sheets API.

## Running locally

1. Enable Google Sheets API at [Google Cloud Platform](https://developers.google.com/sheets/api/quickstart/js), create a [service account](https://cloud.google.com/iam/docs/creating-managing-service-account-keys), and make the following into environmental variables: 
- type 
- project_id
- private_key_id
- private_key
- client_email
- client_id
- auth_uri
- token_uri
- auth_provider_x509_cert_url 
- client_x509_cert_url

If origin(s) is/are not http://localhost:8080/, make host(s) into environment variable(s) as APP_HOST_ONE and/or APP_HOST_TWO.

2. Update config file (config.py) based on preferences.

3. Create a virtual environment and install required packages by running:
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Run the following code:
```
export FLASK_APP=deploy.py
python -m flask run
```

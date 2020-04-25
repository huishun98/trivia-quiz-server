# API Endpoint for Google Sheets

## Description

Collects quiz results from the Circuit Breaker Personality Quiz (https://circuit-breaker-personality.herokuapp.com/) and stores them in Google Sheets.

The live version can be found here: https://circuit-breaker-quiz.herokuapp.com/


## Language, Frameworks and Libraries

Built using Flask. Uses Google Sheets API.

## Running locally

1. Retrieve from Google Cloud Platform make the following into environmental variables: 
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

2. Run the following code:
```
export FLASK_APP=deploy.py
python -m flask run
```

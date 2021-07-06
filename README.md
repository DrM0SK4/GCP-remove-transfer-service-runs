# GCP-remove-transfer-service-runs
A script to programmatically remove GCP transfer service run using python 3.x

If you don't have python:
0) follow the steps to install python https://cloud.google.com/python/docs/setup#installing_python
1) activate venv to run the script in an isolated environment https://cloud.google.com/python/docs/setup#installing_and_using_virtualenv
2) install google-cloud-bigquery-datatransfer by running "pip install --upgrade google-cloud-bigquery-datatransfer"
3) install google-auth-oauthlib by running "pip install --upgrade google-auth-oauthlib"
4) inspect the main.py file and make sure to fill in
  - PROJECT_ID = "YOUR_PROJECT_ID"
  - LOCATION_ID = "YOUR_LOCATION_ID"
  - CONFIG_ID = "YOUR_TRANSFER_CONFIG_ID"
5) fill account_servicet_keys_path with the pat of your account service keys to authenticate as a service account OR
   fill client_secret_path with the path of your client secret if you want to authenticate as end user
6) pass a integer to the TransferState to delete all the transfer runs that have that state (i.e 5 = FAILED, 4 = SUCCEEDED ...)
7) run "py .\main.py"
    

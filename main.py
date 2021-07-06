from module.auth import get_credentials, get_client,set_account_service_credentials
from module.transfer_run import get_transfer_run
from classes.TransferState import TransferState

# the location of your client_secret_path to authenticate as end user
client_secret_path = ""
# the location of your caccount_servicet_keys_path to authenticate as a service account 
account_servicet_keys_path =""

# Set use_account_service_auth to False if you want to authenticate as an end user
# https://cloud.google.com/docs/authentication/end-user
# Set use_account_service_auth to True if you want to authenticate as a service account 
# https://cloud.google.com/docs/authentication/production#auth-cloud-implicit-python

use_account_service_auth = True

credentials = None

if use_account_service_auth:
    if account_servicet_keys_path:
        set_account_service_credentials(account_servicet_keys_path)
else:
    if client_secret_path:
        credentials = get_credentials(client_secret_path)

client = get_client(credentials)

PROJECT_ID = "YOUR_PROJECT_ID"
LOCATION_ID = "YOUR_LOCATION_ID"
CONFIG_ID = "YOUR_TRANSFER_CONFIG_ID"

parent = f"projects/{PROJECT_ID}/locations/{LOCATION_ID}/transferConfigs/{CONFIG_ID}"


result = get_transfer_run(str(TransferState(5)), client, parent)

print(f'{result[1]} out of {result[0]} were deleted')

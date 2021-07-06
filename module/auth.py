import os
from google_auth_oauthlib import flow
from google.cloud import bigquery_datatransfer_v1


def set_account_service_credentials(path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path

# TODO: Uncomment the line below to set the `launch_browser` variable.
# launch_browser = True
#
# The `launch_browser` boolean variable indicates if a local server is used
# as the callback URL in the auth flow. A value of `True` is recommended,
# but a local server does not work if accessing the application remotely,
# such as over SSH or from a remote Jupyter notebook.

def get_credentials(client_secret_path, launch_browser=True):

    appflow = flow.InstalledAppFlow.from_client_secrets_file(
        client_secret_path, scopes=["https://www.googleapis.com/auth/bigquery"]
    )

    if launch_browser:
        appflow.run_local_server()
    else:
        appflow.run_console()

    credentials = appflow.credentials

    return credentials


# we need the credentials to authenticate as end user
# if credentials is None, then we assume that the program is using Service Account Authentication
def get_client(credentials):
    if credentials:
        client = bigquery_datatransfer_v1.DataTransferServiceClient(
        credentials=credentials)
    else:
        client = bigquery_datatransfer_v1.DataTransferServiceClient()
    return client

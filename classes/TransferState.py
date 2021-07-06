from enum import Enum

# https://cloud.google.com/bigquery-transfer/docs/reference/datatransfer/rest/v1/TransferState
class TransferState(Enum):
    TRANSFER_STATE_UNSPECIFIED = 0
    PENDING = 2
    RUNNING = 3
    SUCCEEDED = 4
    FAILED = 5
    CANCELLED = 6

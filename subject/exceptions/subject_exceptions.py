import logging
from typing import Optional

from auth_api.auth_exceptions.base_exception import AUTHBaseException


class SubjectNotFoundError(AUTHBaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "This subject is not listed."
        else:
            super().__init__(msg)
        logging.error(self.msg)


class PermissionDeniedError(AUTHBaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "This user is not permitted to perform this action."
        else:
            super().__init__(msg)
        logging.error(self.msg)

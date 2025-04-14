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


class NotAllowedEditSubjectError(AUTHBaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "You are not allowed to edit this subject."
        else:
            super().__init__(msg)
        logging.error(self.msg)

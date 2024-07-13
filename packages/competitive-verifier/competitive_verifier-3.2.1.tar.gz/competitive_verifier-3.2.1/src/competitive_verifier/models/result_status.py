from enum import Enum


class ResultStatus(str, Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    SKIPPED = "skipped"

    @property
    def status(self) -> "ResultStatus":
        return self

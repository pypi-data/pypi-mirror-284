from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional


@dataclass
class ErrorResponse:
    code: str
    message: str


class PredefinedErrorCodes(Enum):
    VAL_ERR = "VAL_ERR"
    NOT_FND = "NOT_FND"
    INT_ERR = "INT_ERR"
    PER_DEN = "PER_DEN"
    AUTH_ERR = "AUTH_ERR"
    TIMEOUT = "TIMEOUT"
    INV_REQ = "INV_REQ"


class ErrorResponseConfig:
    _errors: Dict[str, ErrorResponse] = {
        PredefinedErrorCodes.VAL_ERR.value: ErrorResponse(PredefinedErrorCodes.VAL_ERR.value, "Validation failed."),
        PredefinedErrorCodes.NOT_FND.value: ErrorResponse(PredefinedErrorCodes.NOT_FND.value, "Resource not found."),
        PredefinedErrorCodes.INT_ERR.value: ErrorResponse(PredefinedErrorCodes.INT_ERR.value, "Internal server error."),
        PredefinedErrorCodes.PER_DEN.value: ErrorResponse(PredefinedErrorCodes.PER_DEN.value, "Permission denied."),
        PredefinedErrorCodes.AUTH_ERR.value: ErrorResponse(PredefinedErrorCodes.AUTH_ERR.value,
                                                           "Authentication error."),
        PredefinedErrorCodes.TIMEOUT.value: ErrorResponse(PredefinedErrorCodes.TIMEOUT.value, "Request timed out."),
        PredefinedErrorCodes.INV_REQ.value: ErrorResponse(PredefinedErrorCodes.INV_REQ.value, "Invalid request.")
    }

    @classmethod
    def add_custom_error(cls, code: str, message: str):
        cls._errors[code] = ErrorResponse(code, message)

    @classmethod
    def add_custom_errors(cls, errors: Dict[str, str]):
        for code, message in errors.items():
            cls.add_custom_error(code, message)

    @classmethod
    def get_error(cls, code: str) -> Optional[ErrorResponse]:
        return cls._errors.get(code)

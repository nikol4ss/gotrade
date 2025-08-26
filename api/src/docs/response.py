from typing import Dict, Any, Union

ERROR_RESPONSES: Dict[Union[int, str], Dict[str, Any]] = {
    400: {
        "description": "Bad Request – invalid parameters or missing data",
        "content": {
            "application/json": {
                "example": {"detail": "Validation error or invalid request"}
            }
        },
    },
    404: {
        "description": "Not Found – resource not found",
        "content": {
            "application/json": {"example": {"detail": "Requested resource not found"}}
        },
    },
    500: {
        "description": "Internal Server Error – something went wrong on the server",
        "content": {
            "application/json": {
                "example": {"detail": "Internal error while processing data"}
            }
        },
    },
}

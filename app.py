"""
Fastapi `ASGI` application
"""
from fastapi import FastAPI
from fastapi.exceptions import ResponseValidationError, HTTPException
from fastapi.responses import JSONResponse

from api.router import api_router
from utils.weather import RESTError

app = FastAPI(title="Track and Trace API")

app.include_router(api_router, prefix="/api")


@app.exception_handler(RESTError)
async def rest_error_handler(_, exc: RESTError):
    return JSONResponse(
        status_code=exc.status_code, content={"detail": exc.detail}
    )


@app.exception_handler(HTTPException)
async def http_error_handler(_, exc: HTTPException):
    if isinstance(exc.detail, str):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": [{"msg": exc.detail}]},
        )
    return JSONResponse(
        status_code=exc.status_code, content={"detail": exc.detail}
    )


@app.exception_handler(ResponseValidationError)
async def resp_validation_error_handler(_, exc: ResponseValidationError):
    return JSONResponse(
        status_code=500, content={"detail": exc.errors()}
    )

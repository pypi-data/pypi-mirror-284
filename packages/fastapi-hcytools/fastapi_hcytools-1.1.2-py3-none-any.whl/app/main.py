import logging
import os
import time
import json
import yaml

from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from fastapi.logger import logger as fastapi_logger

from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.concurrency import iterate_in_threadpool

from app.router.sample_router import router as ioctl_router
from app.comm.utils import *

app = FastAPI(
	swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)

logger = logging.getLogger("gunicorn.access")
fastapi_logger.handlers = logger.handlers
fastapi_logger.setLevel(logger.level)

app.include_router(ioctl_router)

@app.middleware("http")
async def log_requests(request: Request, call_next):
	start_time = time.time()

	response = await call_next(request)

	process_time = (time.time() - start_time) #* 1000
	formatted_process_time = '{0:.4f}'.format(process_time)

	try:
		response_body = [chunk async for chunk in response.body_iterator]
		response.body_iterator = iterate_in_threadpool(iter(response_body))
		response_header = json.loads(response_body[0].decode())['header']
		rtn_code = response_header['rtnCode']

		response_header['tktime'] = process_time

		if rtn_code == "000000":
			rtn_message = "SUCCESS"
		else:
			rtn_message = response_header['rtnMessage']

		logger.info(f"completed_in={formatted_process_time}s / rtnCode={rtn_code} / rtnMessage={rtn_message}")

	finally:
		return response


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
	return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
	header = {
		"rtnCode": "000001",
		"rtnMessage": f'요청 데이터 오류 > {exc.errors()[0]["loc"]} / {exc.errors()[0]["msg"]}'
	}

	body = {}
	response = {'header': header, 'body': body}


	return JSONResponse(
		status_code=200,
		content=jsonable_encoder(response),
	)

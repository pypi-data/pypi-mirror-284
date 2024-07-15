import logging
import traceback

from starlette.responses import JSONResponse
from typing import Optional
from fastapi import APIRouter, Depends, Request, UploadFile, File
from fastapi.encoders import jsonable_encoder
from fastapi.logger import logger as fastapi_logger

from fastapi_hcytools.exceptions.api import exception_handler
from fastapi_hcytools.comm.utils import *
from fastapi_hcytools.model.sample import sample_model

router = APIRouter(
	prefix="/sample",  # url 앞에 고정적으로 붙는 경로추가
	tags=["sample"],
)

logger = logging.getLogger("sample_router")
fastapi_logger.handlers = logger.handlers
fastapi_logger.setLevel(logger.level)

@router.post("/sample", response_model=sample_model.response)
def sample(request: sample_model.request):
	try:
		logger.info(f'request data : {print_data(request.dict())}')

		res = {
			"header": {
				"trId": sample_model.trId,
				"rtnCode": "0",
				"rtnMessage": "Success"
			},
			"body": {
				"result": "sample"
			}
		}
		logger.info(f'response data : {print_data(res)}')
	except Exception as e:
		traceback.format_exc()
		res = exception_handler(e, sample_model.trId)
	finally:
		return res

import logging
from fastapi.responses import JSONResponse
from fastapi.logger import logger as fastapi_logger


logger = logging.getLogger("gunicorn.error")
fastapi_logger.handlers = logger.handlers
fastapi_logger.setLevel(logger.level)

class StatusCode:
	HTTP_500 = 500
	HTTP_400 = 400
	HTTP_401 = 401
	HTTP_403 = 403
	HTTP_404 = 404
	HTTP_405 = 405
	HTTP_422 = 422


class APIException(Exception):
	status_code: int
	rtnCode: str
	rtnMessage: str
	body: dict

	def __init__(self,
	             *,
	             status_code: int = StatusCode.HTTP_500,
	             rtnCode: str = "SP7100",
	             rtnMessage: str = None,
	             ex: Exception = None,
	             body: dict = None):
		self.status_code = status_code
		self.rtnCode = rtnCode
		self.rtnMessage = rtnMessage
		self.body = body if body is not None else {}
		super().__init__(ex)

def exception_handler(error, trId):
	from fastapi_hcytools.comm.utils import print_data
	if not isinstance(error, APIException):
		error = RequestDataError(str(error))
	error_dict = {
		"header": {
			"trId": trId,
			"rtnCode": error.rtnCode,
			"rtnMessage": error.rtnMessage
		},
		"body": error.body
	}
	logger.info(f'response data : \n{print_data(error_dict)}')
	res = JSONResponse(status_code=200, content=error_dict)
	return res

class RequestDataError(APIException):
	def __init__(self,  message: str = "", ex: Exception = None):
		super().__init__(
			status_code=StatusCode.HTTP_422,
			rtnMessage=f"요청 데이터 오류 > {message}",
			rtnCode="000001",
			ex=ex,
		)


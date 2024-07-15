from typing import Optional
from pydantic import BaseModel, validator
from fastapi_hcytools.model.base import *

trId = "100100"

class requestHeader(header):
	@validator('trId')
	def trId_check(cls, v):
		if trId != v:
			raise ValueError('Check trId Value')
		return v.title()

	pass

class request(BaseModel):
	header: requestHeader

	class Config:
		json_schema_extra = {
			"examples": [
				json.dumps({
					"header": {
						"trId": trId
					},
					"body":  {
						"project_name": "",
						"crt": "",
						"prk": "",
						"binary": "",
						"binary_index": 0
					}
				})
			]
		}

class responseBody(BaseModel):
	result: str

class response(BaseModel):
	header: responseHeader
	body: responseBody

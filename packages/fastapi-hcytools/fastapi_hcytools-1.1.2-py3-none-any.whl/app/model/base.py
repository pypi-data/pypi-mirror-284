from typing import Optional
import json
from pydantic import BaseModel

class header(BaseModel):
	trId: str

class responseHeader(header):
	rtnCode: str
	rtnMessage: str = ""


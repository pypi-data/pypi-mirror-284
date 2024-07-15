import os
import yaml
from dataclasses import dataclass


@dataclass
class Config:
	host: str = '0.0.0.0'
	port: int = 8000

	workers: int = 1
	logfile: str = './log/sample.log'
	loglevel: str = 'DEBUG'

	enc_mode: bool = False
	enc_param: str = ""

	def to_dict(self):
		return self.__dict__

	def update_from_dict(self, **kwargs):
		return self.__dict__.update(**kwargs)

	def load_config(self, config_file):
		if not os.path.isfile(config_file):
			raise ValueError(f"{config_file} is not exist")

		with open(config_file, encoding='utf-8') as fi:
			config_data = yaml.safe_load(fi)
			self.update_from_dict(**config_data)

		import platform
		from app.comm.utils import tobytes, tohexstr, SHA256, AES_ENC_CBC, AES_DEC_CBC, pad, unpad, RANDOM

		if self.enc_param == "":
			self.enc_param = tohexstr(RANDOM(32))

		system_key = (platform.processor() + platform.machine() + platform.system()).encode() + tobytes(self.enc_param)
		for _ in range(200):
			system_key = tobytes(SHA256(system_key))

		# if self.enc_mode:
		# 	self.db_password = unpad(AES_DEC_CBC(system_key, tobytes(self.db_password))).decode()
		# else:
		# 	db_password = tohexstr(AES_ENC_CBC(system_key, pad(self.db_password.encode())))
		# 	self.enc_mode = True
		# 	with open(config_file, 'w', encoding='utf-8') as fi:
		# 		config_data['db_password'] = db_password
		# 		config_data['enc_mode'] = self.enc_mode
		# 		config_data['enc_param'] = self.enc_param
		# 		yaml.dump(config_data, fi)
		#
		#
		# self.SQLALCHEMY_DATABASE_URL = f"mysql://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}?charset=utf8"
		#
		# print(self.SQLALCHEMY_DATABASE_URL)

	def get_gunicorn_log_dict(self):
		debug = ["console", "file"]
		release = ["file"]

		config = dict(
			version=1,
			disable_existing_loggers=False,

			root={"level": self.loglevel, "handlers": debug if self.loglevel == "DEBUG" else release},
			loggers={
				"gunicorn.error": {
					"level": self.loglevel,
					"handlers": ["console", "error_file"],
					"qualname": "error_log"
				},
				"gunicorn.access": {
					"level": self.loglevel,
					"handlers": ["console", "file"],
					"qualname": "access_log"
				},

			},
			handlers={
				"console": {
					"class": "logging.StreamHandler",
					"formatter": "generic",
					"stream": "ext://sys.stdout"
				},
				"error_file": {
					"class": "logging.handlers.TimedRotatingFileHandler",
					"filename": self.logfile + ".error.log",
					"when": "D",
					"formatter": "generic",
				},
				"file": {
					"class": "logging.handlers.TimedRotatingFileHandler",
					"filename": self.logfile,
					"when": "D",
					"formatter": "generic",
				}
			},
			formatters={
				"generic": {
					"format": '%(threadName)s %(asctime)s - %(name)s - %(levelname)s - %(message)s',
				}
			}
		)

		return config

	def get_uvicorn_log_dict(self):
		debug = ["console", "file"]
		release = ["file"]

		config = {
			"version": 1,
			"disable_existing_loggers": False,
			"formatters": {
				"generic": {
					"format": '%(threadName)s %(asctime)s - %(name)s - %(levelname)s - %(message)s',
				}
			},
			"handlers": {
				"console": {
					"class": "logging.StreamHandler",
					"formatter": "generic",
					"stream": "ext://sys.stdout"
				},
				"file": {
					"class": "logging.handlers.TimedRotatingFileHandler",
					"filename": self.logfile,
					"when": "D",
					"formatter": "generic",
					"encoding": "utf-8"
				},
				"error_file": {
					"class": "logging.handlers.TimedRotatingFileHandler",
					"filename": self.logfile + ".error.log",
					"when": "D",
					"formatter": "generic",
				}
			},
			"loggers": {
				"uvicorn": {"handlers": ["file"], "level": self.loglevel, "propagate": False},
				"uvicorn.error": {"handlers": ["error_file", "console"], "level": self.loglevel, "propagate": False},
				"uvicorn.access": {"handlers": ["file"], "level": self.loglevel, "propagate": False},
				"root": {
					"handlers": debug if self.loglevel == "DEBUG" else release, "level": self.loglevel
				},
			},
		}
		return config


config = Config()

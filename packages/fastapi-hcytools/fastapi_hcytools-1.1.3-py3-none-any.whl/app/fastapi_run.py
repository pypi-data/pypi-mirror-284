

def run(app, config):
	import uvicorn
	import sys

	# from app.main import app
	# from app.comm.config import Config

	# parser = argparse.ArgumentParser()
	#
	# parser.add_argument("-c", "--config", action="store", dest="config", help="config file path", default="config.yml")
	#
	# args = parser.parse_args()
	# config_file = args.config

	# config = Config()
	# config.load_config(config_file)

	if sys.platform == 'win32':
		uvicorn.run(app, host=config.host, port=config.port, http="httptools", log_config=config.get_uvicorn_log_dict())

	else:

		import gunicorn.app.base
		class StandaloneApplication(gunicorn.app.base.BaseApplication):

			def __init__(self, app, options=None):
				self.options = options or {}
				self.application = app
				super().__init__()

			def load_config(self):
				config = {key: value for key, value in self.options.items()
						  if key in self.cfg.settings and value is not None}
				for key, value in config.items():
					self.cfg.set(key.lower(), value)

			def load(self):
				return self.application

		options = {
			'worker_class': 'uvicorn.workers.UvicornWorker',
			'bind': f"{config.host}:{int(config.port)}",
			'workers': 1,
			'max_request': 0,
			'accesslog': config.logfile,
			'logconfig_dict': config.get_gunicorn_log_dict(),
			'preload_app': True,
		}
		print("##### RUN SERVER")

		StandaloneApplication(app, options).run()

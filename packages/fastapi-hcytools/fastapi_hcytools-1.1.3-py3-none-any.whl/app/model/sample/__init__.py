import os
import importlib

# 현재 패키지 경로
package_directory = os.path.dirname(os.path.abspath(__file__))

# 패키지 내 모든 모듈 import
for file in os.listdir(package_directory):
    # 파일 이름이 "__init__.py"인 경우, continue
    if file == "__init__.py":
        continue
    # 파일 이름이 ".py"로 끝나는 경우, 모듈 import
    if file.endswith(".py"):
        module_name = file[:-3]
        importlib.import_module("." + module_name, package=__name__)


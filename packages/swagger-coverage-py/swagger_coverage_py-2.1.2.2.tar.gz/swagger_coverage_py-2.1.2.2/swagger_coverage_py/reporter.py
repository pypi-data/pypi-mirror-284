import json
import os
import re
import shutil
from pathlib import Path
import platform

import requests


class CoverageReporter:
    def __init__(self, api_name: str, host: str):
        self.host = host
        self.swagger_doc_file = f"swagger-{api_name}.json"
        self.output_dir = f"{self.__get_output_dir()}-{api_name}"
        self.ignore_requests = []
        self.swagger_coverage_config = f"swagger-coverage-config-{api_name}.json"

    def __get_output_dir(self):
        output_dir = "swagger-coverage-output"
        subdir = re.match(r"(^\w*)://(.*)", self.host).group(2)
        return f"{output_dir}/{subdir}"

    def setup(self, path_to_swagger_json: str, auth: object = None):
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)

        link_to_swagger_json = f"{self.host}{path_to_swagger_json}"

        response = requests.get(link_to_swagger_json, auth=auth)
        assert response.ok, (
            f"Swagger doc is not pulled. See details: "
            f"{response.status_code} {response.request.url}"
            f"{response.content}\n{response.content}"
        )
        swagger_json_data = response.json()

        with open(self.swagger_doc_file, "w+") as f:
            swagger_json_data["swagger"] = "2.0"
            f.write(json.dumps(swagger_json_data))

    def is_any_files(self):
        _, _, files = next(os.walk(self.output_dir))
        if len(files) == 0:
            return False
        else:
            return True

    def generate_report(self, installed_as_module=True):
        inner_location = 'swagger-coverage-commandline/bin/swagger-coverage-commandline'

        if installed_as_module:
            cmd_path = os.path.join(os.path.dirname(__file__), inner_location)
            assert Path(cmd_path).exists(), cmd_path
        else:
            raise Exception(
                f"No commandline tools is found in following locations:\n{inner_location}\n"
            )

        if config := self.swagger_coverage_config:
            command = f"{cmd_path} -s {self.swagger_doc_file} -i {self.output_dir} -c {config}"
        else:
            command = f"{cmd_path} -s {self.swagger_doc_file} -i {self.output_dir}"

        command = command if platform.system() != "Windows" else command.replace("/", "\\")

        if self.is_any_files():
            os.system(command)

    def cleanup_input_files(self):
        shutil.rmtree(self.output_dir, ignore_errors=True)

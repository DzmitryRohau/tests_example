import requests
from requests import Response

from tests.core.helpers.converters import load_json


def _check_status_code(expected_status_code: int, response: Response):
    try:
        actual_status_code = response.status_code
        text = response.text
    except Exception():
        raise Exception("Wrong response structure")
    if expected_status_code != actual_status_code:
        raise Exception("Wrong status code. Actual = " + str(actual_status_code) + " Expected = " +
                        str(expected_status_code) + " and text message: '" + text + "'.")


class RestUtil:
    data_dict = load_json()
    server_name = data_dict["server_name"]

    def post(self, path: str, input_params: dict, content_type: str = data_dict["correct_content_type"],
             expected_status_code: int = 200, token: str = None) -> Response:
        if token is None:
            headers = {"Content-Type": content_type}
        else:
            headers = {"Content-Type": content_type, "Authorization": "Bearer " + token}
        response = requests.post(url=self.server_name + path, json=input_params, headers=headers)
        _check_status_code(expected_status_code=expected_status_code, response=response)
        return response

    def get(self, path: str, content_type: str = data_dict["correct_content_type"],
            expected_status_code: int = 200, token: str = "") -> Response:
        if token == "":
            headers = {"Content-Type": content_type}
        else:
            headers = {"Content-Type": content_type, "Authorization": "Bearer " + token}
        response = requests.get(url=self.server_name + path, headers=headers)
        _check_status_code(expected_status_code=expected_status_code, response=response)
        return response

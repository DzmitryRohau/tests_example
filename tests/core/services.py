from requests import Response

from tests.core.helpers.converters import load_json
from tests.core.helpers.response_helper import \
    get_json_data_from_response, \
    get_access_token_from_response
from tests.core.helpers.rest_util import RestUtil


class Services:
    rest_util = RestUtil()
    data_dict = load_json()

    def get_valid_login_params(self) -> dict:
        return self.data_dict["params"]["valid_login_params"]

    def get_login_path(self) -> str:
        return self.data_dict["path"]["login_path"]

    def do_post_request(self, params: dict, path: str,
                        content_type: str = data_dict["correct_content_type"],
                        expected_status_code: int = 200, token: str = None) -> Response:
        return self.rest_util.post(path=path, input_params=params,
                                   content_type=content_type,
                                   expected_status_code=expected_status_code,
                                   token=token)

    def get_token_from_response(self, response: Response) -> str:
        json_data = get_json_data_from_response(response=response)
        return get_access_token_from_response(json_data=json_data)

    def get_incorrect_content_type(self) -> str:
        return self.data_dict["incorrect_content_type"]

    def get_params_for_test_cases(self) -> dict:
        return self.data_dict["params"]["params_for_test_cases"]

    def get_path_for_test_cases(self) -> str:
        return self.data_dict["path"]["path_for_test_cases"]

    def get_path_to_get_all_test_suites(self) -> str:
        return self.data_dict["path"]["path_to_get_all_test_suites"]

    def do_get_request(self, token, path):
        return self.rest_util.get(path=path, token=token)

    def get_path_to_create_test_suit(self) -> str:
        return self.data_dict["path"]["path_to_create_test_suit"]

    def get_params_to_create_test_suit(self) -> dict:
        return self.data_dict["params"]["params_to_create_test_suit"]

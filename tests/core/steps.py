from requests import Response

from tests.core.services import Services


class Steps:
    services = Services()

    def __get_params_and_login_path(self) -> (dict, str):
        return self.services.get_valid_login_params(), self.services.get_login_path()

    def __get_params_and_login_path_for_test_cases(self) -> (dict, str):
        return self.services.get_params_for_test_cases(), self.services.get_path_for_test_cases()

    def __get_path_to_get_all_test_suites(self) -> str:
        return self.services.get_path_to_get_all_test_suites()

    def __get_params_and_path_to_create_test_suit(self) -> (dict, str):
        return self.services.get_params_to_create_test_suit(), self.services.get_path_to_create_test_suit()

    def login_and_return_token(self) -> str:
        params, login_path = self.__get_params_and_login_path()
        response = self.services.do_post_request(params=params, path=login_path)
        token = self.services.get_token_from_response(response=response)
        return token

    def login_with_incorrect_content_type(self, expected_status_code: int) -> Response:
        params, login_path = self.__get_params_and_login_path()
        incorrect_content_type = self.services.get_incorrect_content_type()
        return self.services.do_post_request(params=params, path=login_path,
                                             content_type=incorrect_content_type,
                                             expected_status_code=expected_status_code)

    def post_request_to_create_test_cases(self, token: str, expected_status_code: int = 200) -> Response:
        params, path_test_cases = self.__get_params_and_login_path_for_test_cases()
        response = self.services.do_post_request(params=params, path=path_test_cases, token=token,
                                                 expected_status_code=expected_status_code)
        return response

    def get_request_to_get_all_test_suites(self, token: str) -> Response:
        path_get_all_test_suites = self.__get_path_to_get_all_test_suites()
        response = self.services.do_get_request(token=token, path=path_get_all_test_suites)
        return response

    def post_request_to_create_test_suit(self, token) -> Response:
        params, create_test_suit_path = self.__get_params_and_path_to_create_test_suit()
        response = self.services.do_post_request(token=token, path=create_test_suit_path, params=params)
        return response

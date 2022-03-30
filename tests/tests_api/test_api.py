from tests.core.helpers.response_helper import get_json_data_from_response, get_text_from_response
from tests.core.steps import Steps


class TestApi:
    steps = Steps()

    def test_valid_login(self):
        access_token = self.steps.login_and_return_token()
        assert access_token is not None and access_token != ""

    def test_valid_login_and_invalid_content_type(self):
        response = self.steps.login_with_incorrect_content_type(expected_status_code=415)
        assert response is not None

    def test_post_test_case_iteration_one(self, get_access_token):
        response = self.steps.post_request_to_create_test_cases(token=get_access_token,
                                                                expected_status_code=404)
        text = get_text_from_response(response=response)
        assert text == '{\n  "message": "Test suite does not exist"\n}\n'

    def test_get_all_test_suites(self, get_access_token):
        response = self.steps.get_request_to_get_all_test_suites(token=get_access_token)
        text = get_text_from_response(response=response)
        assert text == '{\n  "test_suites": []\n}\n'

    def test_post_test_suit(self, get_access_token):
        response = self.steps.post_request_to_create_test_suit(token=get_access_token)
        text = get_text_from_response(response=response)
        assert text == \
               '{\n  "id": "1", \n  "message": "Test suite successfully added"\n}\n'

    def test_get_all_test_suites_iteration_two(self, get_access_token):
        response = self.steps.get_request_to_get_all_test_suites(token=get_access_token)
        data = get_json_data_from_response(response=response)
        assert data["test_suites"][0]["title"] == "title"

    def test_post_test_case_iteration_two(self, get_access_token):
        response = self.steps.post_request_to_create_test_cases(token=get_access_token)
        text = get_text_from_response(response=response)
        assert text == '{\n  "id": "1", \n  "message": "Test case successfully added"\n}\n'

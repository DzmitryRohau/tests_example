import pytest

from tests.core.steps import Steps


@pytest.fixture()
def get_access_token():
    return Steps().login_and_return_token()

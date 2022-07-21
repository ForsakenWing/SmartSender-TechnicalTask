import pytest
import requests
from Common import Config, Payloads


@pytest.fixture(autouse=True, scope="class")
def config():
    cfg = Config()
    return cfg


@pytest.fixture(autouse=True, scope="class")
def headers(config):
    return {"Access-Token": config.token}


class TestSmartSenderAPI:

    def test_account_info(self, config, headers):
        response = requests.post(
            url=config.account_info_url,
            headers=headers
        )
        assert response.json() == Payloads.successful_account_info

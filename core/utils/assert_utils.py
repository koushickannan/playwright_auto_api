import self
from assertpy import assert_that

from core.utils.logger_config import get_logger

logger = get_logger(module_name=__name__)


class Assertions:

    @staticmethod
    def assert_status_code(status_code, expected_status):
        logger.info("Status code : %s", status_code)
        assert_that(status_code).is_equal_to(expected_status.value)

    @staticmethod
    def assert_response_contains(response, key):
        assert_that(response).contains(key)

    @staticmethod
    def assert_response_key_equal(response, key, value):
        assert_that(response[key]).is_equal_to(value)

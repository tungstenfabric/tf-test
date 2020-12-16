from functools import wraps
from datetime import datetime
from common import log_orig as contrail_logging
logger = contrail_logging.getLogger('auth')


def preposttest_wrapper(function):
    @wraps(function)
    def wrapper(self, *args, **kwargs):
        logger.info('=' * 80)
        logger.info('STARTING TEST: % s', function.__name__)
        start_time = datetime.now().replace(microsecond=0)
        doc = function.__doc__
        if doc:
            logger.info('TEST DESCRIPTION : %s', doc)
        try:
            function(self, *args, **kwargs)
        except Exception as e:
            logger.error(e)
            test_time = datetime.now().replace(microsecond=0) - start_time
            logger.info(
                "END TEST : %s : FAILED[%s]", function.__name__, test_time)
            logger.info('-' * 80)
        finally:
            test_time = datetime.now().replace(microsecond=0) - start_time
            logger.info(
                "END TEST : %s : PASSED[%s]", function.__name__, test_time)
            logger.info('-' * 80)
    return wrapper

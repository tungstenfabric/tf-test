from functools import wraps
from datetime import datetime
from common import log_orig as contrail_logging
import testtools
logger = contrail_logging.getLogger('auth')


def preposttest_wrapper(function):
    @wraps(function)
    def wrapper(self, *args, **kwargs):
        logger.info('=' * 80)
        logger.info('STARTING TEST: % s', function.__name__)
        start_time = datetime.now().replace(microsecond=0)
        status = 'PASSED'
        doc = function.__doc__
        if doc:
            logger.info('TEST DESCRIPTION : %s', doc)
        try:
            function(self, *args, **kwargs)
        except Exception as e:
            logger.error(e)
            status = 'FAILED'
        finally:
            test_time = datetime.now().replace(microsecond=0) - start_time
            logger.info(
                "END TEST : %s : %s[%s]", function.__name__, status, test_time)
            logger.info('-' * 80)
    return wrapper


def attr(*args, **kwargs):
    """A decorator which applies the  testtools attr decorator

    This decorator applies the testtools.testcase.attr if it is in the list of
    attributes to testtools we want to apply.
    """

    def decorator(f):
        if 'type' in kwargs and isinstance(kwargs['type'], str):
            f = testtools.testcase.attr(kwargs['type'])(f)
        elif 'type' in kwargs and isinstance(kwargs['type'], list):
            for attr in kwargs['type']:
                f = testtools.testcase.attr(attr)(f)
        return f

    return decorator

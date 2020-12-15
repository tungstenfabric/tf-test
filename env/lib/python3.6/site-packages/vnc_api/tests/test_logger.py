import os
import shutil
import tempfile

from testtools import TestCase

from vnc_api.vnc_api import CurlLogger, DEFAULT_LOG_DIR


class TestCurlLogger(TestCase):
    def test_absolute_logfile(self):
        """Tests the logger when absoulte path of the
           logfile is specified
        """
        tmp_dir = tempfile.mkdtemp()
        logfile = os.path.join(tmp_dir, 'vnc-api.log')
        log = CurlLogger(log_file=logfile)
        log.curl_logger.debug("Test absolute log file")
        self.assertTrue(os.path.exists(logfile))

    def test_with_logfile_name(self):
        """Tests the logger when only logfile name is specified
        """
        logfile = 'vnc-api.log'
        log = CurlLogger(log_file=logfile)
        log.curl_logger.debug("Test log file")
        result = (os.path.exists(os.path.join("/var/log/contrail", logfile)) |
                  os.path.exists(os.path.join(DEFAULT_LOG_DIR, logfile)))
        self.assertTrue(result)
        shutil.rmtree(DEFAULT_LOG_DIR, ignore_errors=True)
# end class TestCurlLogger

import pytest
import sys

def run_tests():
    errno = pytest.main("tests/test_decode.py tests/test_encode.py")
    sys.exit(errno)

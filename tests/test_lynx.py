import lynx
import sys
import pytest
import os

def run_tests():
    errno = pytest.main("tests/test_lynx.py")
    sys.exit(errno)


def load(filename):
    path = os.path.join(os.path.dirname(__file__), "config_files", filename)
    with open(path, "r") as fp:
        return lynx.load(fp)

def test_sections_works_correctly():
    config = load("sections.conf")
    assert(config[0].name() == config[1].name() == "section")
    sub_section2 = config[0].sub_sections()[0]
    assert(sub_section2.name() == "subsection2")
    assert(sub_section2.sub_sections()[0].name() == "subsection3")


def test_fields_works_correctly():
    config = load("fields.conf")
    fields = config[0].fields()
    assert(len(fields) == 2)
    assert(fields["my field"] == "hello world")
    assert(fields["hello~!&*#"] == "hello~!&*# world")


def test_lists_works_correctly():
    config = load("lists.conf")
    fields = config[0].fields()
    assert(len(fields) == 2)
    assert(fields["my list"] == ["1" , "myvalue", "3", "5"])
    assert(fields["list2"] == ["%$3", "!$^", "value2"])



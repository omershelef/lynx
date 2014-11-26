import os
import lynx


def load(filename):
    path = os.path.join(os.path.dirname(__file__), "config_files", filename)
    with open(path, "r") as fp:
        return lynx.load(fp)


def test_decode_sections():
    config = load("sections.conf")
    assert(config[0].name() == config[1].name() == "section")
    sub_section2 = config[0].sub_sections()[0]
    assert(sub_section2.name() == "subsection2")
    assert(sub_section2.sub_sections()[0].name() == "subsection3")


def test_decode_fields():
    config = load("fields.conf")
    fields = config[0].fields()
    assert(len(fields) == 2)
    assert(fields["my field"] == "hello world")
    assert(fields["hello~!&*#"] == "hello~!&*# world")


def test_decode_lists():
    config = load("lists.conf")
    fields = config[0].fields()
    assert(len(fields) == 2)
    assert(fields["my list"] == [1 , "myvalue", 3, 57.874])
    assert(fields["list2"] == ["%$3", "!$^", "value2"])


def test_decode_nums():
    config = load("nums.conf")
    fields = config[0].fields()
    assert(len(fields) == 2)
    assert(fields["myint"] == 57)
    assert(fields["myfloat"] == 89.4563)


def test_decode_multiline():
    config = load("multiline.conf")
    fields = config[0].fields()
    assert(len(fields) == 3)
    assert(fields["myfield"] == "mytest")
    assert(fields["mymulti"] == """
hello world
bla bla bla

bla bla

hello world
   how are u?
       are u ok?
    """.strip())
    assert(fields["myfield2"] == "mytest2")

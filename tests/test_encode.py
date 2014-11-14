import lynx

def test_encode_one_section():
    section = lynx.Section("mysection", [], {})
    result = lynx.dumps(section)
    config = lynx.loads(result)
    assert(len(config) == 1)
    assert(config[0].name() == "mysection")

def test_encode_multiple_sections():
    sub_section = lynx.Section("mysection2", [], {})
    section = lynx.Section("mysection", [sub_section], {})
    result = lynx.dumps([section, section])
    config = lynx.loads(result)
    assert(len(config) == 2)
    assert(config[0].name() == "mysection")
    assert(config[0].sub_sections()[0].name() == "mysection2")

def test_encode_fields():
    fields = {"myfield": "value", "field2": "hello#$%"}
    section = lynx.Section("mysection", [], fields)
    result = lynx.dumps(section)
    config = lynx.loads(result)
    r_fields = config[0].fields()
    assert(len(r_fields) == 2)
    assert(r_fields["myfield"] == "value")
    assert(r_fields["field2"] == "hello#$%")

def test_encode_lists():
    fields = {"myfield": ["hello", "world", 75, 88.32]}
    section = lynx.Section("mysection", [], fields)
    result = lynx.dumps(section)
    config = lynx.loads(result)
    r_fields = config[0].fields()
    assert(len(r_fields) == 1)
    assert(r_fields["myfield"] == ["hello", "world", 75, 88.32])

def test_encode_nums():
    fields = {"myfield": 52, "field2": 37.68}
    section = lynx.Section("mysection", [], fields)
    result = lynx.dumps(section)
    config = lynx.loads(result)
    r_fields = config[0].fields()
    assert(len(r_fields) == 2)
    assert(r_fields["myfield"] == 52)
    assert(r_fields["field2"] == 37.68)

from lynx import format

def encode(sections):
    # support one or multiple sections
    if isinstance(sections, format.Section):
        sections = [sections]

    return "\n\n".join(_encode_section(sec, 0) for sec in sections)

def _encode_section(section, indention):
    all_fields = "".join(_encode_field(name, value, indention + 1) for name, value in section.fields().items())
    sub_sections = "".join("\n\n%s\n" % _encode_section(sec, indention + 1) for sec in section.sub_sections())
    format_dic = {"tabs": ("\t" * indention), "sec": section.name(), "fields": all_fields, "sub_sec": sub_sections}
    return "%(tabs)s%(sec)s {\n%(fields)s%(sub_sec)s%(tabs)s}" % format_dic

def _encode_field(name, value, indention):
    # encode as list
    if hasattr(value, "__iter__") and not isinstance(value, str):
       value = "[%s]" % ", ".join(map(str, value))
    else:
        value = str(value)

    return "%s%s: %s\n" % ("\t" * indention, name, value)

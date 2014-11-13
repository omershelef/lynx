class Section(object):
    def __init__(self, name, sections, fields):
        self._name = name
        self._fields = fields
        self._sections = sections

    def name(self):
        """ Returns the section name """
        return self._name

    def sub_sections(self):
        """ Return a list of sub sections """
        return self._sections

    def fields(self):
        """ Return a dictionary of section's fields """
        return self._fields


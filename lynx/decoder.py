import re
from lynx import format

class Decoder(object):
    def decode(self, str):
        self.str = str.strip()
        self.pos = 0
        result = []
        while self.pos < len(self.str):
            result.append(self._scan_part())
        return result

    def _scan_part(self):
        self._skip_comments()
        match = re.compile("[{}:]").search(self.str[self.pos:])
        name = self.str[self.pos:self.pos + match.start()].strip()
        c = match.group()
        self.pos += match.end()

        if (c == "{"):
            return self._scan_section(name)
        elif (c == "}"):
            return None
        elif (c == ":"):
            return self._scan_field(name)


    def _scan_section(self, name):
        fields = {}
        sections = []

        while True:
            result = self._scan_part()

            if result is None:
                break
            elif isinstance(result, format.Section):
                sections.append(result)
            else:
                fields.update(result)

        return format.Section(name, sections, fields)


    def _scan_field(self, name):
        match = re.compile("^\s*[|\[]").search(self.str[self.pos:])

        if match == None:
            return {name: self._scan_string()}

        self.pos += match.end()

        if match.group().strip() == "[":
            return {name: self._scan_list()}

    def _scan_string(self):
        match = re.compile("\n").search(self.str[self.pos:])
        value = self.str[self.pos:self.pos + match.start()].strip()
        self.pos += match.end()
        return value


    def _scan_list(self):
        match = re.compile("\]").search(self.str[self.pos:])
        value = self.str[self.pos:self.pos + match.start()].strip()
        self.pos += match.end()
        return [val.strip() for val in value.split(",")]

    def _skip_comments(self):
        match = re.compile("^\s*#").search(self.str[self.pos:])
        if not match is None:
            self.pos += match.end()
            match = re.compile("\n").search(self.str[self.pos:])
            self.pos += match.end()

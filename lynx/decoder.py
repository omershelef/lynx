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

        if match is None:
            raise format.WrongFormatException("Expected ':' or '{'. position: %s" % self.pos)

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
            return {name: self._scan_field_value()}

        self.pos += match.end()

        if match.group().strip() == "[":
            return {name: self._scan_list()}
        elif match.group().strip() == "|":
            scanner = MultilineScanner(self.str, self.pos)
            self.pos, multiline_str = scanner.scan()
            return {name: multiline_str}

    def _scan_field_value(self):
        match = re.compile("\n").search(self.str[self.pos:])
        value = self.str[self.pos:self.pos + match.start()].strip()
        self.pos += match.end()
        return self._cast(value)

    def _scan_list(self):
        match = re.compile("\]").search(self.str[self.pos:])

        if match is None:
            raise format.WrongFormatException("Expected ']'. position: %s" % self.pos)

        value = self.str[self.pos:self.pos + match.start()].strip()
        self.pos += match.end()
        return [self._cast(val.strip()) for val in value.split(",")]

    def _skip_comments(self):
        match = re.compile("^\s*#").search(self.str[self.pos:])
        if not match is None:
            self.pos += match.end()
            match = re.compile("\n").search(self.str[self.pos:])
            self.pos += match.end()

    def _cast(self, value):
        """
        Try to cast value to int or float if possible
        :param value: value to cast
        :return: casted value
        """
        if value.isdigit():
            value = int(value)
        elif re.compile("^\d+\.\d+").match(value):
            value = float(value)
        return value



class MultilineScanner(object):

    def __init__(self, str, start_position):
        self._str = str
        self._pos = start_position

        # return to the start of the line
        temp_pos = self._pos - 1
        while temp_pos > 0:
            if self._str[temp_pos] == '\n':
                break
            temp_pos -= 1

        self._indent_level = self._get_indent_level(self._str[temp_pos + 1:self._pos])

    def scan(self):
        current_str = ""
        lines = self._str[self._pos:].split('\n')
        self._pos += len(lines[0]) + 1
        first_indent_level = None
        for line in lines[1:]:
            indent = self._get_indent_level(line)

            # empty lines
            if indent is None:
                current_str += line + "\n"
                self._pos += len(line) + 1
                continue

            if first_indent_level is None:
                first_indent_level = indent

            if indent <= self._indent_level:
                return (self._pos, current_str.strip())

            self._pos += len(line) + 1
            current_str += line[first_indent_level:] + "\n"

        return (self._pos, current_str.strip())

    def _get_indent_level(self, line):
        match = re.compile("\S").search(line)
        if match is None:
            return None
        return match.end() - 1

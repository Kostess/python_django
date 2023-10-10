class Alphabet:
    regex = "[a-z, A-Z]{1}"

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return "%04d" % value
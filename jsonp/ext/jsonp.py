from .base import FormatterBase
import json


class Parser(FormatterBase):
    """A very basic formatter.
    """
    def format(self, data):
        return str(json.dumps(data, indent=4))

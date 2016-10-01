from .base import FormatterBase
import json

class Complex(FormatterBase):
    """A very basic formatter.
    """

    def format(self, data):
        """Format the data and return unicode text.
        :param data: A dictionary with string keys and simple types as
                     values.
        :type data: dict(str:?)
        """
        for name, value in sorted(data.items()):
            line = '{name} = {value}\n'.format(
                name=name,
                value=value,
            )
            yield line


class Complex2(FormatterBase):
    def format(self, data):
        for name, value in sorted(data.items()):
            line = '{name} + {value}\n'.format(
                name=name,
                value=value,
            )
            yield line

class Complex3(FormatterBase):
    def format(self, data):
        yield "*" * 100
        for name, value in sorted(data.items()):
            line = '{name}  {value}\n'.format(
                name=name,
                value=value,
            )
            yield line
        yield "*" * 100

class Complex4(FormatterBase):
    def format(self, data):
        yield json.dumps(data, indent=4)

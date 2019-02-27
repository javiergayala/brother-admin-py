# -*- coding: utf-8 -*-

"""Exceptions module."""


class BrotherAdminError(Exception):
    """Base Class for all other errors."""


class PrinterNameTypeError(TypeError):
    """Raised when you do not define the printer name as a string."""

    def __init__(self, **kwargs):
        msg = "Printer name must be provided as a string."
        Exception.__init__(self, msg)

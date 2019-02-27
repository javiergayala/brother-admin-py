# -*- coding: utf-8 -*-

"""Main module."""

import requests

from brother_admin.exceptions import PrinterNameTypeError


class Printer(object):
    """Obtain and parse stats from the printer."""

    def __init__(self, name=None):
        """Initialize the Printer Object.

        Keyword Arguments:
            name {str} -- Name or IP of the printer (default: {None})

        Raises:
            PrinterNameTypeError -- Raised if the given input is not a string

        """
        if not isinstance(name, str):
            raise PrinterNameTypeError
        self.name = name
        self.csv_url = "http://%s/etc/mnt_info.csv" % self.name

    def raw_stats(self):
        """Return the raw CSV stats from the printer.

        Returns:
            requests object -- Object returned from requesting the printer stats

        """
        return requests.get(self.csv_url)

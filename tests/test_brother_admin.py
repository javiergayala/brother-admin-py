#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `brother_admin` package."""

import pytest
import requests
import responses

from brother_admin import brother_admin
from brother_admin.exceptions import PrinterNameTypeError


@pytest.fixture
def mock_csv():
    """Create a mocked CSV file response."""
    _csv = """Node Name,Model Name,Location,Contact,IP Address,Serial No.,Main Firmware Version,Sub1 Firmware Version,Memory Size,Page Counter,Average Coverage,% of Life Remaining(Drum Unit),% of Life Remaining(Toner),A4/Letter,Legal/Folio,B5/Executive,Envelopes,A5,Others,Plain/Thin/Recycled,Thick/Thicker/Bond,Envelopes/Env. Thick/Env. Thin,Label,Hagaki,Total,Total 2-sided Print,Copy,Copy 2-sided Print,Print,Print 2-sided Print,Others,Others 2-sided Print,ADF Scan,Flatbed Scan,Scan Page Count,Replace Count(Toner),Replace Count(Drum Unit),Total Paper Jams,Jam Tray 1,Jam Inside,Jam Rear,Jam 2-sided,Total Paper Jams(ADF),Error Count 1,Error Count 2,Error Count 3,Error Count 4,Error Count 5,Error Count 6,Error Count 7,Error Count 8,Error Count 9,Error Count 10
TEST,Brother DCP-L2550DW series,-,-,127.0.0.1,U00000000000000,L,1.00,128,1,4.01,99,99,1,0,0,0,0,0,1,0,0,0,0,1,0,2,0,1,0,0,0,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"""
    return _csv


@pytest.fixture
def response(requests_mock):
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


@responses.activate
def test_printer_response(mock_csv):
    """Test that the raw stats are requested."""
    _name = "test.local"
    _p = brother_admin.Printer(name=_name)
    responses.add(responses.GET, _p.csv_url, body=mock_csv, status=200)
    assert _p.raw_stats()


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_printer_creation_name():
    """Instantiate the class with a name."""
    return brother_admin.Printer(name="test.local")


def test_printer_creation_ip():
    """Instantiate the class with an IP."""
    return brother_admin.Printer(name="127.0.0.1")


def test_printer_creation_failure():
    """Instantiate the class with no string given."""
    with pytest.raises(PrinterNameTypeError):
        _p = brother_admin.Printer()

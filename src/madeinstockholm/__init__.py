#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
madeinstockholm
----------
TODO: Add description
"""

from flask import Blueprint


__title__ = 'madeinstockholm'
__version__ = '1.0.0'
__build__ = 100
__author__ = 'Martin Sandström'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014-2016 Martin Sandström'


PAGE_SIZE = 10
GA_TRACKING = ""

theme = Blueprint('madeinstockholm', __name__,
                  static_folder="static",
                  static_url_path='/static/madeinstockholm',
                  template_folder='templates')

import views  # NOQA
import filters  # NOQA

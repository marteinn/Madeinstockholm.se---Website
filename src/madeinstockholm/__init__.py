#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
madeinstockholm
----------
TODO: Add description
"""

from flask import Blueprint


PAGE_SIZE = 10
GA_TRACKING = ""

theme = Blueprint('madeinstockholm', __name__,
                  static_folder="static",
                  static_url_path='/static/madeinstockholm',
                  template_folder='templates')

import views  # NOQA
import filters  # NOQA

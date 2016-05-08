#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import inspect

import dotenv


# Load your .env vars before proceeding
try:
    inspect_file = inspect.getfile(inspect.currentframe())
    env_path = os.path.dirname(os.path.abspath(inspect_file))
    dotenv.load_dotenv("%s/.env" % (env_path,))
except Exception, e:
    pass

os.environ.setdefault("ATOMICPRESS_SETTINGS", "settings.prod")

from atomicpress import app
app.setup()

if __name__ == "__main__":
    app.run()

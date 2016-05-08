import os

from .base import *  # NOQA

# Base
PROJECT_ROOT = Path(__file__).ancestor(2)
DB_PATH = os.path.join(PROJECT_ROOT, "blog-test.db")
UPLOADS_PATH = os.path.join(PROJECT_ROOT, "uploads-test")

# dotenv.load_dotenv(PROJECT_ROOT.child(".env"))

SQLALCHEMY_DATABASE_URI = "sqlite:////%s" % DB_PATH
THEME = "atomicpress.themes.minimal"

# Config
DEBUG = True
SECRET_KEY = "SECRET KEY"
FREEZER_BASE_URL = "/blog-test/"
STATIC_URL = os.path.join(FREEZER_BASE_URL, "static")
UPLOADS_URL = os.path.join(FREEZER_BASE_URL, "uploads")
GIST_BACKEND_RENDERING = False
SITE_URL = "http://marteinn.se/blog"

# TODO: Move this logic
if not os.path.exists(UPLOADS_PATH):
    os.makedirs(UPLOADS_PATH)

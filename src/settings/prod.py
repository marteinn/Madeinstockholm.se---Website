import os

from .base import *  # NOQA


DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY")
FREEZER_BASE_URL = "/blog/"
STATIC_URL = os.path.join(FREEZER_BASE_URL, "static")
UPLOADS_URL = os.path.join(FREEZER_BASE_URL, "uploads")
GIST_BACKEND_RENDERING = False
SITE_URL = "http://marteinn.se/blog"

FREEZER_DESTINATION = os.path.join(PROJECT_ROOT, "blog")

GA_TRACKING = os.environ.get("GA_TRACKING")

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_REGION = os.environ.get("AWS_REGION", None)
AWS_S3_CALLING_FORMAT = os.environ.get("AWS_S3_CALLING_FORMAT", None)
S3_BUCKET = os.environ.get("S3_BUCKET")
S3_DESTINATION = os.environ.get("S3_DESTINATION")

SQLALCHEMY_TRACK_MODIFICATIONS = False

import os


PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

DB_PATH = os.path.join(PROJECT_ROOT, "blog.db")
UPLOADS_PATH = os.path.join(PROJECT_ROOT, "uploads")

SQLALCHEMY_DATABASE_URI = "sqlite:////%s" % DB_PATH
THEME = "madeinstockholm"

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import os.path as op

from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.script import Manager, prompt_bool
from flask.ext.frozen import Freezer

from mis.app import app, db
from mis import models
from mis.views import views
from mis.admin import create_admin
from mis import s3_utils
from mis.initial import setup_initial

from mis import config

manager = Manager(app)

app.register_module(views, url_prefix="")

@manager.command
def createdb(initial_data=False):
    """
    Create database (if not created) and if -i is appended, insert initial data.

    python manage.py createdb -i
    """

    db.create_all()
    print "DB Created"

    # Setup inital data
    if initial_data:
        setup_initial()
        print "Initial data added"

@manager.command
def dropdb():
    """
    Remove sqlite database

    python manage.py dropdb
    """

    if prompt_bool("Are you sure?"):
        db.drop_all()
        # TODO: Remove db file?

@manager.command
def runserver(admin=False, toolbar=False, debug=False):
    """
    We use our own runserver (instead of flask-script, so we can toggle
    admin, debug and toolbar views.

    python manage.py runserver -a -t
    """

    if toolbar:
        bar = DebugToolbarExtension(app)

    if admin:
        create_admin()

    app.run(debug=debug)

@manager.command
def build():
    """
    Build static version of website.

    python manage.py build
    """

    # Create freeze
    freezer = Freezer(app)

    @freezer.register_generator
    def uploaded_file():
        path = op.join(op.dirname(__file__), 'mis/uploads')
        file_list = os.listdir(path)
        for file in file_list:
            if file.find(".")>0:
                yield {'filename': file}

    # TODO: Exclude static/less and static/lib
    freezer.run()

@manager.command
def deploy():
    """
    Deploy project to S3.
    """

    s3_utils.upload_dir(config.AWS_ACCESS_KEY_ID,
        config.AWS_ACCESS_KEY,
        config.S3_BUCKET_NAME,
        "mis/%s" % (config.FREEZER_DESTINATION,)
        )

if __name__ == "__main__":
    manager.run()

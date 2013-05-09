import os.path as op
from flask import render_template, send_from_directory
from flask import Module
from models import Site, Post, Project, Person
from sqlalchemy import asc, func
import config

views = Module(__name__)

@views.route("/")
def index():
    sites = Site.query.all()
    site = sites[0]

    posts = Post.query.order_by(asc(Post.order)).filter(Post.published==True)
    projects = Project.query.order_by(asc(Project.order)).filter(Post.published==True)
    persons = Person.query.order_by(func.random()).all()

    return render_template("index.html",
        site=site,
        posts=posts,
        projects=projects,
        persons=persons,
        ga_account=config.GA_TRACKING_ID,
        site_description=site.description,
    )

@views.route("/uploads/<filename>")
def uploaded_file(filename):
    path = op.join(op.dirname(__file__), 'uploads')
    return send_from_directory(path,
        filename)
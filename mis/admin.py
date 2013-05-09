import os.path as op
from flask import current_app
from flask.ext.admin import Admin, expose, AdminIndexView
from flask.ext.admin.contrib.fileadmin import FileAdmin
from flask.ext.admin.contrib.sqlamodel import ModelView
from app import db
import models

class HomeView(AdminIndexView):
    @expose("/")
    def index(self):
        return self.render('admin/home.html')

def create_admin():

    app = current_app._get_current_object()

    admin = Admin(app, "Made In Stockholm", index_view=HomeView(name='Home'))

    admin.add_view(ModelView(models.Site, db.session))
    admin.add_view(ModelView(models.Post, db.session))

    admin.add_view(ModelView(models.Project, db.session,
        category="Project"))
    admin.add_view(ModelView(models.ProjectLink, db.session,
        category="Project"))

    admin.add_view(ModelView(models.Person, db.session))

    path = op.join(op.dirname(__file__), '../mis/uploads')
    admin.add_view(FileAdmin(path, '/uploads/', name='Upload files'))
from app import db

class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(200))
    title = db.Column(db.String(200))
    description = db.Column(db.Text())
    contact = db.Column(db.String(200))

    def __unicode__(self):
        return self.title

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(200))
    title = db.Column(db.String(200))
    content = db.Column(db.Text())
    pub_date = db.Column(db.DateTime)
    published = db.Column(db.Boolean())
    order = db.Column(db.Integer)

    def __unicode__(self):
        return self.title

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(200))
    name = db.Column(db.String(200))
    title = db.Column(db.String(200))
    content = db.Column(db.Text())
    image = db.Column(db.String(300))
    large_image = db.Column(db.String(300))
    pub_date = db.Column(db.DateTime)
    published = db.Column(db.Boolean())
    order = db.Column(db.Integer)

    def __unicode__(self):
        return self.name

class ProjectLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(300))
    title = db.Column(db.String(200))
    description = db.Column(db.String(200))
    link = db.Column(db.String(300))

    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    project = db.relationship("Project", backref=db.backref('projectlinks'))

    def __unicode__(self):
        return self.title


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(300))
    name = db.Column(db.String(200))
    content = db.Column(db.Text())
    image = db.Column(db.String(300))

    def __unicode__(self):
        return self.name
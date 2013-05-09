#!/usr/bin/env python
# -*- coding: utf-8 -*-

import models
from app import app, db

def setup_initial():
    """
    Create initial data when createdb are run from manage.py
    :return:
    """
    site = models.Site()
    site.slug = "mis"
    site.title = u"MadeInStockholm"
    site.contact = "hello@madeinstockholm.se"
    site.description = u"We are a small software and product company from Sweden."
    db.session.add(site)

    post = models.Post()
    post.slug = "headline"
    post.title = u"We are a small software and product company from Sweden."
    post.content = u"Our idea is simple. Love what you do and make great things."
    post.order = 0
    post.published = True
    db.session.add(post)

    post = models.Post()
    post.slug = "headline"
    post.title = u"Hello there, this is a hidden post"
    post.content = u"""Lorem ipsum dolor sit amet, consectetur adipisicing
                               "elit, sed do eiusmod tempor incididunt ut labore et
                               "dolore magna aliqua. Ut enim ad minim veniam, quis no."""
    post.order = 1
    post.published = False
    db.session.add(post)

    project = models.Project()
    project.slug = "vinylwall"
    project.image = "vinylwall-intro-4.png"
    project.name = u"VinyWall"
    project.title = u"Put your vinyls in one place"
    project.content = u"VinylWall is a app that helps you manage your Vinyl "\
                      u"collection. Flip through your collection or tag "\
                      u"something new, all this and a little more is included "\
                      u"in one beautiful interface."
    project.order = 0
    project.published = True
    db.session.add(project)

    link = models.ProjectLink()
    link.slug = "vw-android"
    link.link = "https://play.google.com/store/apps/details?id=net.vinylwall.app"
    link.project = project
    link.title = u"VinylWall for Android"
    db.session.add(link)

    link = models.ProjectLink()
    link.slug = "vw-ios"
    link.link = "https://itunes.apple.com/app/id635737755"
    link.project = project
    link.title = u"VinylWall for iOS"
    db.session.add(link)

    person = models.Person()
    person.name = u"Martin Sandström"
    person.image = "avatar-1.png"
    person.content = u'Developer<br /><a href="http://twitter.com/marteinn_se">@marteinn_se</a>'
    db.session.add(person)

    person = models.Person()
    person.name = u"Mattias Broden"
    person.image = "avatar-2.png"
    person.content = u'Designer<br /><a href="http://twitter.com/EntireStudio">@EntireStudio</a>'
    db.session.add(person)

    db.session.commit()
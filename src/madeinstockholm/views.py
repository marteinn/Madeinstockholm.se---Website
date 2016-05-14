from flask import render_template
from sqlalchemy import desc, asc, func
from atomicpress.models import Blog, Post, PostType, Category, Tag

from madeinstockholm import theme, helpers


@theme.route("/")
def start():
    blog = Blog.query.all()[0]
    start_page = Post.query.filter(Post.name == 'startpage')[0]
    projects = Post.query.filter(Post.parent == start_page,
                                 Post.type == PostType.POST)\
        .filter(helpers.gen_post_status())\
        .order_by(Post.order.desc())

    return render_template("pages/start.html",
                           blog=blog,
                           page=start_page,
                           projects=projects,
                           # posts=posts,
                           # projects=projects,
                           # persons=persons,
                           # ga_account=config.GA_TRACKING_ID,
                           # site_description=site.description,
                           )

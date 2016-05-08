from flask import render_template
from sqlalchemy import desc, asc, func
from atomicpress.models import Blog, Post, PostType, Category, Tag

from madeinstockholm import theme


@theme.route("/")
def start():
    blog = Blog.query.all()[0]
    start_page = Post.query.filter(Post.name == 'startpage')[0]
    projects = Post.query.filter(Post.parent == start_page,
                                 Post.type == PostType.POST)

    # posts = Post.query.order_by(desc(Post.date)).\
        # filter(Post.type == PostType.POST)

    # category_obj = Category.query.filter(Category.slug == category)
    # category_obj = category_obj.slice(0, 1)
    # if category_obj.count() == 0:
        # raise Exception("Category %s does not exist" % (category,))

    # category_obj = category_obj[0]
    # posts = posts.filter(Post.categories.contains(category_obj))

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

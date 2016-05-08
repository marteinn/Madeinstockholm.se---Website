from atomicpress.app import app
from atomicpress.models import Post, PostType


@app.template_filter('nav_menu_items')
def nav_menu_items(post):
    items = Post.query.filter(Post.parent == post,
                              Post.type == PostType.NAVIGATION_MENU)
    return items


@app.template_filter('has_nav_menu_items')
def has_nav_menu_items(post):
    # TODO: Make this more performant
    items = Post.query.filter(Post.parent == post,
                              Post.type == PostType.NAVIGATION_MENU)

    return items.count() != 0


@app.template_filter('post_images')
def post_images(post):
    items = Post.query.filter(Post.parent == post,
                              Post.type == PostType.ATTACHMENT)
    return items


@app.template_filter('has_post_images')
def has_post_images(post):
    # TODO: Make this more performant
    items = Post.query.filter(Post.parent == post,
                              Post.type == PostType.ATTACHMENT)

    return items.count() != 0

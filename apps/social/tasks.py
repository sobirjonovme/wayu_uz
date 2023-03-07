from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .scraping import GetInstagramPost
from apps.social.models import InstagramPost


@shared_task(name="get_instagram_posts")
def get_insta_posts(username):
    loader = GetInstagramPost()
    print("begin")
    # delete all previous posts
    InstagramPost.objects.all().delete()
    # download and store new posts (last 10 post from user)
    loader.download_user_posts(username)
    print("end")

import instaloader
import requests
from django.conf import settings
from .models import InstagramPost


class GetInstagramPost:
    def __init__(self) -> None:
        self.L = instaloader.Instaloader()

    def download_user_posts(self, username):
        posts = instaloader.Profile.from_username(self.L.context, username).get_posts()
        count = 0

        for post in posts:
            count += 1

            url = post.url
            response = requests.get(url)

            if response.status_code == 200:
                file_short_path = f"instagram/{post.shortcode}.jpg"
                file_full_path = f"{settings.BASE_DIR}/media-files/{file_short_path}"
                post_url = f"https://instagram.com/p/{post.shortcode}"
                with open(file_full_path, "wb") as f:
                    f.write(response.content)

                db_post = InstagramPost()
                db_post.image = file_short_path
                db_post.image2 = file_short_path
                db_post.link = post_url
                db_post.save()

            if count >= 10:
                break


if __name__ == "__main__":
    cls = GetInstagramPost()
    cls.download_user_posts("cristiano")

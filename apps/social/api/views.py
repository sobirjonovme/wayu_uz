from rest_framework.views import APIView
from rest_framework.response import Response

from apps.social.scraping import GetInstagramPost
from apps.social.models import InstagramPost
from .serializer import InstagramPostSerializer


class GetPostAPIView(APIView):

    def get(self, request):
        cls = GetInstagramPost()
        # delete all previous posts
        InstagramPost.objects.all().delete()
        # download and store new posts (last 10 post from user)
        cls.download_user_posts("cristiano")

        posts = InstagramPost.objects.all().order_by('-id')
        ser = InstagramPostSerializer(posts, many=True)

        return Response(ser.data, status=200)

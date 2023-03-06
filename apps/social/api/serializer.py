from rest_framework import serializers

from apps.social.models import InstagramPost


class InstagramPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstagramPost
        fields = ('id', 'image', 'link')
        read_only_field = ('image', 'link')


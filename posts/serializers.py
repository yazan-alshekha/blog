
from django.db.models import fields
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields=['tittle','author','updated','timestamp','content','published']
        model=Post


        
from rest_framework import serializers
from .models import Blog

#class serilazer for Blog
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
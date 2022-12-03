from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ('post', 'id', 'user', 'parent', 'body', 'created', 'reply')
        read_only_fields = ['user']
    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many = True)
        serializer.bind('', self)
        return serializer.data
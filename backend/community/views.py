from rest_framework import viewsets
#from rest_framework import permissions

from .serializers import CommentSerializer
from .models import Comment

class CommentViewSet(viewsets.ModelviewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.data(user = self.request.user)
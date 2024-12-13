from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def partial_update(self, request, pk):
        post = Post.objects.get(pk=pk)
        transition_method = request.data['status'] + '_status_transition'
        getattr(post, transition_method)()
        post.save()
        return Response('Details Updated')

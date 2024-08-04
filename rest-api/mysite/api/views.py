from django.shortcuts import render
from .serializers import BlogPostSerializer
from .models import Blogpost
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset=Blogpost.objects.all()
    serializer_class=BlogPostSerializer

    def delete(self,request,*args,**kwargs):
        Blogpost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blogpost.objects.all()
    serializer_class=BlogPostSerializer
    lookup_field='pk'    

class BlogPostList(APIView):
    def get(self, request, format=None):
        
        title=request.query_params.get('title','')
        if title:
            blog_posts=Blogpost.objects.filter(title__icontains=title)
        else:
            blog_posts=Blogpost.objects.all()

        serializer=BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
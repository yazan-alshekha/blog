
from django.shortcuts import render

# import  generics in order to create a views
from rest_framework import generics, permissions, serializers

# import serializers and models
from .serializers import PostSerializer
from .models import Post

#import a class we made in order to edit the permissions  
from .permissions import testAuthenticated

# Create your views here.

#ListAPIView >-- you can reveiw all items
#ListCreateAPIView >--you can reveiw all items or create new one 
class PosteList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    
    ## you can use filter to filter the data 
    # queryset=Post.objects.filter(published=True)
    
    # the name of the Serializer you made
    serializer_class=PostSerializer
    # add permission to the view 
    permission_classes=(testAuthenticated,)

# detail view
#RetrieveAPIView >-- just to read for one item
#RetrieveUpdateAPIView >- you can read one item or update it 
#RetrieveUpdateDestroyAPIView >-you can read one item or update or delete
class PosteDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    # the name of the Serializer you made
    serializer_class=PostSerializer
    # add permission to the view 
    permission_classes=(testAuthenticated,)
1. **add new file to the your app
name it *"serializers.py"***

2. **add the folowing to it**

```
from django.db.models import fields
from rest_framework import serializers
#import the model
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        #fields it is the names of the model 
        fields = ['tittle','author','updated','timestamp','content']
        ##model it is the name of the table(model)
        model = Post

```

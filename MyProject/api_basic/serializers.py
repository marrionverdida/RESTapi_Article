from rest_framework import serializers
from .models import Article

# Indicate which field to display


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields =['id', 'title', 'author', 'email']
        fields = '__all__' #display all field

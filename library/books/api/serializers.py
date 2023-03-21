from rest_framework import serializers
from books import models

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Books
        field= ['idBook', 'title', 'author', 'releaseYear', 'state', 'pages', 'publishingCompany', 'createAt']

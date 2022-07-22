from os import name
from rest_framework import serializers
from .models import Post, Artist, Song, Album, Genre





class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.user_name')
    album_name = serializers.ReadOnlyField(source='album.name')
    artist_name = serializers.ReadOnlyField(source='artist.name')
    class Meta:
        model = Post
        fields = ('id', 'title', 'album', 'artist','content', 'author', 'status', 'author_name', 'rating', 'album_name', 'artist_name', 'likes')


class PostDateSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.user_name')
    album_name = serializers.ReadOnlyField(source='album.name')
    artist_name = serializers.ReadOnlyField(source='artist.name')
    class Meta:
        model = Post
        fields = ('id', 'title', 'album', 'artist', 'content', 'author',
                  'status', 'author_name', 'rating', 'published', 'album_name', 'artist_name', 'likes')




class AlbumSerializer(serializers.ModelSerializer):
    artist_name = serializers.ReadOnlyField(source='artist.name')
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(),
                                         many=True, slug_field="name")
    posts = PostDateSerializer(many=True, read_only=True)
    
    class Meta:
        model = Album
        fields = ('name', 'artist', 'songs', 'id', 'posts',
                  'image', 'release', 'avg_rating', 
                  'artist_name', 'genre')
    
    


class AlbumSerializerReduced(serializers.ModelSerializer):
    artist_name = serializers.ReadOnlyField(source='artist.name')
    genre = serializers.SlugRelatedField(queryset=Genre.objects.all(),
        many=True, slug_field="name")
    postlength = serializers.SerializerMethodField()
    class Meta:
        model = Album
        fields = ('name', 'image',
                  'artist_name', 'genre', 'postlength', 'release')
                  
    def get_postlength(self,obj):
        return obj.posts.count()

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializerReduced(many=True, read_only=True)
    
    class Meta:
        model = Artist
        fields = ('name', 'albums', 'image_url', 'id', 'bio', 'birthday')


class GenreSerializer(serializers.ModelSerializer):
    album_list = AlbumSerializerReduced(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ('name', 'id', 'album_list')


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('album', 'title', 'duration')

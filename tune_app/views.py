from django.shortcuts import render, redirect
from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from .models import Artist, Post, Genre, Album, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import JsonResponse, QueryDict
from rest_framework.views import APIView
from .serializers import PostSerializer, ArtistSerializer, AlbumSerializer, GenreSerializer, SongSerializer, PostDateSerializer, AlbumSerializerReduced
from django.conf import settings
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.db.models import Avg
from rest_framework.throttling import UserRateThrottle

import random

import logging 

class PostUserWritePermission(BasePermission):
    message = 'You can only edit your own posts.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class PostList(generics.ListCreateAPIView):
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostListwithDate(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDateSerializer
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostListUser(generics.ListAPIView):
    serializer_class = PostDateSerializer

    def get_queryset(self):
        slug = self.kwargs.get('pk')
        obj = Post.objects.filter(author=slug)
        return obj

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = 'name'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('pk')
        obj = Artist.objects.get(name=slug)
        return obj

class ArtistListDetailfilter(generics.ListAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['$name']




class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'name'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('pk')
        obj = Genre.objects.get(name=slug)
        return obj

class RecommendedAlbums(generics.ListAPIView):
    # queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get_queryset(self):
        slug = self.kwargs.get('pk')
        obj = Album.objects.all()

        def has_author_return_genres(obj) :
            genres = []
            
            slug = self.kwargs.get('pk')
            for album in obj:
                posts = Post.objects.filter(album=album.id)
                for post in posts:
                    logging.warning(post.title)
                    if post.author.id == slug and post.rating >= 3:
                        genrelist = list(album.genre.all().values())
                        for genre in genrelist:
                            genres.append(genre['name'])
            return genres
        def given_genres_return_albums(genres):
            slug = self.kwargs.get('pk')
            albums = []
            for genresingle in genres:
                for album in obj:
                    posts = list(Post.objects.filter(album=album.id).values())
                    genrelist = list(album.genre.all().values())
                    if any(ele['name'] == genresingle for ele in genrelist):
                        if not any(post['author_id'] == slug for post in posts):
                            albums.append(album.name)
            return albums


        genrelist = list(set(has_author_return_genres(obj)))
        albumlist = given_genres_return_albums(genrelist)
        logging.warning(type(genrelist))
        logging.warning(genrelist)
        logging.warning(type(albumlist))
        logging.warning(albumlist)
        logging.warning(type(obj))
        queryset = Album.objects.filter(name__in=albumlist)
        final = random.choice(queryset)
        return [final]

class GenreListDetailfilter(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['$name']



class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer




class AlbumList(generics.ListAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

class CreateAlbum(APIView):
    parser_classes = [MultiPartParser, FormParser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # def post(self, request, format=None):
    #     print(request.data)
    #     genres = request.data.pop('genre', [])
    #     instance = Album.objects.create(request.data)
    #     temp = str(genres)
    #     temp2 = str(temp)[1:-1]
    #     temp3 = temp2.strip('\'').replace(',','')
    #     array = temp3.split(' ')
    #     for g in array:
    #         al=Genre.objects.get_or_create(name=g['name'])
    #         instance.genre.add(al)
    #     serializer = AlbumSerializer(data=instance)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request, *args, **kwargs):
        posts_serializer = AlbumSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = 'name'
    
    def get_object(self, queryset=None):
        slug = self.kwargs.get('pk')
        obj = Album.objects.get(name=slug)
        first = Post.objects.filter(album=obj.id).aggregate(Avg('rating'))
        second = list(first.values())[0]
        print(type(obj))
        obj.avg_rating = second
        return obj
        
    
class AlbumListDetailfilter(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['$name']
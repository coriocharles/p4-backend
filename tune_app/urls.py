from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'tune_app'

urlpatterns = (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)) + [
    # # path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='PostDetail'),
    path('posts/', views.PostList.as_view(), name='PostList'),
    path('postsdate/', views.PostListwithDate.as_view(), name='PostListDate'),
    path('posts/user/<int:pk>', views.PostListUser.as_view(), name='PostListUser'),
    path('', TemplateView.as_view(template_name="tune_app/index.html")),

    path('artists/<str:pk>', views.ArtistDetail.as_view(), name='ArtistDetail'),
    path('artists/', views.ArtistList.as_view(), name='ArtistList'),
    path('search/artists/', views.ArtistListDetailfilter.as_view(), name='searchArtist'),

    path('genres/<str:pk>', views.GenreDetail.as_view(), name='GenreDetail'),
    path('genres/', views.GenreList.as_view(), name='GenreList'),
    path('search/genres/', views.GenreListDetailfilter.as_view(),
         name='searchGenre'),

    path('albums/create', views.CreateAlbum.as_view(), name='AlbumCreate'),
    path('albums/<str:pk>', views.AlbumDetail.as_view(), name='AlbumDetail'),
    path('albums/', views.AlbumList.as_view(), name='AlbumList'),
    path('search/albums/', views.AlbumListDetailfilter.as_view(),
         name='searchAlbums'),
    path('albums/recommended/<int:pk>',
         views.RecommendedAlbums.as_view(), name='AlbumList'),

    path('songs/<int:pk>', views.SongDetail.as_view(), name='SongDetail'),
    path('songs/', views.SongList.as_view(), name='SongList'),
    # path('albums/<int:pk>/reviews', views.PostReviews.as_view(), name='PostReviews'),
    
]


from django.conf.urls import url
from django.urls import re_path, path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'music'

urlpatterns = [

    # /music/api/albums
    url(r'^api/albums$', views.AlbumList.as_view()),

    # /music/
    path('', views.index, name='index'),

    # /music/login_user
    url(r'^login_user/$', views.login_user, name='login_user'),

    # /music/register/
    re_path(r'^register/$', views.register, name='register'),

    # /music/logout_user
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # /music/<album_id>/delete
    re_path(r'^album/(?P<album_id>[0-9]+)/delete$', views.delete_album, name='delete_album'),

    # /music/<album_id>/favourite
    re_path(r'^album/(?P<album_id>[0-9]+)/favourite', views.favourite_album, name='favorite_album'),

    # /music/create_album/
    re_path(r'^album/create_album', views.create_album, name='create_album'),

    # /music/<album_id>, detail view expects primary key, hence pk
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/<album_id>/create_song/
    re_path(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),

    # /music/<song_id>/favourite/
    re_path(r'^(?P<song_id>[0-9]+)/favourite/$', views.favourite_song, name='favourite_song'),

    # /music/<album_id>/delete_song/<song_id>/
    re_path(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)$', views.delete_song, name='delete_song'),

    # /music/<album_id>/delete_song/<song_id>/
    re_path(r'^songs/(?P<filter_by>[a-zA-Z]+)/$', views.songs, name='songs'),

    # re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add
    re_path(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2
    re_path(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete
    # re_path(r'^album/(?P<pk>[0-9]+)/delete$', views.AlbumDelete.as_view(), name='album-delete'),
]


urlpatterns = format_suffix_patterns(urlpatterns)

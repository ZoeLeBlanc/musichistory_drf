from django.contrib import admin
from django.contrib.auth.models import User
from shakeitup.models import *

admin.site.unregister(User)
admin.site.register(User)
admin.site.register(playlist_model.Playlist)
admin.site.register(album_model.Album)
admin.site.register(albumsbygenres_model.Album_By_Genre)
admin.site.register(artist_model.Artist)
admin.site.register(artistsonalbums_model.Artist_On_Album)
admin.site.register(genre_model.Genre)
admin.site.register(song_model.Song)
admin.site.register(songsbygenres_model.Song_By_Genre)
admin.site.register(songsonalbums_model.Song_On_Album)
admin.site.register(songsonplaylists_model.Song_On_Playlist)


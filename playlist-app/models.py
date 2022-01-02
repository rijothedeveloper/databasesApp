"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = "playlists"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                    autoincrement=True)
    
    name = db.Column(db.String,
                    nullable=False)
    
    description = db.Column(db.String,
                            nullable=False)
    
    playlist_songs = db.relationship('PlaylistSong', backref='playlists')


class Song(db.Model):
    """Song."""

    __tablename__ = "songs"

    id = db.Column(db.Integer,
                   primary_key=True,
                    autoincrement=True)
    
    title = db.Column(db.String,
                    nullable=False)
    
    artist = db.Column(db.String,
                            nullable=False)
    
    playlist_songs = db.relationship('PlaylistSong', backref='songs')


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    
    __tablename__ = "playlists_songs"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                    autoincrement=True)
    
    playlist_id = db.Column(db.Integer,
                        db.ForeignKey('playlists.id', ondelete="CASCADE"))

    song_id = db.Column(db.Integer,
                        db.ForeignKey('songs.id', ondelete="CASCADE"))
    
    #constructor
    def __init__(self, playlist_id=None, song_id=None):
        self.playlist_id = playlist_id
        self.song_id=song_id
    
# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
    

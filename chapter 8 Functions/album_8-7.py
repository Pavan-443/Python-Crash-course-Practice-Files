def make_album(artist_name, title, noof_songs=None):
    """returns info about music album in a dictionary"""
    album = {}
    album['artist name'] = artist_name.title()
    album['song title'] = title.title()
    if noof_songs:
        album['no of songs'] = noof_songs
    return album

print(make_album('dasari', 'hari', '123'))
print(make_album('ladjf', 'kljfa'))
print(make_album('ajsdf', 'lkahdf'))
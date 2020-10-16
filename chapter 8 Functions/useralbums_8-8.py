def make_album(artist_name, title, noof_songs=None):
    """returns info about music album in a dictionary"""
    album = {}
    album['artist name'] = artist_name.title()
    album['song title'] = title.title()
    if noof_songs:
        album['no of songs'] = noof_songs
    return album

while True:
    print('\ntype q to quit at any time')
    name = input('please enter the Artist name: ')
    if name.lower() == 'q':
        break
    title = input('please enter title of the song: ')
    if title.lower() == 'q':
        break
    print(make_album(name, title))

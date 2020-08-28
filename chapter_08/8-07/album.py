def make_album(artist, title, num_songs=None):
    if num_songs:
        return({'artist': artist.title(),
                'title': title.title(),
                'number of songs': num_songs})
    else:
        return({'artist': artist.title(),
                'title': title.title()})


print(make_album('queens of the stone age', 'songs for the dead'))
print(make_album('metallica', 'master of puppets', 8))
print(make_album('iron maiden', 'the number of the beast'))

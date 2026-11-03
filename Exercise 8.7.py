def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if songs is not None:
        album["songs"] = songs

    return album

print(make_album("Reality Club", "Never Get Better"))
print(make_album("Reality Club", "What Do You Really Know?"))
print(make_album("Reality Club", "Reality Club Presents..."))
print(make_album("Reality Club", "Never Get Better", 13))
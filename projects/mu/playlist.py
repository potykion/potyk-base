with open('playlist.md', encoding='utf-8') as f:
    tracks = f.readlines()
    tracks = list(map(str.strip, tracks))
    tracks = [line.strip('[]') for line in tracks]
    tracks = [track.replace('>', '_') for track in tracks]

all_artists = set()


def artists_from_track():
    parts = track.rsplit('-', 1)
    parts = list(map(str.strip, parts))
    artists_str, _ = parts
    artists = artists_str.split(',')
    artists = list(map(str.strip, artists))
    return artists


for track in tracks:
    artists = artists_from_track()

    with open(f"negro-dnb/tracks/{track}.md", 'w', encoding='utf-8') as f:
        # f.write('#playlist\n\n')
        for artist in artists:
            f.write(f'[[{artist}]]\n\n ')

    all_artists.update(artists)

for artist in all_artists:
    with open(f"negro-dnb/artists/{artist}.md", 'w'):
        pass
